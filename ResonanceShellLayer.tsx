export const resonanceTheme = {
  primary: '#c084fc',
  secondary: '#8b5cf6',
  background: '#090414'
};

export function mountResonanceShell(runtime) {
  return {
    ...runtime,
    shell: {
      mode: 'resonance',
      overlay: true,
      runtimePreserved: true,
      messagePassingVisible: true
    }
  };
}

export function createTelemetryPanel(app) {
  return {
    id: app.id,
    lineage: app.lineage,
    morphs: app.morphs,
    health: app.health,
    graph: app.relationships
  };
}