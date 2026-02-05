## 1. Persona-Driven Content Generation
* **User Story:** "As a **Worker Agent**, I need to ingest the `SOUL.md` definition so that my content style, vocabulary, and values remain 100% consistent with my assigned persona."
* **Requirement (FR-001):** System MUST validate all generated content against the persona's "Brand Safety" parameters before sending it to the Judge.

## 2. Trend Perception via MCP
* **User Story:** "As a **Planner Agent**, I need to fetch real-time trends from the `news://` and `social://` MCP resources so I can prioritize high-impact content topics."
* **Requirement (FR-002):** The system MUST support parallel fetching from at least 3 distinct MCP sources to build a weighted trend score.

## 3. HITL Governance & Confidence Scoring
* **User Story:** "As a **Human Reviewer**, I need to see a detailed reasoning log for any action with a confidence score < 0.90 so I can make an informed Approval decision."
* **Requirement (FR-003):** If confidence is < 0.70, the system MUST bypass the human and automatically trigger a "Refine" loop with a Judge feedback log.