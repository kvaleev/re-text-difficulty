---
project: a11y-mcp
repository: CalvHobbes/a11y-mcp
license: Apache License 2.0
source_file: a11y mcp server-prd.md
source_url: https://github.com/CalvHobbes/a11y-mcp/blob/273f8a07db5ad9257271e86cec0a60903581154d/a11y%20mcp%20server-prd.md
downloaded_at: 2025-12-05T10:35:27.498112+00:00
consensus_grade_level: 12.9
headings_per_sentence: 0.19
lists_per_sentence: 0.89
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.15
anaphora_per_sentence: 0.02
sentence_cv: 0.655
cpre_terms_per_sentence: 0.39
---
# MCP Accessibility & Navigation Server PRD

### TL;DR

A Playwright-based MCP server purpose-built for LLMs. Enables automated
navigation to URLs (headless or visual mode), on-demand accessibility
reports via axe-core, full-page HTML retrieval, and extraction of all
navigable URLs (with domain filtering). Exposes all Playwright MCP
commands to the LLM for robust browser automation and web accessibility
improvement. Designed for use in CI and local dev environments—fully
programmable, no human UI.

------------------------------------------------------------------------

## Goals

### Business Goals

- Accelerate accessibility testing and remediation pipelines through
  LLM-driven automation.

- Reduce developer manual QA workload by enabling LLMs to detect and
  suggest fixes for a11y issues.

- Increase CI pipeline compliance and catch more web accessibility
  failures pre-release.

- Promote higher accessibility standards with minimal human oversight.

- Enable rapid, scalable web analysis and site upgrades powered by LLMs.

### User Goals

- Provide a unified, programmable interface for LLMs to control browsers
  and automate web page interactions.

- Enable LLMs to generate detailed axe-core accessibility reports with
  WCAG references.

- Allow LLMs to extract all navigable URLs from any page, with optional
  same-origin filter for bounded exploration.

- Supply full HTML (and optionally CSS/JS) to LLMs for advanced code
  analysis and automated fixing.

- Support chainable, scriptable commands to facilitate complex,
  multi-step web automation without manual intervention.

### Non-Goals

- No graphical user interface or dashboard; strictly API/command-based
  for LLM integration.

- No functionality for manual input or expert review of accessibility
  issues—automation only.

- No persistent browser/user sessions or long-running authentication
  states; stateless command handling.

------------------------------------------------------------------------

## User Stories

All stories are from the viewpoint of an LLM agent:

- As an LLM, I want to navigate to a URL in headless or visual mode so I
  can access live web pages for analysis.

- As an LLM, I want to generate an accessibility (a11y) report with
  axe-core so I can identify issues programmatically.

- As an LLM, I want a list of all navigable URLs (same-origin filter
  optional) so I can plan multi-page analyses.

- As an LLM, I want to retrieve full HTML and a11y results together so I
  can generate or propose code changes on the fly.

- As an LLM, I want to invoke any Playwright MCP command so I can
  perform advanced browser automation.

------------------------------------------------------------------------

## Functional Requirements

- **Navigation & Browser Control** (Priority: High)

  - Endpoint to open/navigate browser to supplied URL; choose headless
    or visual mode.

  - Support interaction commands (click, type, scroll, etc.) as per
    Playwright MCP protocol.

  - Endpoint to close/reset browser context on demand.

- **A11y Reporting** (Priority: High)

  - Endpoint to run axe-core accessibility scan on the current page.

  - Return JSON-formatted accessibility issues: CSS selectors, problem
    descriptions, and WCAG references for each issue.

- **Link Extraction** (Priority: Medium)

  - Endpoint to extract all anchor and navigable links from the rendered
    page.

  - Option to return only same-origin URLs.

  - Output: Array of URLs, link texts, and locations.

- **Code Fetch** (Priority: High)

  - Endpoint to return the raw HTML of the current page.

  - Option to include CSS/JS blobs if needed for repair workflows.

- **Playwright Surface** (Priority: High)

  - Pass-through for all other Playwright MCP commands, callable
    directly by LLM.

  - Return all outputs in machine-readable, consistent JSON.

- **Statelessness** (Priority: High)

  - Every API call is atomic; no requirement for persistent sessions.

  - Optionally, support ephemeral tokens for LLM command chains.

------------------------------------------------------------------------

## User Experience

**Entry Point & First-Time User Experience**

- Only accessible to LLM agents via API with clear, authenticated
  command surface.

- No onboarding or human tutorial; API documentation sufficient for LLM
  integration.

- LLM issues a direct command to the server with required parameters.

**Core Experience**

- **Step 1:** LLM issues 'navigate' command with URL and mode
  (headless/visual).

  - Server confirms navigation, returns status.

  - Handles errors (unreachable URL, invalid domain), and returns clear
    error codes.

- **Step 2:** LLM invokes 'a11y_report' command on the current session.

  - Server returns a structured JSON list of a11y violations, selectors,
    and WCAG rule refs.

- **Step 3:** LLM issues 'get_links' for navigable URLs with optional
  same-origin filter.

  - Returns array of URLs and metadata (location, link text, target
    attributes).

- **Step 4:** LLM issues 'fetch_html' to pull full page HTML (and
  optionally CSS).

  - Returns HTML blob and page metadata in JSON.

- **Step 5:** LLM chains browser commands (e.g., clicks, navigation
  steps) as needed.

  - All commands are stateless; responses include all required page
    state and context.

**Advanced Features & Edge Cases**

- Link extraction must handle JavaScript-injected/SPA navigation, not
  just static anchors.

- Graceful error responses for navigation failures, script execution
  errors, or unsupported Playwright commands.

- Output truncation or pagination for extremely large HTML or link
  lists.

**UI/UX Highlights**

- All endpoints return JSON with clear schema and error reporting.

- Emphasis on accessibility of programmatic interface (robust error
  codes, self-describing outputs).

- All API calls include request/response timing and resource usage for
  LLM workflow optimization.

------------------------------------------------------------------------

## Narrative

A language model agent—integrated into a CI pipeline—receives an
assignment: check and remediate web accessibility issues before the
team’s next deployment. With the MCP Accessibility & Navigation Server,
the LLM launches a headless browser, navigates to the target site, and
commands the server to run an axe-core scan. Instantly, it’s provided
with a detailed report: every WCAG violation, the precise HTML selector,
and human-readable summaries.

The model requests a dump of the page’s HTML, correlates the violations,
and drafts improved code for each issue. Next, it asks for a list of all
same-origin navigable URLs and plans a crawl to ensure coverage. At each
step, the agent directs browser actions and records the state—all
through stateless, atomic API calls.

Deployed in CI, this closed-loop approach catches more accessibility
flaws, delivers actionable reports, and accelerates web compliance.
Developers review clean fix suggestions rather than combing through
vague scan results. The business ships more inclusive websites, faster.
Everyone wins—especially the users who need accessible experiences.

------------------------------------------------------------------------

## Success Metrics

- **Number of LLM-automated a11y audits and remediations per release
  cycle:** Measures how much work shifts from developers to LLM
  automation.

- **Median response time for navigation + a11y reporting pair:** Ensures
  API speed is compatible with CI/CD.

- **% reduction in unresolved accessibility issues (pre/post
  integration):** Tracks effectiveness of LLM-powered remediation.

- **Adoption:** Tracked by number of LLM/scripted API calls over time.

- **Report recall/precision:** Compares MCP a11y report results with
  manual audits for quality/coverage.

- **API stability:** Monitors error-free operation across chained LLM
  workflows.

### User-Centric Metrics

- Workflow cycle time reduction for a11y fixes (CI minutes/hours saved).

- Number of unique URLs/a11y issues addressed by LLM each release.

### Business Metrics

- Decrease in manual QA resource hours spent on accessibility.

- Improved site accessibility scores (e.g., Lighthouse, third-party
  audits).

### Technical Metrics

- Average/95th percentile API response times.

- Uptime/availability (in CI and local environments).

- Error rate on chained browser commands.

### Tracking Plan

- Event: 'navigate-command' executed

- Event: 'a11y-report' completed with result

- Event: 'get-links' command result size

- Metric: API call error/exception rate

- Metric: Average command response time

- Event: HTML/code fetch request

------------------------------------------------------------------------

## Technical Considerations

### Technical Needs

- Modular API server, each endpoint maps to a Playwright action or a11y
  result.

- Fast, stream-capable response pipeline with clear error handling per
  command.

- Tight axe-core integration for a11y scans on arbitrary DOMs.

- Secure, local or CI-only deployment; API key/token authentication as
  needed.

- Resource cleanup post-command: close browser/page when necessary.

### Integration Points

- Existing Playwright MCP protocol support.

- Axe-core library integration.

- Compatibility with any LLM interface capable of making structured API
  calls.

### Data Storage & Privacy

- No persistent storage of HTML, a11y reports, or navigation state.

- Optional ephemeral context for LLM-chained commands (short-lived
  session tokens).

- Data processed in secure, local/CI environment only.

- Full compliance with internal data-handling standards; no user PII is
  collected.

### Scalability & Performance

- Optimized for dozens of sequential LLM calls per minute (not public
  scale).

- Minimal memory/CPU footprint per command; browser teardown after use.

### Potential Challenges

- Handling edge-case navigation failures (dynamic content, heavy JS
  sites).

- Ensuring Playwright version parity with supported MCP commands.

- Preventing resource leaks in high-churn CI chains.

- Secure sandboxing of each browser session to avoid cross-call
  contamination.

------------------------------------------------------------------------

## Milestones & Sequencing

### Project Estimate

- Small: 2–3 weeks to MVP

### Team Size & Composition

- Small Team: 1–2 total people (full-stack engineer, optional QA/PM
  input)

### Suggested Phases

**Prototype Navigation & A11y Report (Week 1)**

- Key Deliverables:

  - Materials: 'navigate', 'a11y_report', and 'fetch_html' endpoint
    implementations.

  - Responsible: Lead engineer.

- Dependencies: Playwright, axe-core library.

**Link Extraction & Filtering (Week 2)**

- Key Deliverables:

  - Stable 'get_links' endpoint with domain filtering.

  - Expanded tests for edge-case anchor discovery.

- Dependencies: Integration with page DOM extractors.

**Playwright MCP Command Surface (Week 2–3)**

- Key Deliverables:

  - Pass-through for all Playwright MCP commands.

  - Consistent API schema for LLM chaining.

- Dependencies: Up-to-date compatibility with Playwright’s MCP protocol.

**LLM/Fetch Co-Design and Output Stabilization (Week 3)**

- Key Deliverables:

  - Validate outputs work with LLM agent’s expectations.

  - Tighten error handling, command atomization.

- Dependencies: LLM test harness.

**CI Integration Scripts & Finalization (Week 4)**

- Key Deliverables:

  - Example CI scripts showing full a11y remediation cycle.

  - MVP deployment and validation in representative CI workflow.

- Dependencies: DevOps for pipeline integration.

------------------------------------------------------------------------
