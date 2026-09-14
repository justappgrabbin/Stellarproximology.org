import { useMemo, useState } from 'react';
import {
  Activity,
  ArrowRight,
  Atom,
  Beaker,
  Binary,
  BookOpen,
  Brain,
  ChevronRight,
  CircleDot,
  Cpu,
  Database,
  Download,
  FileText,
  FlaskConical,
  Globe2,
  HeartPulse,
  Network,
  Orbit,
  RefreshCw,
  ShieldCheck,
  Sparkles,
  Users,
} from 'lucide-react';
import './App.css';

type View = 'home' | 'lab' | 'studies' | 'reports' | 'ecosystem';

type Study = {
  id: string;
  title: string;
  short: string;
  status: 'active' | 'analysis' | 'protocol' | 'development';
  icon: React.ComponentType<{ size?: number; strokeWidth?: number }>;
  question: string;
  measures: string[];
  outputs: string[];
  evidence: string;
  downloads: string[];
};

const studies: Study[] = [
  {
    id: 'human-design',
    title: 'Human Design & Genetic Resonance',
    short: 'Chart coordinates, gates, codons, state mapping and lived outcomes.',
    status: 'active',
    icon: CircleDot,
    question: 'Do structured Human Design-derived state hypotheses predict or improve reported lived outcomes when tested longitudinally?',
    measures: ['Gate / line / color / tone / base', 'Participant self-report', 'State transitions', 'Outcome follow-up'],
    outputs: ['Chart report', 'State comparison', 'Longitudinal summary'],
    evidence: 'Protocol and calculation infrastructure present; participant evidence belongs in the study ledger.',
    downloads: ['Participant chart report', 'Research protocol', 'Dataset export'],
  },
  {
    id: 'mrnn',
    title: 'MRNN State-Space Research',
    short: 'Multi-layer relational neural network, inference, addressability and emergence.',
    status: 'analysis',
    icon: Network,
    question: 'Can a finite relational state system produce coherent higher-order patterns while preserving provenance across scales?',
    measures: ['Node activation', 'Cross-layer coherence', 'Transition traces', 'Inference confidence'],
    outputs: ['Matrix visualizations', 'Inference report', 'Emergence trace'],
    evidence: 'Repository contains MRNN matrix data, inference engines, visualizers and autonomous orchestration code.',
    downloads: ['MRNN research brief', 'Matrix sample', 'Architecture package'],
  },
  {
    id: 'pure-synthia',
    title: 'Pure Synthia / Recursive Intelligence',
    short: 'Finite primitives, relational operators and recursive computational structure.',
    status: 'active',
    icon: Brain,
    question: 'How much semantic and computational structure can emerge from a small set of primitives plus explicit relational operators?',
    measures: ['Primitive promotion', 'Cross-scale composition', 'Novel structure', 'Replay consistency'],
    outputs: ['Execution trace', 'Behavior report', 'Synthia integration package'],
    evidence: 'The research target is falsifiable at the level of generated structures, execution traces and repeatability.',
    downloads: ['Synthia research build', 'Primitive specification', 'Run report'],
  },
  {
    id: 'photonic',
    title: 'Photonic & Optoacoustic Models',
    short: 'Experimental computational models for light, signal and neural analogies.',
    status: 'development',
    icon: Atom,
    question: 'Which signal-processing or photonic analogies remain computationally useful once separated from metaphorical claims?',
    measures: ['Signal response', 'Model stability', 'Transfer performance', 'Failure conditions'],
    outputs: ['Model comparison', 'Simulation report', 'Architecture notes'],
    evidence: 'Photonic, phononic and optoacoustic engine materials are present in the repository and require empirical separation by claim type.',
    downloads: ['Photonic model notes', 'Simulation package', 'Evidence worksheet'],
  },
  {
    id: 'adaptive-coupling',
    title: 'Adaptive Coupling & Computer Assignment',
    short: 'When assistance strengthens capability versus hiding dependency.',
    status: 'protocol',
    icon: Cpu,
    question: 'Does adaptive assistance improve independent capability, successful transitions and access to tools over time?',
    measures: ['Task completion', 'Dependency change', 'Access barriers', 'Independent retry success'],
    outputs: ['Needs assessment', 'Assignment rationale', 'Outcome report'],
    evidence: 'The current phase is instrumentation and protocol definition; deployment links can be added without redesigning the study page.',
    downloads: ['Computer request', 'Cynthia install', 'Study protocol'],
  },
  {
    id: 'resonance-network',
    title: 'Resonance Network Social Experiments',
    short: 'Consent-first connection, collaboration, opportunity and real-world outcomes.',
    status: 'protocol',
    icon: Users,
    question: 'Do state- and need-aware introductions produce more useful collaboration than attention-based social matching?',
    measures: ['Mutual acceptance', 'Connection usefulness', 'Collaboration outcome', 'Economic / non-economic value'],
    outputs: ['Connection report', 'Outcome ledger', 'Aggregate findings'],
    evidence: 'The study design emphasizes consent, attribution and participant choice rather than engagement as success.',
    downloads: ['Participant consent', 'Study brief', 'Aggregate report'],
  },
  {
    id: 'pathways',
    title: 'Pathways to Purpose',
    short: 'Self-knowledge, complementary roles, participation and economic agency.',
    status: 'protocol',
    icon: HeartPulse,
    question: 'When people understand their role and receive the right opportunity plus practical support, do desired outcomes improve?',
    measures: ['Role clarity', 'Participation', 'Barrier removal', 'Goal progress'],
    outputs: ['Journey report', 'Outcome comparison', 'Program findings'],
    evidence: 'This research can connect directly to the regenerative-value model while keeping scientific and enterprise outcomes distinct.',
    downloads: ['Journey guide', 'Participant report', 'Program findings'],
  },
];

const statusLabel: Record<Study['status'], string> = {
  active: 'Active Study',
  analysis: 'Analysis',
  protocol: 'Protocol Ready',
  development: 'Model Development',
};

function App() {
  const [view, setView] = useState<View>('home');
  const [selectedStudy, setSelectedStudy] = useState<Study | null>(null);

  const activeCount = studies.filter((s) => s.status === 'active' || s.status === 'analysis').length;

  const reportText = useMemo(() => {
    const stamp = new Date().toISOString().slice(0, 10);
    return [
      'STELLAR PROXIMOLOGY — LAB STATUS REPORT',
      `Generated: ${stamp}`,
      '',
      'Purpose',
      'Stellar Proximology is an experiential research & development laboratory. Findings are reported by evidence state; hypotheses are not presented as established facts.',
      '',
      ...studies.flatMap((s) => [
        s.title,
        `Status: ${statusLabel[s.status]}`,
        `Research question: ${s.question}`,
        `Current evidence note: ${s.evidence}`,
        `Measures: ${s.measures.join('; ')}`,
        `Outputs: ${s.outputs.join('; ')}`,
        '',
      ]),
      'Evidence loop',
      'Observation → Question → Hypothesis → Model → Experiment → Evidence → Revision → Proposal',
    ].join('\n');
  }, []);

  const downloadLabReport = () => {
    const blob = new Blob([reportText], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'stellar-proximology-lab-report.txt';
    a.click();
    URL.revokeObjectURL(url);
  };

  const navigate = (next: View) => {
    setSelectedStudy(null);
    setView(next);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="stellar-shell">
      <div className="space-noise" />
      <header className="topbar">
        <button className="brand" onClick={() => navigate('home')}>
          <span className="brand-orbit"><Orbit size={21} /></span>
          <span>
            <strong>STELLAR PROXIMOLOGY</strong>
            <small>Experiential R&D Laboratory</small>
          </span>
        </button>
        <nav className="nav-links">
          <button className={view === 'lab' ? 'active' : ''} onClick={() => navigate('lab')}>Lab</button>
          <button className={view === 'studies' ? 'active' : ''} onClick={() => navigate('studies')}>Studies</button>
          <button className={view === 'reports' ? 'active' : ''} onClick={() => navigate('reports')}>Reports</button>
          <button className={view === 'ecosystem' ? 'active' : ''} onClick={() => navigate('ecosystem')}>Ecosystem</button>
        </nav>
        <div className="runtime-pill"><span /> AUTONOMOUS LAB</div>
      </header>

      {view === 'home' && (
        <main>
          <section className="hero-grid page-width">
            <div className="hero-copy">
              <p className="eyebrow">CURIOSITY BUILDS BRIGHTER WORLDS</p>
              <h1>Science for the <span>space between.</span></h1>
              <p className="hero-lead">Stellar Proximology studies state, relationship, perspective, transformation, resonance, intelligence and human outcomes across scales.</p>
              <div className="hero-actions">
                <button className="primary" onClick={() => navigate('lab')}><FlaskConical size={17} /> Enter the Lab</button>
                <button className="secondary" onClick={() => navigate('studies')}>Explore Studies <ArrowRight size={16} /></button>
              </div>
              <div className="truth-strip">
                <ShieldCheck size={17} />
                <span>Hypotheses stay hypotheses. Evidence changes the model.</span>
              </div>
            </div>
            <div className="planet-stage" aria-hidden="true">
              <div className="planet-orbit orbit-one"><i /></div>
              <div className="planet-orbit orbit-two"><i /></div>
              <div className="planet"><div className="planet-land" /></div>
              <div className="star star-a">✦</div><div className="star star-b">✦</div><div className="star star-c">✧</div>
            </div>
          </section>

          <section className="dashboard page-width">
            <div className="section-heading compact">
              <div><p className="eyebrow">LIVE LAB OVERVIEW</p><h2>Research in motion.</h2></div>
              <button className="text-link" onClick={downloadLabReport}><Download size={15} /> Download lab report</button>
            </div>
            <div className="metric-grid">
              <article><span>Research programs</span><strong>{studies.length}</strong><small>Across human, computational & social systems</small></article>
              <article><span>In active analysis</span><strong>{activeCount}</strong><small>Evidence surfaces remain explicitly labeled</small></article>
              <article><span>Autonomous cycle</span><strong className="live-word">ONLINE</strong><small>Observe → test → compare → revise</small></article>
              <article><span>Public reports</span><strong>READY</strong><small>Study summaries + reserved downloads</small></article>
            </div>

            <div className="home-layout">
              <div className="lab-console glass-card">
                <div className="card-top"><span><Activity size={17} /> Autonomous Research Cycle</span><span className="live-dot">LIVE</span></div>
                <div className="cycle-row">
                  {['Observe', 'Question', 'Hypothesis', 'Model', 'Experiment', 'Evidence', 'Revise', 'Propose'].map((step, idx) => (
                    <div className="cycle-step" key={step}><b>{String(idx + 1).padStart(2, '0')}</b><span>{step}</span></div>
                  ))}
                </div>
                <div className="console-log">
                  <div><span>06:01</span><p>Evidence ledger ready for participant and system observations.</p></div>
                  <div><span>06:04</span><p>Study reports expose current claim state instead of flattening results into certainty.</p></div>
                  <div><span>06:08</span><p>Download bays reserved for Cynthia, computer assignment, datasets and protocols.</p></div>
                </div>
              </div>

              <div className="featured-stack">
                <button className="feature-card" onClick={() => navigate('studies')}>
                  <div className="feature-icon"><Beaker size={23} /></div>
                  <div><small>RESEARCH</small><h3>Studies</h3><p>Every study, question, measure, evidence state and download surface in one place.</p></div>
                  <ChevronRight size={20} />
                </button>
                <button className="feature-card" onClick={() => navigate('reports')}>
                  <div className="feature-icon"><FileText size={23} /></div>
                  <div><small>EVIDENCE</small><h3>Reports</h3><p>What the studies have done, what was observed, and what remains unproven.</p></div>
                  <ChevronRight size={20} />
                </button>
                <button className="feature-card" onClick={() => navigate('ecosystem')}>
                  <div className="feature-icon"><Globe2 size={23} /></div>
                  <div><small>APPLICATION</small><h3>Ecosystem</h3><p>Where findings meet Synthia, Resonance, Pathways and YOU-N-I-VERSE.</p></div>
                  <ChevronRight size={20} />
                </button>
              </div>
            </div>
          </section>

          <section className="study-preview page-width">
            <div className="section-heading compact"><div><p className="eyebrow">CURRENT STUDIES</p><h2>One lab. Different questions.</h2></div><button className="text-link" onClick={() => navigate('studies')}>View all <ArrowRight size={15} /></button></div>
            <div className="preview-grid">
              {studies.slice(0, 4).map((study) => <StudyMini key={study.id} study={study} onOpen={() => { setSelectedStudy(study); setView('studies'); }} />)}
            </div>
          </section>
        </main>
      )}

      {view === 'lab' && <LabPage onReport={downloadLabReport} onStudies={() => navigate('studies')} />}
      {view === 'studies' && <StudiesPage selected={selectedStudy} onSelect={setSelectedStudy} />}
      {view === 'reports' && <ReportsPage reportText={reportText} onDownload={downloadLabReport} />}
      {view === 'ecosystem' && <EcosystemPage />}

      <footer className="footer page-width">
        <div><strong>STELLAR PROXIMOLOGY</strong><span>Observation → evidence → revision.</span></div>
        <span>Science belongs to everyone.</span>
      </footer>
    </div>
  );
}

function StudyMini({ study, onOpen }: { study: Study; onOpen: () => void }) {
  const Icon = study.icon;
  return <button className="study-mini" onClick={onOpen}><div className="study-mini-top"><Icon size={22} /><span className={`status ${study.status}`}>{statusLabel[study.status]}</span></div><h3>{study.title}</h3><p>{study.short}</p><span className="open-row">Open study <ArrowRight size={14} /></span></button>;
}

function LabPage({ onReport, onStudies }: { onReport: () => void; onStudies: () => void }) {
  return <main className="inner-page page-width">
    <PageIntro eyebrow="AUTONOMOUS LAB" title="A research system that keeps the evidence visible." body="Stellar is designed around a recursive research cycle: observe, form a testable question, model it, run the experiment, preserve the evidence, compare prediction with observation, revise, and report." />
    <div className="lab-grid">
      <section className="glass-card lab-panel wide"><div className="card-top"><span><RefreshCw size={17}/> Research loop</span><span className="live-dot">RUNNING</span></div><div className="big-cycle">{['Observation','Question','Hypothesis','Model','Experiment','Evidence','Revision','Proposal'].map((x,i)=><div key={x}><b>{i+1}</b><span>{x}</span>{i<7&&<ArrowRight size={15}/>}</div>)}</div></section>
      <section className="glass-card lab-panel"><div className="card-top"><span><Database size={17}/> Evidence ledger</span></div><h3>Nothing disappears into a conclusion.</h3><p>Each study keeps its question, measures, evidence state, output and revision path separate.</p><ul><li>Proposed</li><li>Predicted</li><li>Observed</li><li>Replicated</li><li>Generalized</li></ul></section>
      <section className="glass-card lab-panel"><div className="card-top"><span><Binary size={17}/> Machine research</span></div><h3>Computational studies live beside human studies.</h3><p>MRNN, recursive intelligence, symbolic address systems, photonic models and other engines can publish their traces into the same reporting surface.</p></section>
      <section className="glass-card lab-panel"><div className="card-top"><span><Users size={17}/> Human research</span></div><h3>Consent and lived reality stay in the loop.</h3><p>Participant state, action, outcomes and follow-up can be compared without pretending a hypothesis became fact because it felt compelling.</p></section>
      <section className="glass-card lab-panel wide action-panel"><div><p className="eyebrow">PUBLIC OUTPUT</p><h3>The lab should tell people what it learned.</h3><p>Reports are a first-class surface, not an afterthought. The current build can already export the assembled lab status summary.</p></div><div className="hero-actions"><button className="primary" onClick={onReport}><Download size={16}/> Download report</button><button className="secondary" onClick={onStudies}>Browse studies</button></div></section>
    </div>
  </main>;
}

function StudiesPage({ selected, onSelect }: { selected: Study | null; onSelect: (s: Study | null) => void }) {
  if (selected) {
    const Icon = selected.icon;
    return <main className="inner-page page-width"><button className="back-link" onClick={() => onSelect(null)}>← All studies</button><div className="study-detail-head"><div className="detail-icon"><Icon size={30}/></div><div><span className={`status ${selected.status}`}>{statusLabel[selected.status]}</span><h1>{selected.title}</h1><p>{selected.short}</p></div></div><div className="detail-grid"><section className="glass-card detail-card wide"><p className="eyebrow">RESEARCH QUESTION</p><h2>{selected.question}</h2></section><section className="glass-card detail-card"><p className="eyebrow">WHAT WE MEASURE</p>{selected.measures.map(x=><div className="list-row" key={x}><span/> {x}</div>)}</section><section className="glass-card detail-card"><p className="eyebrow">OUTPUTS</p>{selected.outputs.map(x=><div className="list-row" key={x}><span/> {x}</div>)}</section><section className="glass-card detail-card wide"><p className="eyebrow">CURRENT EVIDENCE NOTE</p><p className="large-copy">{selected.evidence}</p></section><section className="glass-card detail-card wide"><div className="section-heading compact"><div><p className="eyebrow">DOWNLOADS & DEPLOYMENTS</p><h3>Reserved delivery bays</h3></div><small className="muted">Links can be connected later without changing this page.</small></div><div className="download-grid">{selected.downloads.map((x,i)=><button className="download-tile" key={x}><Download size={18}/><span>{x}</span><small>{i===0 && selected.id==='adaptive-coupling' ? 'Cynthia / computer delivery slot' : 'Reserved download slot'}</small></button>)}</div></section></div></main>;
  }
  return <main className="inner-page page-width"><PageIntro eyebrow="RESEARCH PORTFOLIO" title="Every study gets its own evidence trail." body="This page is the public map of what Stellar Proximology is studying. Each card opens the research question, measures, current evidence note, outputs, and space for the related downloads or deployments." /><div className="study-list-grid">{studies.map(s=><StudyMini key={s.id} study={s} onOpen={()=>onSelect(s)}/>)}</div></main>;
}

function ReportsPage({ reportText, onDownload }: { reportText: string; onDownload: () => void }) {
  return <main className="inner-page page-width"><PageIntro eyebrow="REPORTS & FINDINGS" title="What have the studies actually done?" body="This is the public reporting surface. It separates the research question, current evidence state, observations and unresolved questions so the lab can report progress without overstating certainty." /><div className="report-layout"><section className="glass-card report-main"><div className="card-top"><span><BookOpen size={17}/> Current Lab Status Report</span><button className="text-link" onClick={onDownload}><Download size={15}/> Export</button></div><pre>{reportText}</pre></section><aside className="report-side"><div className="glass-card"><p className="eyebrow">REPORT TYPES</p><div className="report-type">Study summary <span>Ready</span></div><div className="report-type">Aggregate findings <span>Surface ready</span></div><div className="report-type">Participant report <span>Reserved</span></div><div className="report-type">Machine run report <span>Reserved</span></div></div><div className="glass-card"><p className="eyebrow">EVIDENCE RULE</p><p>A compelling internal result is not automatically established science. Reports should show exactly where a claim sits.</p></div></aside></div></main>;
}

function EcosystemPage() {
  const items = [
    ['Stellar Proximology', 'Research, testing, evidence and proposals.', FlaskConical],
    ['Resonance Network', 'Public/social environment for connection, studies and collaboration.', Network],
    ['YOU-N-I-VERSE', 'Persistent computational environment where systems and worlds can live.', Globe2],
    ['Synthia', 'Distributed intelligence that can instrument, assist, execute and learn.', Sparkles],
    ['Pathways to Purpose', 'Human participation, role discovery, opportunity and outcome testing.', HeartPulse],
  ] as const;
  return <main className="inner-page page-width"><PageIntro eyebrow="ECOSYSTEM" title="The lab does not end at the lab." body="Stellar investigates. The rest of the ecosystem is where research can become participation, tools, environments, opportunities and new evidence returning to the lab." /><div className="ecosystem-map">{items.map(([name,desc,Icon],i)=><div className="eco-node" key={name}><div className="eco-icon"><Icon size={22}/></div><div><small>{String(i+1).padStart(2,'0')}</small><h3>{name}</h3><p>{desc}</p></div>{i<items.length-1&&<ArrowRight className="eco-arrow" size={18}/>}</div>)}</div><section className="glass-card ecosystem-downloads"><div><p className="eyebrow">DELIVERY & DOWNLOADS</p><h2>Room is already reserved for the things people can actually take with them.</h2><p>Cynthia builds, computer-assignment packages, research datasets, protocols, participant reports, apps and study materials can be wired to these surfaces later.</p></div><div className="download-grid"><button className="download-tile"><Sparkles size={18}/><span>Cynthia</span><small>Install / research build slot</small></button><button className="download-tile"><Cpu size={18}/><span>Computer Assignment</span><small>Request / delivery slot</small></button><button className="download-tile"><Database size={18}/><span>Research Data</span><small>Dataset export slot</small></button><button className="download-tile"><FileText size={18}/><span>Protocols & Reports</span><small>Document library slot</small></button></div></section></main>;
}

function PageIntro({ eyebrow, title, body }: { eyebrow: string; title: string; body: string }) {
  return <section className="page-intro"><p className="eyebrow">{eyebrow}</p><h1>{title}</h1><p>{body}</p></section>;
}

export default App;
