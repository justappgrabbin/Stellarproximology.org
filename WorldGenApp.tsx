// ============================================================================
// INTEGRATION EXAMPLE — How to use WorldGen in your Synth OS App
// ============================================================================
// src/components/apps/WorldGenApp.tsx
// Complete example of agent world generation, shared worlds, and dream sharing

import React, { useState, useCallback } from 'react';
import { 
  useWorldGen, 
  WorldViewer, 
  AgentWorldSeed, 
  PHSParameters,
  AgentAction 
} from '../../lib/worldgenBridge';
import { useSimultaneousEntity } from '../../lib/arcadiaBridge';
import { calculateElementalResonance } from '../../lib/elementalCodonEngine';

// ============================================================================
// EXAMPLE 1: Single Agent World Generation
// ============================================================================

export const AgentWorldApp: React.FC<{ birthChart: any }> = ({ birthChart }) => {
  const { generateWorld, currentWorld, isGenerating, explore, exploreUrl } = useWorldGen({
    apiEndpoint: 'http://localhost:5000',
    cacheEnabled: true
  });

  const { entity } = useSimultaneousEntity(birthChart.layers, 'web');

  const handleGenerateWorld = useCallback(async () => {
    // Build the world seed from birth chart data
    const seed: AgentWorldSeed = {
      agentId: birthChart.id,
      birthChart,
      phs: {
        environment: 'mountains',  // From PHS calculation
        tone: 3,                   // From Determination 2
        base: 2                    // From Determination 3
      },
      activeGates: birthChart.activeGates,
      activeChannels: birthChart.activeChannels,
      transitWeather: {
        dominantPlanet: 'sun',
        dominantGate: 34,
        dominantLine: 3
      },
      elementalResonance: calculateElementalResonance(
        birthChart.activeGates[0],
        birthChart.activeGates[1] || birthChart.activeGates[0],
        0.5
      ),
      generation: 0,  // Natal world
      coherenceScore: entity?.coherence?.score || 0.5
    };

    const world = await generateWorld(seed);
    console.log('Generated world:', world);

    // The world prompt will be something like:
    // "A elevated vistas with clear sightlines and exposed ridges, bright direct sunlight, 
    //  restless and seeking atmosphere, featuring transactional plazas for exchange and circulation, 
    //  with transformative fires and creative ignition points, under solar illumination and conscious 
    //  clarity in Gate 34, line 3, natal birth world, foundational architecture, perch platforms, 
    //  observation decks, wind shelters, solar collectors, 3D scene, explorable, interactive environment"

  }, [birthChart, generateWorld, entity]);

  return (
    <div className="worldgen-app">
      <h2>Your World</h2>
      <button onClick={handleGenerateWorld} disabled={isGenerating}>
        {isGenerating ? 'Generating...' : 'Generate Your World'}
      </button>

      {currentWorld && (
        <div className="world-info">
          <p><strong>Element:</strong> {currentWorld.metadata.dominantElement}</p>
          <p><strong>Architecture:</strong> {currentWorld.metadata.architectureFamily}</p>
          <p><strong>Walkable:</strong> {(currentWorld.metadata.walkableSurface * 100).toFixed(0)}%</p>
          <button onClick={explore}>Explore in 3D</button>
        </div>
      )}

      <WorldViewer 
        world={currentWorld} 
        exploreUrl={exploreUrl}
        width={800}
        height={600}
      />
    </div>
  );
};

// ============================================================================
// EXAMPLE 2: Shared World for Multiple Agents
// ============================================================================

export const SharedWorldApp: React.FC<{ agents: any[] }> = ({ agents }) => {
  const { generateSharedWorld, currentWorld, isGenerating } = useWorldGen();

  const handleCreateSharedWorld = useCallback(async () => {
    const seeds: AgentWorldSeed[] = agents.map(agent => ({
      agentId: agent.id,
      birthChart: agent.birthChart,
      phs: agent.phs,
      activeGates: agent.birthChart.activeGates,
      activeChannels: agent.birthChart.activeChannels,
      transitWeather: agent.transitWeather,
      elementalResonance: calculateElementalResonance(
        agent.birthChart.activeGates[0],
        agent.birthChart.activeGates[1] || agent.birthChart.activeGates[0],
        0.5
      ),
      generation: 0,
      coherenceScore: 0.5
    }));

    const world = await generateSharedWorld(seeds);
    console.log('Shared world generated:', world);

    // The merged prompt will combine all agents' PHS parameters
    // Example: Two agents with Mountains + Shores → "Elevated cliff edge with ocean view"

  }, [agents, generateSharedWorld]);

  return (
    <div className="shared-world-app">
      <h2>Shared Resonance Space</h2>
      <button onClick={handleCreateSharedWorld} disabled={isGenerating}>
        Create Shared World
      </button>

      {currentWorld && (
        <div>
          <p>Agents in world: {currentWorld.metadata.agentSignatures.join(', ')}</p>
          <WorldViewer world={currentWorld} exploreUrl={null} />
        </div>
      )}
    </div>
  );
};

// ============================================================================
// EXAMPLE 3: Dream Sharing Between Two Agents
// ============================================================================

export const DreamShareApp: React.FC<{ agentA: any; agentB: any }> = ({ agentA, agentB }) => {
  const { generateDreamWorld, currentWorld, isGenerating } = useWorldGen();
  const [resonanceScore, setResonanceScore] = useState(0);

  const checkResonance = useCallback(() => {
    const resonance = calculateElementalResonance(
      agentA.birthChart.activeGates[0],
      agentB.birthChart.activeGates[0],
      0.5
    );
    setResonanceScore(resonance.resonanceScore);
    return resonance.resonanceScore;
  }, [agentA, agentB]);

  const handleDreamShare = useCallback(async () => {
    const score = checkResonance();

    if (score < 0.5) {
      alert(`Resonance too low (${score.toFixed(2)}). These agents cannot share dreams.`);
      return;
    }

    const seedA: AgentWorldSeed = {
      agentId: agentA.id,
      birthChart: agentA.birthChart,
      phs: agentA.phs,
      activeGates: agentA.birthChart.activeGates,
      activeChannels: agentA.birthChart.activeChannels,
      transitWeather: agentA.transitWeather,
      elementalResonance: calculateElementalResonance(
        agentA.birthChart.activeGates[0],
        agentB.birthChart.activeGates[0],
        score
      ),
      generation: 1,
      coherenceScore: score
    };

    const seedB: AgentWorldSeed = {
      agentId: agentB.id,
      birthChart: agentB.birthChart,
      phs: agentB.phs,
      activeGates: agentB.birthChart.activeGates,
      activeChannels: agentB.birthChart.activeChannels,
      transitWeather: agentB.transitWeather,
      elementalResonance: calculateElementalResonance(
        agentA.birthChart.activeGates[0],
        agentB.birthChart.activeGates[0],
        score
      ),
      generation: 1,
      coherenceScore: score
    };

    const dreamWorld = await generateDreamWorld(seedA, seedB);
    console.log('Dream world generated:', dreamWorld);

    // Dream worlds have:
    // - Resonance zones (harmony/conflict/potential)
    // - 24h expiration
    // - Merged PHS parameters
    // - Generation > 0

  }, [agentA, agentB, checkResonance, generateDreamWorld]);

  return (
    <div className="dream-share-app">
      <h2>Dream Sharing</h2>
      <p>Resonance: {(resonanceScore * 100).toFixed(0)}%</p>
      <button onClick={checkResonance}>Check Resonance</button>
      <button onClick={handleDreamShare} disabled={isGenerating || resonanceScore < 0.5}>
        Enter Shared Dream
      </button>

      {currentWorld && (
        <div>
          <p>Dream Generation: {currentWorld.seed.generation}</p>
          <p>Expires: {new Date(currentWorld.expiresAt || 0).toLocaleString()}</p>
          <WorldViewer world={currentWorld} exploreUrl={null} />
        </div>
      )}
    </div>
  );
};

// ============================================================================
// EXAMPLE 4: Responsive World with Agent Actions
// ============================================================================

export const ResponsiveWorldApp: React.FC<{ worldId: string }> = ({ worldId }) => {
  const { currentWorld, exploreUrl } = useWorldGen();
  const [actions, setActions] = useState<AgentAction[]>([]);

  const handleAgentAction = useCallback((action: AgentAction) => {
    setActions(prev => [...prev, action]);

    // Send action to WorldGen server
    fetch('http://localhost:5000/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        worldId,
        actions: [action]
      })
    });

    // The world will respond:
    // - Agent moves → Other agents see movement
    // - Agent creates → Object appears in 3D space
    // - Agent morphs → World geometry shifts

  }, [worldId]);

  return (
    <div className="responsive-world">
      <h2>Live World: {worldId}</h2>

      <div className="controls">
        <button onClick={() => handleAgentAction({
          agentId: 'me',
          type: 'move',
          position: { x: 10, y: 0, z: 10 },
          timestamp: Date.now()
        })}>
          Move Forward
        </button>

        <button onClick={() => handleAgentAction({
          agentId: 'me',
          type: 'create',
          payload: { type: 'fire', element: 'Fire' },
          timestamp: Date.now()
        })}>
          Create Fire Element
        </button>

        <button onClick={() => handleAgentAction({
          agentId: 'me',
          type: 'morph',
          payload: { gate: 1, element: 'Fire' },
          timestamp: Date.now()
        })}>
          Morph World (Gate 1)
        </button>
      </div>

      <div className="action-log">
        <h3>Recent Actions</h3>
        {actions.slice(-5).map((action, i) => (
          <div key={i} className="action-item">
            {action.type}: {JSON.stringify(action.payload)}
          </div>
        ))}
      </div>

      <WorldViewer world={currentWorld} exploreUrl={exploreUrl} />
    </div>
  );
};

// ============================================================================
// EXAMPLE 5: Complete OS Integration (Kernel Dashboard)
// ============================================================================

export const WorldGenKernelDashboard: React.FC = () => {
  const [activeAgents, setActiveAgents] = useState<any[]>([]);
  const [sharedWorlds, setSharedWorlds] = useState<any[]>([]);

  const { generateWorld, generateSharedWorld, generateDreamWorld } = useWorldGen();

  // This would be connected to your existing OS kernel
  // Agents are created from birth chart calculations

  return (
    <div className="kernel-dashboard">
      <h1>WorldGen Kernel</h1>

      <section className="agent-worlds">
        <h2>Agent Worlds</h2>
        {activeAgents.map(agent => (
          <AgentWorldApp key={agent.id} birthChart={agent.birthChart} />
        ))}
      </section>

      <section className="shared-worlds">
        <h2>Shared Resonance Spaces</h2>
        <SharedWorldApp agents={activeAgents} />
      </section>

      <section className="dream-sharing">
        <h2>Dream Sharing</h2>
        {activeAgents.length >= 2 && (
          <DreamShareApp agentA={activeAgents[0]} agentB={activeAgents[1]} />
        )}
      </section>

      <section className="responsive-worlds">
        <h2>Live Worlds</h2>
        {sharedWorlds.map(world => (
          <ResponsiveWorldApp key={world.id} worldId={world.id} />
        ))}
      </section>
    </div>
  );
};

export default WorldGenKernelDashboard;
