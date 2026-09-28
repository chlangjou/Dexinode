# Distributed Cognitive Execution Reference Specification v0.3

- Status: **Accepted for reference implementation**
- Date: 2026-09-28
- Authorizing decision: [ADR 0004](../decisions/0004-distributed-cognitive-execution-reference-slice.md)
- Decision issue: [#42](https://github.com/chlangjou/Dexinode/issues/42)
- Predecessor: [Repository-Repair Verifiable Execution Fabric v0.2](bounded-repository-repair-verifiable-execution-v0.2.md)
- Scope: **first implementation-oriented vertical slice**
- Experimental Gate: **none**

## 1. Purpose

This specification defines the smallest end-to-end implementation that can test Dexinode new system boundary:

> A Consumer expresses a bounded cognitive execution intent; Dexinode selects a Provider capable of satisfying that intent; the Provider executes inside an isolated task-scoped environment using its own Agent／Skill topology; and the Consumer receives Artifact(s) plus structured execution evidence.

The slice intentionally does not test whether one model family, Agent framework, latent method, or Specialist architecture is best.

The implementation question is:

> **Can Dexinode preserve a stable Consumer／Provider contract, strict requester-resource isolation, provider-internal implementation freedom, and useful execution receipts in one complete working path?**

## 2. Non-goals

The first slice does not implement or decide:

- public or permissionless discovery;
- decentralized registry federation;
- reputation or global scoring;
- marketplace, payment, token, settlement, or disputes;
- dynamic pricing;
- arbitrary cross-provider workflows;
- cross-provider latent／KV exchange;
- persistent multi-tenant Agent societies;
- requester-local shell access;
- requester-local filesystem mounts;
- credential delegation;
- custom model training;
- benchmark leaderboards;
- production-grade confidential computing;
- formal proof of sandbox isolation.

## 3. Reference flow

    Consumer CLI
        |
        | TaskIntent + TaskBundle
        v
    Static Provider Registry
        |
        | hard-constraint match
        v
    ProviderDescriptor
        |
        | negotiated / derived
        v
    ExecutionContract
        |
        v
    Provider Runtime
        |
        +-- create ephemeral task sandbox
        +-- materialize explicit task bundle only
        +-- network deny-by-default
        +-- choose internal Agent/Skill configuration
        +-- execute
        +-- run required Verifier(s)
        +-- produce Artifact(s)
        +-- produce ExecutionReceipt
        +-- destroy / quarantine task sandbox
        |
        v
    Consumer
        |
        +-- verify receipt schema / hashes
        +-- inspect result
        +-- accept / reject locally

The Provider may be hosted on the same physical developer machine during reference development, but it must execute as if it were remote: no implicit access to Consumer-local resources is permitted.

## 4. Security-domain invariant

### 4.1 Consumer domain

Consumer-private state includes, by default:

- home directory;
- unrelated project files;
- SSH keys and API tokens;
- browser cookies and sessions;
- local Agent memory;
- LAN services;
- local databases;
- credentials;
- policy files;
- private task material not included in the Task Bundle.

### 4.2 Provider domain

Provider receives only:

- the TaskIntent;
- the explicit Task Bundle;
- the derived ExecutionContract;
- protocol metadata required for the request.

### 4.3 No ambient authority

The implementation must uphold:

    ProviderAuthority = ExplicitExecutionContract

not:

    ProviderAuthority = ConsumerProcessAuthority

The Provider must not inherit Consumer process credentials, local mounts, unrestricted networking, or environment variables merely because both sides run on the same host during development.

## 5. Core protocol objects

The first implementation may use JSON or YAML on disk／HTTP. The semantic fields below are normative; transport is not.

### 5.1 TaskIntent

Represents what the Consumer wants accomplished without prescribing the Provider internal Agent topology.

Minimum fields:

    task_id: string
    goal: string
    capability_requirements:
      - capability_id: string
        required: true
    verification_requirements:
      independent_verification: boolean
    constraints:
      max_wall_time_s: integer | null
      max_cost_units: number | null
      network: deny | allowlist
      persistence: ephemeral
    requested_outputs:
      - artifact_type: string

The goal may initially contain natural language. Capability requirements and constraints should remain machine-readable.

### 5.2 TaskBundle

Contains only material intentionally disclosed to the Provider.

Minimum fields:

    bundle_id: string
    files:
      - logical_path: string
        sha256: string
    manifest_sha256: string

The reference implementation should materialize bundle contents into a new Provider-owned sandbox directory or container filesystem.

No path in a Task Bundle grants access to the Consumer original source path.

### 5.3 ProviderDescriptor

Describes one Provider externally relevant capacity.

Minimum fields:

    provider_id: string
    protocol_revision: v0.3
    capabilities:
      - capability_id: string
        version: string
    capacity:
      max_concurrent_tasks: integer
      execution_classes:
        - string
    verification:
      supported:
        - string
    isolation:
      filesystem: task_sandbox_only
      network: deny_by_default
      persistence: ephemeral
    runtime:
      implementation_id: string
      implementation_revision: string

Optional implementation metadata may disclose model, Agent framework, hardware, Skill inventory, or latency estimates, but the Consumer contract must not depend on a specific internal topology.

### 5.4 ExecutionContract

Binds one selected Provider to one task.

Minimum fields:

    contract_id: string
    task_id: string
    provider_id: string
    provider_descriptor_hash: string
    task_bundle_hash: string
    granted_capabilities:
      - string
    network_policy:
      mode: deny | allowlist
      destinations: []
    filesystem_policy:
      mode: task_sandbox_only
    credential_policy:
      mode: none
    persistence_policy:
      mode: ephemeral
    verification_policy:
      required:
        - string
    deadline:
      max_wall_time_s: integer | null

For v0.3:

- filesystem policy MUST be task_sandbox_only;
- credential policy MUST be none;
- persistence policy MUST be ephemeral;
- network SHOULD be deny; allowlists are reserved for later slice extensions.

### 5.5 Artifact

A Provider output intended for Consumer inspection or later local acceptance.

Minimum metadata:

    artifact_id: string
    contract_id: string
    artifact_type: string
    logical_name: string
    sha256: string
    media_type: string

Artifacts never directly mutate Consumer durable state.

### 5.6 VerificationRecord

Minimum fields:

    verifier_id: string
    verifier_revision: string
    scope: string
    independence_class: string
    result: pass | fail | error | not_run
    coverage_notes: string
    evidence_refs:
      - string

The reference slice may use deterministic schema／hash／fixture verification plus a provider-supplied content verifier. Independence claims must be explicit and modest.

### 5.7 ExecutionReceipt

Binds the result to what actually executed.

Minimum fields:

    receipt_id: string
    contract_id: string
    provider_id: string
    provider_descriptor_hash: string
    implementation_id: string
    implementation_revision: string
    started_at: string
    finished_at: string
    terminal_state: succeeded | failed | timed_out | rejected
    task_bundle_hash: string
    capabilities_used:
      - string
    execution_configuration:
      agent_topology_summary: string
      skill_revisions:
        - string
      model_or_backend_refs:
        - string
      verifier_revisions:
        - string
    artifacts:
      - artifact_id: string
        sha256: string
    verification_records:
      - verifier_id: string
        result: string
    isolation:
      filesystem: task_sandbox_only
      network: deny
      credentials: none
      persistence: ephemeral
    cleanup:
      attempted: boolean
      result: success | failed | quarantined
    failure:
      code: string | null
      message: string | null
    receipt_sha256: string

The receipt does not need to expose private chain-of-thought or raw latent state.

## 6. Provider internal freedom

The Provider may fulfill the same contract using one strong Agent, several independent explorers plus synthesis and verification, a general Core plus Decision Skills and deterministic Operators, or another topology.

The Consumer may request externally meaningful properties such as independent verification, but must not need to know internal prompt layout, hidden reasoning state, or model-specific latent representation.

## 7. First reference task family

The reference implementation should use a bounded repository exploration／analysis task because it produces inspectable artifacts without granting direct mutation authority.

Suggested initial capability contract:

    repository.explore

Optional required sub-capabilities:

    repository.architecture.inspect
    repository.security.inspect
    repository.synthesize
    repository.verify

The Consumer packages a repository fixture or snapshot into the Task Bundle.

The Provider returns:

    analysis.md
    findings.json
    execution-receipt.json

The Provider does not push commits, alter the Consumer repository, access unrelated files, or receive Consumer Git credentials.

The exact AI backend is replaceable. A deterministic/mock backend is allowed for protocol tests; at least one real Agent backend is required before declaring the vertical slice complete.

## 8. Reference implementation components

### 8.1 Consumer CLI

Responsibilities:

- load TaskIntent;
- package TaskBundle;
- hash manifest;
- query static registry;
- select an eligible Provider;
- create ExecutionContract;
- submit task;
- receive Artifact(s) and ExecutionReceipt;
- validate hashes and schema;
- place outputs in an explicit Consumer output directory.

### 8.2 Static Provider Registry

A checked-in configuration listing one or more ProviderDescriptors.

No peer discovery protocol is required.

### 8.3 Provider Runtime

Responsibilities:

- validate ExecutionContract;
- reject unsupported capability or policy requests;
- create isolated task workspace;
- materialize only TaskBundle files;
- invoke configured Agent backend;
- invoke required verifier(s);
- hash outputs;
- emit ExecutionReceipt;
- clean up or quarantine workspace.

### 8.4 Agent backend adapter

A narrow interface allowing the Provider to change internal execution without changing the Dexinode protocol.

Suggested shape:

    execute(task_context) -> ProviderExecutionResult

Initial adapters may include:

- deterministic/mock adapter for lifecycle tests;
- command／process adapter for a real external Agent runtime.

Dexinode v0.3 does not implement its own Agent framework.

### 8.5 Verifier adapter

Suggested shape:

    verify(task_context, artifacts) -> VerificationRecord

At least one deterministic verifier must run in the reference slice.

## 9. Isolation requirements

The reference implementation is accepted only if the demo demonstrates:

1. Consumer does not pass its environment wholesale to Provider.
2. Provider has no requester-home-directory mount.
3. Provider receives no Consumer credentials.
4. Provider task filesystem starts from the explicit Task Bundle.
5. Provider network is disabled for the reference task.
6. A task cannot read a sentinel file placed outside the Provider sandbox.
7. Task state is deleted after success; failed deletion results in quarantine and receipt failure metadata.
8. A second task cannot read the first task private workspace state.
9. Artifacts are copied out through the protocol boundary, not by sharing Consumer writable directories.
10. Consumer durable state changes require a separate local action outside Provider authority.

Container, namespace, VM, or equivalent mechanisms may be used. The mechanism is replaceable; the observable isolation properties are what matter.

## 10. Selection policy

The first scheduler is intentionally simple.

Selection order:

1. protocol revision compatible;
2. all required capabilities present;
3. requested verification supported;
4. isolation constraints compatible;
5. declared capacity available;
6. deterministic tie-break.

No learned router, reputation model, price auction, or probabilistic success predictor is required.

This is deliberate: the first slice should test whether the Provider abstraction works before optimizing routing.

## 11. Failure states

The implementation must distinguish at least:

- NO_PROVIDER;
- CAPABILITY_MISMATCH;
- POLICY_MISMATCH;
- CONTRACT_REJECTED;
- SANDBOX_SETUP_FAILED;
- EXECUTION_FAILED;
- EXECUTION_TIMED_OUT;
- VERIFICATION_FAILED;
- ARTIFACT_INVALID;
- CLEANUP_FAILED;
- PROTOCOL_ERROR.

Failures must produce a terminal receipt when the Provider had accepted the contract far enough to create an execution record.

## 12. Acceptance criteria

The first reference vertical slice is complete when all of the following are reproducibly demonstrated.

### Contract

- One TaskIntent can be matched to a ProviderDescriptor and bound into an ExecutionContract.
- Provider internal backend can be swapped without changing TaskIntent or ExecutionContract schema.
- Unsupported capability／policy requests fail closed.

### Isolation

- Consumer runs with no local AI model requirement.
- Provider cannot read a Consumer-side sentinel file outside the task bundle.
- Provider has no Consumer credentials.
- Network is disabled for the reference execution.
- Workspaces are task-scoped and do not leak between two consecutive requests.

### Execution

- At least one deterministic/mock backend completes the full lifecycle.
- At least one real Agent backend completes the same lifecycle.
- Provider may use one or multiple internal Agent roles without protocol changes.

### Evidence

- Output artifacts are content-hashed.
- ExecutionReceipt identifies Provider, implementation revision, capabilities used, backend references, verification records, isolation mode, terminal state, and cleanup state.
- Consumer validates receipt and artifact hashes before presenting the result as eligible.

### Failure handling

- At least one intentionally unsupported request is rejected.
- At least one execution failure produces a structured terminal state.
- At least one verifier failure prevents a result from being marked successful.
- Cleanup failure is visible and cannot be silently reported as clean success.

## 13. Implementation order

Recommended bounded sequence:

1. data models and schema validation;
2. static Provider Registry and hard-constraint matcher;
3. local transport abstraction;
4. Provider sandbox lifecycle;
5. deterministic/mock backend;
6. Artifact + Receipt generation and validation;
7. deterministic verifier;
8. real Agent backend adapter;
9. isolation and failure acceptance tests;
10. end-to-end demo and evidence report.

Do not add federation or market features while any earlier acceptance criterion remains unresolved.

## 14. Repository evidence

Implementation should preserve:

- example TaskIntent;
- example ProviderDescriptor;
- example ExecutionContract;
- example receipts;
- isolation test fixtures;
- failure-path tests;
- one recorded reference demo configuration;
- concise reproducibility instructions.

Do not commit credentials, private repositories, model weights, or large transient Agent logs.

## 15. Research watch policy during implementation

External research remains relevant if it materially changes:

- the capability contract;
- Consumer／Provider isolation;
- Agent runtime composition;
- verifier independence;
- execution receipts and provenance;
- Provider capacity semantics;
- scheduling economics;
- security or authority boundaries.

Other model／Agent papers may be recorded as watch items but do not block the reference slice.

## 16. Exit and next decision

Completion of v0.3 authorizes a new human decision, not automatic expansion.

Possible next decisions include:

- add a second independently implemented Provider;
- add controlled network capabilities;
- add provider failover／redundancy;
- add capability artifact distribution in addition to remote invocation;
- compare provider strategies on time-to-verified-result;
- begin a limited federation experiment.

Marketplace, reputation, and payment remain later questions.
