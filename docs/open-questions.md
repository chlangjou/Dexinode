# Open questions

This is the active research backlog. Questions should move into experiments or decision records as they become concrete.

## Value and scope

- Which tasks benefit enough from specialization to offset routing and verification overhead?
- Is Dexinode primarily a protocol, a runtime, a marketplace, or a federation toolkit?
- What can it provide that existing agent tool protocols and distributed job systems cannot?
- Should the first use case be software engineering, private enterprise knowledge, scientific work, or edge inference?

## Skill semantics

- How narrow should a skill be?
- How are compatible versions negotiated?
- Can capability descriptions remain expressive without becoming unmatchable natural-language claims?
- How do we represent probabilistic quality and domain limitations?
- How does a skill declare side effects and required authority?

## Routing and planning

- Does the caller select a complete workflow, or can downstream nodes delegate?
- How are cost, latency, quality, privacy, locality, and diversity traded off?
- How does the router explore new providers without risking important workloads?
- How do we detect routing loops and correlated model failures?
- Who pays for failed attempts and verification?

## Verification

- Which task classes allow deterministic verification?
- When is replication cheaper than sophisticated verification?
- How do we prevent verifier collusion, bribery, or shared blind spots?
- Can private inputs be verified without exposing them?
- What evidence is useful without leaking proprietary models or prompts?
- How do humans enter or override the acceptance process?

## Reputation

- Should reputation attach to a node, operator, skill version, model, or complete supply chain?
- How quickly should old evidence decay?
- How do new entrants avoid a permanent cold-start disadvantage?
- How do we resist Sybil identities and reputation laundering?
- Can reputation remain plural and consumer-specific while still being portable?

## Security and safety

- How are prompt injection and tool abuse contained across trust boundaries?
- What prevents a skill from exfiltrating task data?
- How are malicious skill declarations and dependency substitution detected?
- How are credentials delegated with least privilege and revoked?
- What tasks should never be routed to unknown nodes?
- How do we contain denial-of-service, poisoned evidence, and dispute spam?

## Decentralization and governance

- Which components must truly be decentralized to avoid capture?
- What is the minimum viable federation model?
- How are protocol changes proposed and adopted?
- How can conformance tests evolve without becoming a central gatekeeper?
- How do legal jurisdictions and export restrictions affect node participation?

## Economics

- Is direct payment necessary, or are reciprocal/federated quotas enough?
- What unit represents value: time, compute, task, verified result, or negotiated bundle?
- How are failed or partially accepted tasks accounted for?
- Could markets reward benchmark gaming or low-value task fragmentation?
- At what stage would a token add real utility rather than distraction?

## Operations

- How are nodes updated without silently changing a skill's behavior?
- What observability can be shared without revealing private workloads?
- How does the network handle intermittent edge nodes?
- How are large artifacts transferred and retained?
- What is the simplest deployment experience for a small local specialist?

## Naming and project identity

- Is “Dexinode” sufficiently distinct in trademarks, packages, and domains?
- Which domain should anchor the project?
- Should the public name emphasize decentralization, skills, weaving, or nodes?
- When should the working name become a formal naming decision?
