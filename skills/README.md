## Agent Skill Registry (Runtime)
### Overview
This directory contains the Skill packages for Chimera Agents. Each skill is an MCP Tool designed to be invoked by a Worker Agent and verified by a Judge Agent. Skills follow a strict contract-first design to ensure reliability in autonomous swarms.

1. **skill_transcribe_media**
- Purpose: Allows agents to perceive video and audio content from external URLs (YouTube, X, TikTok) to gather intel or repurpose content.

- Input Contract (JSON):

```JSON

{
  "url": "string",
  "language_hint": "string (optional)",
  "format": "text | segments | vtt"
}
``` 
- Output Contract (JSON):
``` 
JSON

{
  "transcript": "string",
  "confidence_score": "float",
  "metadata": { "duration": "int", "author": "string" }
}
``` 
2. **skill_generate_social_post**
- Purpose: The core creative engine. It takes a content pillar and persona context to draft platform-specific posts.

- Input Contract (JSON):

JSON
``` 
{
  "persona_id": "uuid",
  "platform": "twitter | linkedin | farcaster",
  "topic_context": "string",
  "constraints": { "max_chars": "int", "include_hashtags": "boolean" }
}
``` 
- Output Contract (JSON):

JSON
``` 
{
  "content_draft": "string",
  "media_suggestions": "array",
  "scheduled_time_utc": "iso8601"
}
``` 
3. **skill_onchain_payment (Agentic Commerce)**
- Purpose: Leverages the Coinbase AgentKit to allow agents to execute economic actions (e.g., paying for a premium API or tipping a collaborator).

- Input Contract (JSON):

JSON
``` 
{
  "recipient_address": "string (0x...)",
  "amount_usd": "float",
  "network": "base | ethereum",
  "reason_code": "string"
}
``` 
- Output Contract (JSON):

JSON
``` 
{
  "transaction_hash": "string",
  "status": "confirmed | pending",
  "remaining_balance_usd": "float"
}
``` 

- Execution Logic
Selection: The Planner identifies the need for a skill based on the task DAG.

- Invocation: The Worker calls the MCP Tool using the defined Input Contract.

- Validation: The Judge verifies the Output Contract against the agent's SOUL.md (e.g., "Is this post in the correct voice?") and the AgentTask budget (e.g., "Does the agent have enough funds for this payment?").