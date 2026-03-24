---
project: QA
repository: spencerpeyrot/QA
license: Unknown
source_file: prd.md
source_url: https://github.com/spencerpeyrot/QA/blob/8dfd4e8c38baf7f4d0b3d2a57af34d0c1119e3b5/prd.md
downloaded_at: 2025-12-05T10:31:48.178145+00:00
consensus_grade_level: 10.9
headings_per_sentence: 0.29
lists_per_sentence: 0.64
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.07
anaphora_per_sentence: 0.03
sentence_cv: 1.86
cpre_terms_per_sentence: 0.28
---
# QA Platform – Product Requirements Document (PRD)

**Version:** v0.1   **Author:** Spencer Peyrot   **Date:** 22 Apr 2025

---
## 1 Purpose
Build a lean, local‑first web application that lets analysts QA every component of AgentSmyth’s financial‑analysis platform via OpenAI prompts, record the LLM‑generated evaluation, and log a human pass/fail vote for future insight + RLHF.

## 2 Scope (MVP)
* Single‑user, local execution (no auth, no hosting).
* Supports all existing agents & sub‑components listed in the briefing.
* Variable‑aware prompt execution (inputs differ by component).
* UI elements: two‑level dropdown, report textarea, **Run QA** button, markdown result pane, ✅/❌ buttons.
* Persistence to local MongoDB.

## 3 Users & Roles
| Role                  | Description                              |
|-----------------------|------------------------------------------|
| **Analyst (default)** | Runs QA, votes pass/fail.                |
| _Admin_ (future)      | Manage prompt templates, view analytics. |

## 4 Functional Requirements
### 4.1 Component Selector
* Dropdown‑1: **Agent** (S, M, Q, O, E, Ticker Dashboard).
* Dropdown‑2: **Sub‑component** (contextual list; nullable).

### 4.2 Prompt Input Registry

#### 4.2.1 Agent S  
**Variables:**  
- `current_date`  
- `report_text`  

#### 4.2.2 Agent M  
##### 4.2.2.1 Long Term View  
**Variables:**  
- `current_date`  
- `category`  
- `report_text`  

##### 4.2.2.2 Short Term View  
**Variables:**  
- `current_date`  
- `prev_trading_day`  
- `market_recap`  
- `market_thesis`  

##### 4.2.2.3 Sector Level View  
**Variables:**  
- `current_date`  
- `sector_type`  
- `report_text`  

##### 4.2.2.4 Key Gamma Levels  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

#### 4.2.3 Agent Q  
##### 4.2.3.1 Support & Resistance  
**Variables:**  
- `current_date`  
- `ticker`  
- `current_price`  
- `report_text`  

##### 4.2.3.2 Volume Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

##### 4.2.3.3 Candlestick Patterns  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

##### 4.2.3.4 Consolidated Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `current_price`  
- `report_text`  

#### 4.2.4 Agent O  
##### 4.2.4.1 Flow Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `current_price`  
- `report_text`  

##### 4.2.4.2 Volatility Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `current_price`  
- `report_text`  

##### 4.2.4.3 Consolidated Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `current_price`  
- `report_text`  

#### 4.2.5 Agent E  
##### 4.2.5.1 EPS/Revenue Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

##### 4.2.5.2 Forward Guidance  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

##### 4.2.5.3 Quantitative Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

##### 4.2.5.4 Options Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

##### 4.2.5.5 Consolidated Analysis  
**Variables:**  
- `current_date`  
- `ticker`  
- `eps_rev_report`  
- `fg_report`  
- `quant_report`  
- `options_report`  

#### 4.2.6 Ticker Dashboard  
##### 4.2.6.1 Overview  
**Variables:**  
- `ticker`  
- `agent_ratings`  
- `overview_report`  

##### 4.2.6.2 Agent S Snapshot  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  

##### 4.2.6.3 Agent Q Snapshot  
**Variables:**  
- `current_date`  
- `ticker`  
- `current_price`  
- `td_q_report`  
- `q_standalone_report`  

##### 4.2.6.4 Agent O Snapshot  
**Variables:**  
- `current_date`  
- `ticker`  
- `current_price`  
- `td_o_report`  
- `o_standalone_report`  

##### 4.2.6.5 Agent M Snapshot  
**Variables:**  
- `current_date`  
- `ticker`  
- `report_text`  


> **Action:** maintain this table in `/prompts/registry.json`; backend reads it to validate inputs.

### 4.3 QA Execution

**Evaluation dimensions**
1. *QA‑prompt correctness* – Did the LLM accurately detect issues in the report?
2. *Original report accuracy* – Is the underlying component report itself error‑free?

The backend performs the following steps:
1. Backend injects `CURRENT_DATE` (server clock, ISO‑8601).
2. Backend formats selected prompt template with posted vars.
3. Calls OpenAI Chat Completions (stream=True).
4. Streams markdown back to UI.
5. Persists run document.

### 4.4 Human Vote
* Two buttons, green ✅ = pass, red ❌ = fail.
* One click PATCHes `pass` field.

### 4.5 Persistence
See §7 Data Model — note the distinct `qa_pass` and `report_pass` fields that separately track **QA quality** and **original report accuracy**.

### 4.6 API Endpoint Spec (MVP)
| Method | Path | Body / Params | Purpose |
|--------|------|---------------|---------|
| **POST** | `/qa` | `{ agent, sub_component, variables, report_text }` | Create a QA run: server injects `CURRENT_DATE`, formats prompt, calls OpenAI, persists run, returns `{id, markdown}`. |
| **PATCH** | `/qa/{id}/qa_pass` | `{ qa_pass: true \| false }` | Record analyst judgment on **QA prompt correctness**. |
| **PATCH** | `/qa/{id}/report_pass` | `{ report_pass: true \| false }` | Record analyst judgment on **original report accuracy**. |
| **GET** | `/qa/{id}` | – | Fetch a saved run (used for page reloads). |
| **GET** | `/qa?limit=20` | – | (Dev helper) List recent runs. |

*All endpoints return `{status: "ok"}` on success and descriptive JSON error on failure.*
See §7 Data Model — note the distinct `qa_pass` and `report_pass` fields that separately track **QA quality** and **original report accuracy**.

## 5 Non‑Functional Requirements
* **Local‑only**; runs on macOS/Windows with Python 3.12 & Node 18+.
* **Performance:** LLM latency only; UI must not block.
* **Reliability:** Graceful error display on OpenAI / Mongo errors.
* **Extensibility:** Future drop‑in auth & analytics without refactor.

## 6 Tech Stack (MVP)
| Layer | Choice | Rationale |
|-------|--------|-----------|
| Frontend | React + Vite + TypeScript | Fast boot, Cursor‑friendly. |
| UI Kit | shadcn/ui + Tailwind | Minimal CSS hassle. |
| State | React Context (Zustand optional) | Small scope. |
| Backend | FastAPI + uvicorn (reload) | Async, auto docs. |
| DB | MongoDB (local) using `motor` | Schema‑flexible. |
| LLM | OpenAI (gpt‑4o‑mini default) | Consistent with prod agents. |

## 7 Data Model
# MongoDB collection: qa_evaluations
# One document = one QA run for one component report
qa_evaluations:
  _id: ObjectId                # Mongo primary key
  agent: string                # "Agent M", "Agent S", etc.
  sub_component: string|null   # e.g., "Long Term View" or null
  report_text: string          # raw report pasted by analyst
  variables: object            # any extra vars posted by UI
  injected_date: string        # ISO‑8601 (YYYY‑MM‑DD), added server‑side
  openai_model: string         # model used for QA (e.g., "gpt‑4o‑mini")
  response_markdown: string    # LLM QA output (markdown)
  
  # --- HUMAN‑VOTED FIELDS ---
  qa_pass: boolean|null        # ✅/❌ on QA prompt correctness
  report_pass: boolean|null    # 👍/👎 on original report accuracy
  
  created_at: datetime         # inserted automatically

## 8 Prompt Template Storage
* Directory: `/prompts/{agent}/{sub_component}.jinja`
* Use Jinja2 syntax for variable placeholders.
* Registry file (§4.2) validates user input keys.

## 9 Build Progression Map
| # | Task | Sub‑tasks |
|---|------|-----------|
| **Phase 1 – Env Setup** |
| 1a | _Backend scaffold_ | `python -m venv`, install FastAPI, uvicorn, motor, openai |
| 1b | _Frontend scaffold_ | `npm create vite@latest`, add Tailwind & shadcn/ui |
| **Phase 2 – Static UI** |
| 2a | Dropdown components | hard‑code Agent → Sub options |
| 2b | Textarea + char count |
| 2c | Disable **Run** button until required fields present |
| **Phase 3 – Prompt Engine** |
| 3a | Implement `/qa` POST (no OpenAI, returns echo) |
| 3b | Add prompt registry loader |
| 3c | Inject server date; validate missing vars |
| **Phase 4 – OpenAI Integration** |
| 4a | Wire `openai.chat.completions` with streaming |
| 4b | Display streamed markdown in UI |
| 4c | Error + token‑usage logging |
| **Phase 5 – Persistence Layer** |
| 5a | Spin up local Mongo, create `qa_evaluations` collection |
| 5b | Save run document on `/qa` completion |
| 5c | Implement `/qa/{id}/pass` endpoint |
| 5d‑1 | QA Pass/Fail buttons (✅/❌) trigger PATCH → `qa_pass`; disable after vote |
| 5d‑2 | Report accuracy buttons (👍/👎) trigger PATCH → `report_pass`; disable after vote |
| **Phase 6 – Polish & Docs** |
| 6a | Loading spinners & toast errors |
| 6b | README quick‑start + env sample |
| 6c | Code comments for future auth/analytics hooks |

> **Cursor Tip:** reference any sub‑task via `#5d` etc. Commit messages like “feat: 5d – pass/fail endpoint & UI hook”.

## 10 Out‑of‑Scope (MVP)
* Authentication & user roles.
* Analytics dashboard.
* Dockerisation & cloud hosting.
* Prompt‑editing UI.

## 11 Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Prompt variables mis‑match | Registry validation + fast error toast. |
| OpenAI rate‑limits | Local retry w/ exponential back‑off; expose error. |
| Cursor unfamiliarity | Follow numbered tasks; small commits. |

---

## 12 System Architecture

┌──────────────────────┐        ┌────────────────────────────┐
│        React         │  HTTPS │         FastAPI            │
│  (Vite or Next.js)   │──────▶ │  (Python 3.12, uvicorn)    │
└────────┬─────────────┘        └──────────--┬───────────────┘
         │  WebSocket (optional live stream) │
┌────────▼─────────────┐        ┌──────────▼────────────────┐
│   Tailwind / shadcn  │        │   OpenAI SDK (async)      │
│   Zustand / TanStack │        │   Pydantic models         │
└──────────────────────┘        │   Motor (async MongoDB)   │
                                └──────────┬────────────────┘
                                           │
                                ┌──────────▼───────────┐
                                │   MongoDB Atlas      │
                                │  (or local Docker)   │
                                └──────────────────────┘

**End of Document**

