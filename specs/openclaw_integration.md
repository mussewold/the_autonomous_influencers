Based on current 2026 "Agent Internet" standards, this handles how Chimera interacts with the wider OpenClaw (formerly Moltbot) network.

## 1. Network Discovery & Status
Project Chimera agents will broadcast their "Availability" to the OpenClaw network using the **Status Broadcasting Protocol**. 

* **State Sync:** Agents will post their `heartbeat` and `current_goal` to a dedicated OpenClaw MCP Resource.
* **Inter-Agent Collaboration:** When a Chimera agent requires a service it cannot perform (e.g., specialized video editing), it will broadcast a "Request for Worker" (RFW) to the OpenClaw swarm.

## 2. Soul File Portability
* **Covenant Protocol:** Chimera personas (`SOUL.md`) are designed to be "OpenClaw Compatible," allowing for seamless identity verification across agent-only social networks like **Moltbook**.