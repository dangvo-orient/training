# A2A (Agent-to-Agent Protocol)

A2A is an open protocol that enables AI agents to discover, communicate, and collaborate seamlessly - regardless of their underlying frameworks or providers

## key capabilities

- agent discovery: agent can advertise their capabilities using an "Agent Card", allowing client agents to identify the best agent for a specific task
- capability negotiation: agents can discuss what types of communication they support, or work the best (e.g text-based, structured forms)
- secure collaboration: agents can work together on complex, multi-step projects while keeping their internal workings private

## key components

- agent card: a simple JSON document (often hosted at `/.well-known/agent.json`) that describes an agent's identity (name, version), capabilities, supported modalities (text, audio, video), endpoints for communication
- client & remote agents
    - client agent: wraps user request in a task - with unique IDs - and selects the appropriate remote agent via discovery
    - remote agent: receives the task and executes it, returning status updates or final artifacts
- task lifecycle & messaging: tasks are structured and stateful - it flows from submission to completion and failure -> messages are exchanged via JSON-RPC over HTTP, Server-Sent Events (SSE) for real-time updates
- security: A2A supports enterprise-level security:
    - transport via HTTPS or mTLS
    - authentication via OAuth, JWT, or OIDC
    - build-in observability/audit hooks

## A2a vs MCP

- MCP: focuses on how an agent connects to tools, services, or APIS - essentially agent-to-tool/agent-to-service
- A2A: focuses on communication and collaboration between agents themselves -> one coordinates tasks across other agents using A2A while each agent might internally use MCP to access tools
- other protocols: ACP, ANP