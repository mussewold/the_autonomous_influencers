# Technical Specification

## 1. Database Schema (Hybrid Layer)

### PostgreSQL (Transactional)
* **Table: `agents`**: `id` (UUID), `persona_id`, `wallet_address`, `status` (active/idle).
* **Table: `campaigns`**: `id`, `objective`, `budget_limit`, `owner_tenant_id`.
* **Table: `transactions`**: `tx_hash`, `agent_id`, `amount_usdc`, `purpose` (e.g., "gas_fees", "ad_spend").

### Weaviate (Semantic Memory)
* **Class: `AgentMemory`**: Properties: `content` (text), `embedding` (vector), `timestamp`, `sentiment_score`.

## 2. API Contract: The "Task Packet"
All internal swarm communication must follow this JSON schema:

```json
{
  "task_id": "uuid-v4",
  "role": "WORKER",
  "persona_context": "SOUL_ID_45",
  "action": "content_generation",
  "input_data": {
    "trend_topic": "AI Agentic Commerce",
    "platform": "Twitter"
  },
  "safety_constraints": ["no_politics", "brand_safe_only"],
  "priority": 1-10
}
``` 


