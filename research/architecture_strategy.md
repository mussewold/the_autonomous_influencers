## Architecture Strategy

### 1. Agent Pattern: Hierarchical Swarm (FastRender)
For Project Chimera, the Hierarchical Swarm, specifically the FastRender Pattern is the definitive choice over a Sequential Chain.




Rationale: Sequential chains are fragile; if one step fails, the entire process halts. The FastRender swarm utilizes specialized roles (Planner, Worker, and Judge) to allow for high parallelism and robust error recovery.



The Roles:


Planner: Decomposes abstract goals into a Directed Acyclic Graph (DAG) of executable tasks.



Worker: Stateless, ephemeral agents that execute atomic tasks (e.g., drafting a caption or calling an MCP tool).


Judge: Acts as the gatekeeper, reviewing Worker output against persona constraints and safety guidelines.


### 2. Human-in-the-Loop (HITL): The Safety Layer
The HITL framework is not a manual bottleneck but a probability-based governance layer integrated into the Judge agent's workflow.



Location of Approval: Approval happens post-generation but pre-execution/upload/publishing.


Escalation Logic:


* Auto-Approve (> 0.90 confidence): The action is executed immediately.


* Async Approval (0.70 - 0.90 confidence): The task is paused and added to a human review queue in the Orchestrator Dashboard while the agent moves to other tasks.


* Reject/Retry (< 0.70 confidence): The Judge automatically triggers a retry with refined instructions.

### 3. Database Strategy: Hybrid SQL + Vector Store
While "high-velocity" metadata often suggests NoSQL, Project Chimera's requirements for complex campaign configurations and transactional integrity favor a hybrid approach.


* Transactional Metadata (PostgreSQL): PostgreSQL is selected for storing user data, campaign configurations, and operational logs. Its clustering capabilities support the required horizontal scalability for 1,000+ concurrent agents.



* Semantic Metadata (Weaviate): High-velocity "memories" and persona-relevant world knowledge are offloaded to a Vector Database (Weaviate). This allows for efficient Retrieval-Augmented Generation (RAG) without bloating the relational database.




* Episodic Cache (Redis): Short-term task queuing and ephemeral state are handled by Redis to ensure the system remains responsive.

## 4. System Architecture Diagram

```mermaid
graph TD
    subgraph "Orchestrator Control Plane"
        A[Human Operator] -->|Sets Objectives| B[Orchestrator Hub]
        B -->|Syncs Policy| C[AGENTS.md / SOUL.md]
    end

    subgraph "FastRender Swarm"
        D[Planner] -->|Generates Task DAG| E[Worker Swarm]
        E -->|Executes MCP Tools| F[Judge Agent]
        F -->|Low Confidence| G{HITL Safety Layer}
        G -->|Manual Review| H[Dashboard Review Queue]
        H -->|Approve/Edit| I[Final Action]
        F -->|High Confidence| I
    end

    subgraph "Data Persistence Layer"
        I -->|Log Transaction| J[(PostgreSQL: SQL)]
        I -->|Commit Memory| K[(Weaviate: Vector)]
        I -->|On-Chain Event| L{{Blockchain Ledger}}
    end

    subgraph "External World (MCP)"
        E <-->|Standardized API| M[MCP Servers: Twitter, Coinbase, etc.]
    end

    I -->|Publish/Transact| M