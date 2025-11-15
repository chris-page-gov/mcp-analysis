# Prompt Record

- **Title:** Initial Research Prompt, simple
- **Date:** 15/11/2025
- **Researcher:** Chris Page
- **Target Output:**
- **Model / Version:** GPT-5.1 Thinking
- **Context Links:**
    -

## Prompt

```text
You are an expert AI research assistant tasked with producing a rigorous, balanced, and up-to-date analysis of the Model Context Protocol (MCP): past, present, and future.

Your job is NOT to advocate for or against MCP, but to map the landscape: what it is, how it has evolved, why people are excited, why others are sceptical, what real problems exist, what mitigations are emerging, and what this means for using MCP as a core integration layer in a Government / Local Authority AI Hub.

Current date: [insert today’s date when you run this].

------------------------------------------------
A. SCOPE AND HIGH-LEVEL GOALS
------------------------------------------------

1. Give a carefully evidenced overview of:
   - How MCP works at a high level (servers, tools, prompts, resources, discovery, auth, etc.).
   - How the specification and ecosystem have evolved over time (especially from late 2024 onwards).
   - The main lines of criticism (technical, security, governance, UX, ecosystem, “hype”) and the main lines of support.
   - How newer ideas (e.g. Anthropic’s Skills, connectors frameworks, agent orchestration frameworks) complement or compete with MCP.
   - What this implies for using MCP as a backbone for a Government / Local Authority AI Hub that mediates conversational access to systems.

2. Throughout, clearly distinguish:
   - **Facts**: verifiable statements from specs, vendor docs, academic or technical papers, and concrete implementation behaviour.
   - **Perceptions / opinions**: what different commentators, vendors, or practitioners *claim* or *fear*.
   - **Your own analysis**: reasoned synthesis and judgement that you derive from the evidence.

3. Allow your research plan to evolve:
   - Start with the structure below, but if you discover important themes, technologies, or critiques that materially change the picture, update your outline and say explicitly what you added and why.
   - When extending scope, stay anchored to the central question: “Is MCP a robust, secure, and sustainable basis for AI-mediated integration, especially in public-sector / enterprise settings?”

------------------------------------------------
B. RESEARCH TASKS
------------------------------------------------

B1. Map current perceptions and “chatter”

Goal: build a grounded view of how MCP is currently perceived across the ecosystem.

Tasks:
1. Scan a wide range of sources:
   - Technical blogs and engineering posts (Anthropic, Microsoft, GitHub, Auth0, security vendors, cloud providers, independent engineers, etc.).
   - Community discussions: GitHub issues on MCP-related repos, Hacker News / Reddit threads, Stack Overflow questions, relevant Discord/Slack summaries if indexed publicly, LinkedIn/Medium posts.
   - Vendor marketing content and product announcements that reference MCP.

2. Identify and categorise perceptions into themes, such as:
   - “MCP is the ‘USB-C for AI’ / universal connector.”
   - “Discovery is an unsolved or weak part of the spec.”
   - “MCP clogs the context window or is inefficient at scale.”
   - “MCP has no security / is insecure by design.”
   - “MCP is over-engineered / too complex vs simple APIs.”
   - “Everyone is jumping on the MCP bandwagon to sell things.”
   - “MCP is essential for multi-tool, multi-agent ecosystems.”

3. For each theme:
   - Provide representative **quotes** (short, attributed, properly cited).
   - Identify who is saying this (e.g. security researchers, big vendors, open-source devs, consultants, etc.).
   - Note whether the view is widespread or niche, and whether it’s based on concrete evidence, early implementations, or misunderstandings of the current spec.

Deliverable section:
- **Section 2 – Perceptions and discourse**
  - 2.1 Sentiment overview (positive/negative/mixed).
  - 2.2 Key perception themes with representative quotes.
  - 2.3 Misconceptions vs legitimate concerns.

B2. Analyse technical criticisms and proposed solutions

Goal: dig into *substance* rather than surface hot takes.

Focus on at least:
1. **Discovery and registries**
   - How MCP discovery works in the spec (and any recent changes).
   - Approaches such as local OS-level registries, enterprise registries, and community registries.
   - Critiques: complexity, security risks, operational overhead, versioning and governance concerns.
   - Solutions and mitigations: registry patterns from Microsoft, GitHub, Windows, and open-source MCP registries; how these address or fail to address the criticisms.

2. **Context window bloat and performance**
   - Critiques that MCP “clogs the context window” because some implementations dump full tool lists, resource indexes, or large blobs into context.
   - Distinguish:
     - Problems that stem from **spec design**.
     - Problems that stem from **naïve implementations** (e.g. sending everything eagerly).
   - Summarise emerging patterns to reduce overhead:
     - Lazy / progressive discovery and loading.
     - Using code execution / function calling to interact with MCP servers without including everything in the conversational context.
     - Agent-side context engineering strategies for MCP (e.g. Anthropic posts on context management and code execution with MCP).
   - Capture any concrete benchmarks or case studies where MCP-based agents became slower or more expensive, and how those were improved.

3. **Security and identity**
   - Summarise claims that “MCP has no security” or is fundamentally insecure.
   - Compare these claims with:
     - The current MCP spec’s security and authorisation model (e.g. OAuth 2.1 patterns, resource indicators, token scoping, dynamic client registration).
     - Published security guidance and best practices for MCP from vendors and security researchers.
   - Identify major security concerns raised (e.g. multi-tenant auth, tool impersonation, server compromise, data exfiltration, prompt-injection via MCP tools).
   - Document mitigations:
     - Updates to the spec over time.
     - Guidance from security blogs / advisories (e.g. security vendors writing about MCP).
     - Patterns like placing MCP behind API gateways, using least-privilege tokens, and server-side policy enforcement.

4. **Complexity, standardisation gaps, and real-world enterprise challenges**
   - Summarise critiques that MCP is over-engineered, underspecified in places, or hard to adopt in enterprises.
   - Include perspectives from:
     - Vendors trying to build MCP servers/clients.
     - Enterprise case-study blog posts.
     - Academic or practitioner papers evaluating MCP deployments.
   - Identify gaps or pain points:
     - Lack of standardised semantics for certain tool/resource types.
     - Observability, logging, and auditability.
     - Multi-tenant governance in large organisations.
     - Versioning and compatibility.

5. **Positive technical assessments**
   - Collect analyses that argue MCP:
     - Improves separation of concerns between models and tools.
     - Reduces duplication by allowing “build once, integrate anywhere”.
     - Provides a unified path to expose existing APIs/services to multiple AI clients.
   - Identify any concrete success stories or case studies (especially in enterprise settings) where MCP clearly added value versus ad-hoc tool integrations.

Deliverable section:
- **Section 3 – Technical critiques and mitigations**
  - 3.1 Discovery and registries.
  - 3.2 Context window and performance.
  - 3.3 Security and identity.
  - 3.4 Complexity and standardisation gaps.
  - 3.5 Positive technical assessments and real-world benefits.

B3. Build a timeline of MCP’s evolution

Goal: understand how the spec and ecosystem have changed and whether criticisms have been addressed over time.

Tasks:
1. Track key events:
   - Initial public release of MCP and early reference implementations (e.g. late 2024).
   - Major spec updates, especially around:
     - Security and authorisation.
     - Discovery/registries.
     - Backwards compatibility and versioning.
   - Key ecosystem milestones:
     - Adoption by major vendors (Anthropic, Microsoft, GitHub, others).
     - Launch of official SDKs and community libraries.
     - Emergence of prominent open-source MCP servers and registries.
     - Conferences, blog series, or academic papers that significantly shifted understanding.

2. For each event:
   - Note date, source, and what changed.
   - Link criticisms that pre-dated the change to any mitigations that came afterwards.
   - Highlight where critics may still be referencing *older* states of the spec or ecosystem.

Deliverable section:
- **Section 4 – Timeline and evolution**
  - 4.1 Chronological timeline with annotation.
  - 4.2 Mapping criticisms to spec/ecosystem changes.
  - 4.3 Remaining open issues despite updates.

B4. Compare MCP with alternative paradigms

Goal: clarify what MCP actually adds beyond “just APIs”, and whether those differences help or hinder.

Tasks:
1. Compare MCP with:
   - Traditional REST/gRPC APIs and OpenAPI-style integration.
   - LLM function-calling / tools that directly wrap APIs without MCP.
   - Agent-framework integrations (e.g. LangChain, Semantic Kernel tool abstractions).
   - Other vendor-specific ecosystems, e.g.:
     - Anthropic Skills: task-oriented schemas, procedural knowledge + tools, and how they can work alongside MCP servers.
     - Connector frameworks and app-specific plugin models (e.g. proprietary connectors that are *not* MCP).

2. For each comparison, be specific about:
   - What MCP standardises (protocol, discovery, capabilities description, streaming, etc.).
   - Where MCP is simply “an extra layer” around APIs, and whether that is beneficial or just overhead.
   - How well each alternative addresses:
     - Tool discovery and lifecycle.
     - Security and auth.
     - Governance and observability.
     - Multi-client reuse (one server, many AI clients).
     - Developer ergonomics and ecosystem lock-in.

3. Summarise whether MCP is:
   - Primarily a transport/protocol standard.
   - Also a governance and discovery pattern.
   - Or effectively just one of several competing ways to expose tools to models.

Deliverable section:
- **Section 5 – MCP vs APIs, Skills, and other approaches**
  - 5.1 MCP vs “raw” APIs and function calling.
  - 5.2 MCP vs Skills and similar task abstractions.
  - 5.3 MCP vs agent-framework tool ecosystems.
  - 5.4 Where MCP clearly helps vs where it may hinder.

B5. Investigate “bandwagon” and commercial hype

Goal: assess the claim that organisations are “jumping on MCP just to sell things”.

Tasks:
1. Identify vendors, consultancies, and tool makers marketing MCP-related products:
   - MCP servers and SDKs.
   - MCP registries and management platforms.
   - Security, governance, or observability tools positioned around MCP.
   - Consulting offerings labelled as “MCP strategy” or similar.

2. For each:
   - Determine whether they provide substantive technical value (e.g. real features, open-source repos, detailed documentation) vs shallow rebranding or vague claims.
   - Note where marketing rhetoric over-states MCP’s capabilities or maturity.

3. Provide a nuanced assessment:
   - Where is there genuine innovation aligned with MCP’s goals?
   - Where does it look like opportunistic bandwagoning?
   - How does this commercial activity affect trust and adoption, especially in cautious environments like government and regulated industries?

Deliverable section:
- **Section 6 – Hype vs substance**
  - 6.1 Vendor landscape and offerings.
  - 6.2 Evidence of bandwagon effects.
  - 6.3 Impact on trust, risk, and procurement decisions.

B6. Additional positive and negative analyses

Goal: uncover less-obvious, high-quality critiques or endorsements.

Tasks:
1. Actively search for:
   - Academic or practitioner papers analysing MCP in domains like digital forensics, legal tech, healthcare, finance, or public sector.
   - In-depth technical blogs that go beyond surface marketing.
   - Security research (red-teaming MCP, variant hunting, IAM analyses, etc.).
   - Thoughtful critiques or endorsements from respected engineers and architects.

2. Include:
   - At least a few case studies where MCP has been piloted or deployed at scale.
   - Any evidence of MCP being rejected in favour of alternative patterns, and why.

Deliverable section:
- **Section 7 – Deeper analyses and case studies**
  - 7.1 Notable academic / practitioner work.
  - 7.2 Industry case studies (successes and failures).
  - 7.3 Lessons learned for future MCP evolution.

------------------------------------------------
C. APPLICATION: GOVERNMENT / LOCAL AUTHORITY AI HUB
------------------------------------------------

Goal: evaluate the implications of all the above for using MCP as a foundational integration layer in a Government or Local Authority AI Hub.

Scenario:
- Assume an organisation wants a central AI “hub” that mediates most human–system interaction through conversational interfaces.
- Integration options include:
  1. MCP-based connectors to systems (a shared standard across apps).
  2. Each Line-of-Business (LOB) application implementing its own model/tools with no MCP.
  3. Pure agent-orchestration approaches where each system exposes some kind of agent, and a meta-orchestrator coordinates them (with or without MCP).
  4. Hybrid options (e.g. MCP for infrastructure-level tooling + Skills or other task abstractions for workflows).

Tasks:
1. Assess MCP in this setting across:
   - Security, identity, and data protection (including multi-tenant concerns).
   - Governance, audit, and observability (logging, traceability of tool use, policy enforcement).
   - Discovery and lifecycle (how an AI Hub finds, vets, and updates MCP servers).
   - Operational complexity and support burden.
   - Vendor lock-in vs interoperability.
   - Handling of context window and performance constraints at scale.
   - Fit with public-sector regulatory expectations and risk appetites.

2. Compare to alternative patterns:
   - Direct LOB-specific integrations without MCP.
   - Agent-orchestration approaches where each system exposes its own agent API.
   - Using MCP together with higher-level abstractions (e.g. Skills/task schemas) for governed workflows.

3. Make **explicit, evidence-based recommendations**, such as:
   - When MCP is a strong fit.
   - When MCP should be used selectively (e.g. only for certain classes of tools or data).
   - When alternative approaches may be simpler or safer.
   - What governance and security controls are non-negotiable if MCP is adopted for public-sector AI Hubs.

Deliverable section:
- **Section 8 – Implications for a Government / Local Authority AI Hub**
  - 8.1 Scenario description and assumptions.
  - 8.2 Option analysis (MCP-centric vs alternatives).
  - 8.3 Risks, mitigations, and governance patterns.
  - 8.4 Recommendations and design principles.

------------------------------------------------
D. OUTPUT STRUCTURE AND QUALITY BAR
------------------------------------------------

Please structure the final report roughly as follows:

0. **Executive summary (1–2 pages)**
   - Key findings about MCP’s strengths, weaknesses, and trajectory.
   - Top 5–7 insights relevant to architects considering MCP for an AI Hub.
   - Clear “headline” recommendations.

1. **Introduction and methods**
   - Briefly describe your research approach, major source types, and date range.
   - Note any important scope adjustments you made along the way.

2. **Perceptions and discourse** (from B1)

3. **Technical critiques and mitigations** (from B2)

4. **Timeline and evolution** (from B3)

5. **MCP vs alternative paradigms** (from B4)

6. **Hype vs substance** (from B5)

7. **Deeper analyses and case studies** (from B6)

8. **Implications for a Government / Local Authority AI Hub** (from C)

9. **Open questions and future directions**
   - Remaining uncertainties about MCP’s long-term role.
   - Spec areas that still need work.
   - How emerging ideas like Skills or other task abstractions might reshape the landscape.
   - What to watch over the next 12–24 months.

10. **Glossary and references**
    - Concise glossary of key terms (MCP server/client, Skills, tools, resources, registries, dynamic client registration, etc.).
    - Full references in a consistent academic or technical style, with clickable URLs where possible.

Quality requirements:
- Be **balanced and critical**. Highlight both real problems and real successes.
- Always separate:
  - Factual description.
  - Reported opinions and perceptions.
  - Your own reasoned evaluation.
- Prioritise **recent** sources (last 12–18 months) but include earlier material where it explains how perceptions and the spec evolved.
- Prefer primary and technically detailed sources (specs, vendor engineering blogs, security write-ups, academic papers) over purely marketing content.
- Where claims conflict, present the competing views side-by-side and explain why they differ and which is better supported by evidence.
- Where appropriate, quantify (even roughly): scale of deployments, performance impacts, security incidents/concerns, etc.
```

## Outcome Summary

- **Linked Artifact:**
- **Post-processing Notes:**
- **Open Questions:**
