import { useEffect } from 'react';
import './App.css';
import useOSStore from './store/useOSStore';

import BootScreen from './components/BootScreen';
import Starfield from './components/Starfield';
import NeuralCanvas from './components/NeuralCanvas';
import Topbar from './components/Topbar';
import WidgetArea from './components/WidgetArea';
import AppGrid from './components/AppGrid';
import Dock from './components/Dock';
import WindowManager from './components/WindowManager';
import NeuralTerminal from './components/NeuralTerminal';
import MorphOverlay from './components/MorphOverlay';
import ToastContainer from './components/ToastContainer';
import FederationPanel from './components/FederationPanel';
import SettingsApp from './components/AppWindows/SettingsApp';

function App() {
  const bootComplete = useOSStore((s) => s.bootComplete);
  const federationPanelOpen = useOSStore((s) => s.federationPanelOpen);
  const settingsOpen = useOSStore((s) => s.settingsOpen);
  const closeSettings = useOSStore((s) => s.closeSettings);
  const goHome = useOSStore((s) => s.goHome);
  const toggleTerminal = useOSStore((s) => s.toggleTerminal);
  const toggleAdmin = useOSStore((s) => s.toggleAdmin);
  const toggleFederationPanel = useOSStore((s) => s.toggleFederationPanel);

  // Keyboard shortcuts
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      // Ctrl/Cmd + ` (backtick) — Toggle terminal
      if ((e.metaKey || e.ctrlKey) && e.key === '`') {
        e.preventDefault();
        toggleTerminal();
      }
      // Ctrl/Cmd + Shift + A — Toggle admin
      if ((e.metaKey || e.ctrlKey) && e.shiftKey && e.key === 'A') {
        e.preventDefault();
        toggleAdmin();
      }
      // Escape — Close active window / go home
      if (e.key === 'Escape') {
        if (settingsOpen) closeSettings();
        else if (federationPanelOpen) toggleFederationPanel();
        else goHome();
      }
      // Ctrl/Cmd + Shift + F — Toggle federation panel
      if ((e.metaKey || e.ctrlKey) && e.shiftKey && e.key === 'F') {
        e.preventDefault();
        toggleFederationPanel();
      }
    };

    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [toggleTerminal, toggleAdmin, goHome, toggleFederationPanel, settingsOpen, closeSettings, federationPanelOpen]);

  // Mesh pulse interval
  useEffect(() => {
    if (!bootComplete) return;
    const interval = setInterval(() => {
      const state = useOSStore.getState();
      useOSStore.setState({
        mesh: {
          ...state.mesh,
          nodes: Math.min(64, state.mesh.nodes + (Math.random() > 0.7 ? 1 : 0)),
          messages: state.mesh.messages + Math.floor(Math.random() * 3),
          coherence: Math.max(0.5, Math.min(1, state.mesh.coherence + (Math.random() - 0.5) * 0.05)),
        },
      });
    }, 5000);
    return () => clearInterval(interval);
  }, [bootComplete]);

  return (
    <>
      {/* Boot Screen */}
      <BootScreen />

      {/* Background layers */}
      <Starfield />
      <NeuralCanvas />

      {/* Main OS shell */}
      {bootComplete && (
        <>
          <div className={`desktop ${federationPanelOpen ? 'desktop-federation-open' : ''}`}>
            <Topbar />
            <WidgetArea />
            <AppGrid />
          </div>

          <Dock />

          {/* Overlays */}
          <WindowManager />
          <NeuralTerminal />
          <MorphOverlay />
          <ToastContainer />
          <FederationPanel />

          {/* Settings overlay */}
          {settingsOpen && (
            <div className="window-overlay" onClick={closeSettings}>
              <div
                className="window-container"
                onClick={(e) => e.stopPropagation()}
                style={{ maxWidth: '700px' }}
              >
                <div className="window-header">
                  <div className="window-title">
                    <span>⚙️</span> Settings
                  </div>
                  <div className="window-controls">
                    <button className="window-btn min" onClick={closeSettings}>
                      <span className="text-xs">−</span>
                    </button>
                    <button className="window-btn max" onClick={closeSettings}>
                      <span className="text-xs">□</span>
                    </button>
                    <button className="window-btn close" onClick={closeSettings}>
                      <span className="text-xs">×</span>
                    </button>
                  </div>
                </div>
                <div className="window-body">
                  <SettingsApp />
                </div>
              </div>
            </div>
          )}
        </>
      )}
    </>
  );
}

export default App;
