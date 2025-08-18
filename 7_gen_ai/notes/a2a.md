# A2A (Agent-to-Agent Protocol)

A2A is an open protocol that enables AI agents to discover, communicate, and collaborate seamlessly - regardless of their underlying frameworks or providers

## how it works

- capability discovery: agent can advertise their capabilities using an "Agent Card", allowing client agents to identify the best agent for a specific task
- task management: communication focuses on completing protocol-defined tasks with a lifecycle -> tasks may be completed immediately or, if long-running, agents stay in sync by sharing status updates
    - output of a task is known as an "artifact"
- collaboration: agents can send each other messages to communicate context, replies, artifacts, or user instructions
- ux negotiation: agents can discuss what types of communication they support, or work the best (e.g text-based, structured forms)

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
- the output of a task is known as an "artifact"

## A2a vs MCP

<div style="display: flex; justify-content: space-around;">
    <image src="./images/complementary_protocols.png" style="height: 400px" />
</div>

- MCP: focuses on how an agent connects to tools, services, or APIS - essentially agent-to-tool/agent-to-service
- A2A: focuses on communication and collaboration between agents themselves -> one coordinates tasks across other agents using A2A while each agent might internally use MCP to access tools
- other protocols: ACP, ANP

# MCP (Model Context Protocol)

core idea: give AI agents a consistent way to connect with tools, services, and data in a structured, secure way - no matter of their underlying systems

## why

traditionally, each AI agent or framework had its own plugin/integration format -> fragment:
- custom plugins per LLM vendor
- no consistent security model
- high integration costs

-> MCP solves this by standardizing how models talk to tools

## core ideas

1. Client-Server Model
    - client = usually the AI model (ChatGPT, Claude, etc)
    - server = tool or service provider (db, API, etc)
    - communication is bidirectional -> both can send requests
2. transport: runs over JSON-RPC 2.0, typically using stdio, WebSockets, or HTTP as transport
3. capabilities: tools/services expose capabilities in a declarative way
4. schema-based definitions: each tool is defined with JSON Schema → ensures validation, auto-docs, and safe parameter handling
5. security
    - permissions and scopes are part of the protocol
    - tools declare what they expose, and models can enforce policies

# a2a framework

## server

- agent skills: describes a specific capability or function the agent can perform -> tell clients what kinds of tasks the agent is good for
- agent cars: JSON document
    - `url`: where the agent runs at
    - `capabilities` param:
        - push_notifications: whether the agent can send asynchronous updates (via webhooks) to clients about task status
        - state_transition_history: whether the agent tracks and exposes the full history of task state transitions
        - streaming: supports real-time, incremental updates via SSE
    - `supports_authenticated_extended_card`: signals whether the agent can serve an extended version of its agent card when requested by an authenticated client

- agent executor: 2 primary methods
    - `async def execute (self, context: RequestContext, event_queue: EventQueue)`: handles incoming request that expect a response or a stream of events
        - processes user's input (via `context`) and uses `event_queue` to send back `Message`, `Task`, `TaskStatusUpdateEvent`, or `TaskArtifactUpdateEvent` objects
    - `async def cancel(self, context: RequestContext, event_queue: EventQueue)`: handles requests to cancel an ongoing task

    -> `RequestContext`: provides information about the incoming request, `EventQueue`: used by the executor to send events back to the client

- `DefaultRequestHandler`: takes `AgentExecutor` and a `TaskStore`
    - `taskStore`: manages lifecycle of tasks, especially for stateful interactions, streaming

## client

1. fetch the AgentCard & initialize the client

```python
base_url = 'http://localhost:9999'

async with httpx.AsyncClient() as httpx_client:
    # Initialize A2ACardResolver
    resolver = A2ACardResolver(
        httpx_client=httpx_client,
        base_url=base_url,
        # agent_card_path uses default, extended_agent_card_path also uses default
    )
```

- `A2ACardResolver`: fetches agent cards (public or extended) from provided base paths, provides the flexibility for using authenticated endpoints when needed
- `A2AClient`: client-side interface to interact with an A2A agent -> encapsulates HTTP communication with the agent endpoints and simplifies common actions