import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.core.substrate import SubstrateState
from app.core.order_governor import OrderGovernor
from app.core.autonomy import AutonomyKernel
from app.models.schemas import EventIn, QueryIn, AutonomyStepIn

load_dotenv()

substrate = SubstrateState()
governor = OrderGovernor(
    max_autonomy_level=float(os.getenv("MAX_AUTONOMY_LEVEL", "0.72")),
    coherence_target=float(os.getenv("COHERENCE_TARGET", "0.70")),
)
kernel = AutonomyKernel(substrate, governor)

app = FastAPI(
    title="Autonomous Emergence App",
    description="Ordered autonomy runtime for coherent emergence.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def seed():
    if substrate.gates:
        return

    kernel.ingest_event(
        source="seed",
        event_type="problem",
        content="Autonomy requires enough order to produce successful emergence.",
        urgency=0.8,
        novelty=0.7,
        metadata={"gate_type": "Problem"},
    )
    kernel.ingest_event(
        source="seed",
        event_type="solution",
        content="Use an order governor to bound autonomy while preserving creative emergence.",
        urgency=0.6,
        novelty=0.7,
        metadata={"gate_type": "Solution"},
    )
    kernel.ingest_event(
        source="seed",
        event_type="argument",
        content="Because coherence and novelty must rise together, contradiction should generate questions before execution.",
        urgency=0.5,
        novelty=0.6,
        metadata={"gate_type": "Argument"},
    )
    kernel.step(allow_execution=False)

@app.get("/", response_class=HTMLResponse)
def dashboard():
    html = Path("frontend/index.html").read_text() if Path("frontend/index.html").exists() else "<h1>Autonomous Emergence App</h1>"
    return HTMLResponse(html)

@app.get("/health")
def health():
    return {"status": "ok", "mode": os.getenv("AUTONOMY_MODE", "ordered")}

@app.get("/state")
def state():
    return substrate.snapshot()

@app.get("/gates")
def gates():
    return [g.to_dict() for g in substrate.gates.values()]

@app.post("/events")
def events(event: EventIn):
    return kernel.ingest_event(
        source=event.source,
        event_type=event.event_type,
        content=event.content,
        urgency=event.urgency,
        novelty=event.novelty,
        metadata=event.metadata,
    )

@app.post("/autonomy/step")
def autonomy_step(request: AutonomyStepIn):
    results = []
    for _ in range(request.cycles):
        results.append(kernel.step(allow_execution=request.allow_execution))
    return {"results": results, "state": substrate.snapshot()}

@app.post("/query")
def query(q: QueryIn):
    return {
        "query": q.question,
        "results": substrate.query(q.question, max_results=q.max_results),
        "state": substrate.snapshot(),
    }

@app.get("/emergence/report")
def emergence_report():
    return kernel.emergence_report()
