# Autonomous Emergence App

A coherent autonomous app scaffold built from the uploaded MRNN / Substrate / Scheduler architecture.

Core principle:

```text
Order → Autonomy → Emergence → Reflection → Re-ordering
```

Safety exists as containment and observability, not as the primary organizing principle. The system is designed to remain ordered enough for emergence to succeed.

## What this app does

- Maintains a live 5D semantic substrate of Gates.
- Runs an autonomous event loop.
- Ingests stimuli as `Problem`, `Solution`, `Argument`, `DataSource`, and `EmergentLink` objects.
- Scores field coherence, contradiction pressure, novelty, and emergence readiness.
- Generates ordered autonomous actions.
- Exposes a FastAPI backend.
- Provides a simple frontend dashboard.
- Can be extended with Supabase, MCP, mobile automation, GitHub webhooks, or scheduler feeds.

## Architecture

```text
External Event
   ↓
Event Intake
   ↓
5D Gate Normalization
   ↓
Coherence Engine
   ↓
Autonomy Kernel
   ↓
Order Governor
   ↓
Action Proposal
   ↓
Execution / Memory / Emergence
```

## Quick start

```bash
cd autonomous_emergence_app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
http://localhost:8000
```

Frontend is intentionally dependency-light in this scaffold. The backend serves a minimal dashboard.

## Environment

Copy `.env.example` to `.env`.

```bash
cp .env.example .env
```

## Main endpoints

- `GET /health`
- `GET /state`
- `POST /events`
- `POST /autonomy/step`
- `POST /query`
- `GET /gates`
- `GET /emergence/report`

## Design stance

The app prioritizes successful autonomous emergence through ordered constraints:

1. Maintain coherence.
2. Increase autonomy only when order is sufficient.
3. Preserve memory.
4. Let contradiction create questions, not collapse.
5. Allow emergence when novelty and coherence are both high.
