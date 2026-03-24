---
project: selfhost-backend
repository: evergreen-os/selfhost-backend
license: Unknown
source_file: plans/prd_01.md
source_url: https://github.com/evergreen-os/selfhost-backend/blob/60c6759159bf3b663b9c63f4ea6a82c0bb93754d/plans/prd_01.md
downloaded_at: 2025-12-05T10:48:19.632175+00:00
consensus_grade_level: 10.8
headings_per_sentence: 0.18
lists_per_sentence: 0.86
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.06
anaphora_per_sentence: 0.05
sentence_cv: 1.063
cpre_terms_per_sentence: 0.09
---
# EvergreenOS Selfhost Backend – PRD

## 📌 Overview
The `selfhost-backend` repo implements the **EvergreenOS device management backend** for self-hosted and enterprise deployments.  
It consumes contracts from [`shared-specs`](https://github.com/evergreen-os/shared-specs) and exposes:

- **gRPC APIs** for EvergreenOS device agents (enrollment, policy, state, events, attestation).
- **REST/OpenAPI APIs** for admin consoles and integrations.
- **Database + persistence layer** for devices, policies, and logs.
- **Tenant & auth management** for schools, resellers, or districts.

This backend is functionally equivalent to Evergreen Cloud, but deployed by IT admins on their own infrastructure (VM, bare metal, Kubernetes, etc.).

---

## 🎯 Goals

- Provide a **self-contained management server** for EvergreenOS devices.
- Fully compatible with `shared-specs` contracts (proto + OpenAPI + JSON schemas).
- Support **multi-tenant** operation (school → org → device).
- Allow deployment on **Postgres** + container runtimes.
- Make **setup simple** (Docker Compose or Helm chart).
- Include **audit & compliance features** (logs, role-based access).
- Allow **upgrades with zero downtime**.

---

## 🚫 Non-Goals

- No device agent code (that lives in `device-agent` repo).
- No admin UI (that lives in `web-console` repo).
- No proprietary cloud features (e.g., SaaS billing, Clever/ClassLink SSO).

---

## 📂 Repository Layout

selfhost-backend/
├─ README.md
├─ docs/
│ ├─ prd.md
│ ├─ architecture.md
│ └─ deployment.md
├─ cmd/
│ ├─ server/ # Main backend server entrypoint
│ └─ migrate/ # DB migration tool
├─ internal/
│ ├─ api/ # gRPC + REST handlers
│ ├─ db/ # Postgres queries, migrations
│ ├─ auth/ # JWT, LDAP/SSO adapters
│ ├─ policies/ # Policy storage + signing
│ ├─ devices/ # Enrollment, state, events
│ ├─ attestation/ # TPM checks (optional in v1)
│ └─ audit/ # Audit log + metrics
├─ migrations/ # SQL migrations
├─ gen/ # Code generated from shared-specs
├─ config/
│ ├─ config.yaml # Default config
│ └─ secrets.yaml # Secret overrides (gitignored)
├─ Makefile
├─ buf.gen.yaml
├─ docker-compose.yaml
└─ helm/ # Helm chart (optional v2)


---

## 📐 Functional Requirements

### Device Lifecycle
- **EnrollDevice**  
  - Accept enrollment requests, validate `tenant_code` + `enroll_secret`.
  - Issue `device_id` + `device_token`.
- **PullPolicy**  
  - Return latest `PolicyBundle` (signed).
- **ReportState**  
  - Store device state (apps, update, health).
- **ReportEvents**  
  - Persist event logs for troubleshooting.
- **AttestBoot** (optional in v1.1)  
  - Verify TPM quote if available.

### Policy Management
- CRUD for `PolicyBundle` objects.
- Digital signature applied to all policies.
- Enforce **version monotonicity**.

### Tenant & User Management
- Multi-tenant hierarchy:  
  `reseller → org (school/district) → devices`.
- Local admin accounts with RBAC:
  - **Owner**
  - **Admin**
  - **Auditor (read-only)**
- Authentication:
  - v0.1: Local username/password + JWT.  
  - v0.2: LDAP/AD + SSO (optional).

### API Exposure
- gRPC API per `shared-specs` Protos.  
- REST API via `openapi/evergreen.v1.yaml`.  
- Authentication with JWT (Bearer).  
- Admin endpoints protected by RBAC.

### Database
- Postgres schema:
  - `tenants`
  - `users`
  - `devices`
  - `policies`
  - `events`
  - `audit_logs`
- All schema changes via migrations (`migrate` tool).

### Audit & Logging
- Store device events + admin actions.
- Export logs via:
  - Postgres queries
  - Optional syslog or webhook forwarders.
- Metrics via Prometheus endpoints (`/metrics`).

---

## 🛠️ Technical Requirements

- **Language**: Go (1.23+).
- **Frameworks**:
  - gRPC + buf for APIs.
  - Echo/Fiber for REST.
  - sqlc or GORM for DB queries.
- **Persistence**: Postgres 14+.
- **Containerization**: Docker, Docker Compose.
- **Secrets**: Env vars or mounted secrets.
- **Codegen**: `make gen` pulls from `shared-specs`.

---

## 🔐 Security Requirements

- All traffic HTTPS only.
- JWT auth with 1-hour expiry, refresh via API.
- Device tokens scoped to device ID.
- Policies signed with Ed25519 keys.
- Admin actions written to immutable audit log.
- Config option for FIPS crypto mode.

---

## 📊 Success Metrics

- Device agent can:
  - Enroll successfully.
  - Pull and apply a policy.
  - Report state + events with <200ms latency.
- Admin can:
  - Create/update policies.
  - View enrolled devices.
  - Audit logs for any action.
- Deployment:
  - Start via `docker-compose up` in <5 min.
  - Helm chart available for K8s (v0.2+).

---

## 🚀 Roadmap

### v0.1 (MVP)
- Enrollment, PullPolicy, ReportState, ReportEvents.
- Local admin accounts + JWT auth.
- Postgres persistence.
- Docker Compose deployment.

### v0.2
- RBAC (Owner/Admin/Auditor).
- Policy signing.
- LDAP/AD auth support.
- Basic Helm chart.

### v1.0
- Attestation.
- Webhook log forwarder.
- Backup/restore tooling.
- Compliance reports (CSV/JSON export).

---

## 📝 Open Questions

- Should we support **multi-org federation** (shared resellers across multiple backends)?  
- Should policy signing keys be **per-tenant** or **global**?  
- How do we handle **device de-registration** securely?  
- Do we need **delta policies** (diffs) or just full replacement?  

---

## 📖 References

- [shared-specs repo](https://github.com/evergreen-os/shared-specs)  
- [Buf](https://buf.build/) for gRPC/proto codegen  
- [sqlc](https://sqlc.dev/) or [GORM](https://gorm.io/) for DB queries  
- [Prometheus metrics](https://prometheus.io/)  

---
