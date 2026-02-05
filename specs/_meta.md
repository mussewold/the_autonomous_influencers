## 1. Project Vision: "The Digital Sovereign"
`Project Chimera` is an autonomous network designed to evolve social media influence from static, human-operated accounts to a fleet of Autonomous Influencer Agents.
Unlike traditional bots, these agents possess:
* Perception: Real-time awareness of global trends via MCP.
* Reasoning: A "FastRender" swarm (Planner, Worker, Judge) to ensure high-quality, persona-aligned output.Agency: 
* Non-custodial crypto wallets (Coinbase AgentKit) to manage their own computational and marketing budgets.

## 2. Strategic Objectives
* Scalability: Support a fleet of 1,000+ concurrent agents with zero manual overhead.
* Trust & Safety: Maintain a "Human-in-the-Loop" (HITL) gate for any action with a confidence score below 0.90.* Economic Viability: Every agent must operate as a profit-center, tracking its own ROI on-chain.

## 3. Core Constraints
Constraint & Requirement:
* Connectivity: All external I/O and communication must use the Model Context Protocol (MCP).
* Intelligence: Agents must leverage Gemini 3 Pro or Claude 4.5 for high-stakes reasoning.
* Compliance: Strict adherence to the EU AI Act (automated self-disclosure of AI-generated content).
* Data Isolation: No shared state between separate influencer "Souls" to prevent persona leakage.

## 4. Tech Stack (The "Soul" Machine)
* Orchestration: Python 3.12+ (Managed by uv).
* Memory: Hybrid SQL (PostgreSQL) + Vector (Weaviate).
* Commerce: Coinbase AgentKit (USDC/Base Network).
* Communication: Pydantic-AI for type-safe agent handoffs.

## 5. Success Metrics
* Autonomous ROI: Monthly revenue (ad-rev, affiliate, or tips) exceeds agent compute costs.
* Safety Integrity: 0% brand-safety violations in public-facing content.
* Human Efficiency: A single human operator can oversee >50 agents via the "Async Approval" queue.