# Dexinode Hybrid Agent Research Decision

- 決策日期：2026-08-10
- Worker recommendation：`HOLD`（保留下文作 provenance）
- Accepted human decision（2026-08-11）：`PROCEED TO BOUNDED ARCHITECTURE SPEC`
- Decision record：[ADR 0002](../decisions/0002-proceed-to-bounded-repository-repair-spec.md)／[Issue #29](https://github.com/chlangjou/Dexinode/issues/29)
- Durable state：Gate A `PASS / CLOSED`；Gate B `FAIL / CLOSED`；無活動實驗 Gate；FIM／syntax-aware MVSS `HOLD`

## Accepted decision: `PROCEED TO BOUNDED ARCHITECTURE SPEC`

Human review 接受 Worker 的 evidence、confounders 與未解項，但不接受以「完整 configuration 已有 integrated real-work evidence」作為開始寫 spec 的先決條件。原 brief 要求的是可信路徑、至少兩類 absolute-small end-to-end signal、可拆責任與可量測指標；Worker 自己的證據已滿足這些 proceed-to-spec 條件。

這項決策只允許把 hypothesis 寫成 bounded、可追溯、可證偽的 repository-repair specification。它**不表示** Local Resident Core、任何 checkpoint、16K–32K envelope、部署經濟或完整 workflow 已驗證，也不授權 benchmark、Gate 或 inference。

| Brief 的 proceed-to-spec 條件 | Human-review disposition |
|---|---|
| credible Local Resident Core 路徑 | 4B–8B candidate region + versioned memory + deterministic control plane + bounded packet + remote fallback，足以被規格化 |
| 不需每一步呼叫 Remote | GUI、tool workflow、coding 已有 absolute-small end-to-end signal；尚待後續證據量化 remote dependence |
| 至少兩類 absolute-small capability | MAI-UI-2B、xLAM-2 3B／8B、SERA-8B 提供三類保留區域 |
| memory／context／loop 責任可拆 | architecture hypothesis 已完成 responsibility decomposition |
| workflow 指標可量測 | quality、human time、P95、privacy、fallback、severe failure 均可操作化；沒有通用 threshold |

下文保留 Worker 原始 `HOLD` recommendation，讓 Agent interpretation 與 human decision 可分辨。

# Worker recommendation: `HOLD`（未被 human review 接受）

現有研究足以形成一個**可被清楚陳述、值得保留的 hybrid resident-agent hypothesis**，但不足以宣稱它已可信到可直接撰寫 bounded architecture specification。阻礙不是「完全沒有小模型能力」，而是關鍵結論仍同時受下列因素混淆：

- memory/context controller 經常使用 frontier／remote backbone，或只在 conversational QA 驗證；
- specialist headline 常混入特定 scaffold、長 context、pass@k／Best-of-N、LLM judge或 vendor environment；
- absolute-small 的真實 device latency／memory／energy資料稀少；
- 尚無一個公開配置同時量到 end-to-end quality、active human burden、P95 latency、privacy、fallback與 severe failure；
- local control plane 的 trust價值有明確 architecture evidence，但 Local Resident Model 承擔主要推理的 integrated evidence仍缺。

因此 Worker recommendation 不是 `PROCEED TO BOUNDED ARCHITECTURE SPEC`，也尚未降為 `PIVOT TO LOCAL CONTROL PLANE`。

## 1. Decision criteria assessment

| `PROCEED` 所需條件 | 本輪結果 | 判定 |
|---|---|---|
| credible Local Resident Core 路徑 | 可描述一個 4B–8B、16K–32K packet、versioned memory、deterministic tools/verifiers、remote fallback 的**候選區域**；沒有 integrated real-work evidence | `OPEN` |
| 不需要每一步都呼叫 remote | FunctionGemma、MAI-UI、xLAM、SERA、AgentCPM等顯示部分 bounded steps 可 local；但 memory reconciliation／final integration仍可能依賴大模型 | `PARTIALLY SUPPORTED` |
| 至少兩類 absolute-small agent capability 有 end-to-end evidence | GUI：MAI-UI-2B AndroidWorld；tool workflow：xLAM-2 3B/8B τ-bench；coding：SERA-8B SWE-bench Verified | `PARTIALLY SUPPORTED`；成立但各有license／hardware／harness缺口 |
| memory／context／loop 責任可明確拆解 | canonical storage、derived memory、packet、judgment、execution、verification、fallback可拆；見 [architecture hypothesis](./dexinode-hybrid-architecture-hypothesis.md) | `ESTABLISHED` 作 responsibility decomposition，不等於效能成立 |
| full-workflow metrics 原則上可量測 | quality、active human time、P50/P95、token/call、privacy、recovery、severe loss、reuse均可操作化 | `ESTABLISHED` 可量；threshold沒有共識 |

Worker 當時判定 `PROCEED` 的必要條件不是全部達到，故推薦不選 `PROCEED TO BOUNDED ARCHITECTURE SPEC`；human review 對此門檻映射的修正見文件開頭。

## 2. 七個必答問題

### 2.1 是否有可信的 Minimum Viable Resident Core region？

**有可信的候選路徑，但沒有可信的已證區域。判定：`OPEN`。**

候選路徑是：可信 deterministic local plane保存state／memory／credentials／policy；4B–8B general resident只在16K–32K working packet上處理澄清、分解、context judgment與integration；窄 specialist處理tool／GUI／code／search／verification；remote只處理超出local capability／risk／context的subtask，且本地驗證後才整合或執行。`Qwen/Qwen3.5-4B`（完整artifact約5B）是目前可指名的metadata候選之一，但其agent分數皆為vendor harness，且官方建議complex thinking至少128K，故不是validated resident證據。

其 component choices各有證據，但沒有一手研究證明這個完整 configuration 在同一真實 workflow 達成使用者願意採用的品質、人工時間、延遲、隱私與failure loss。因此只能稱「credible candidate region」，不能稱「validated MVR Core」。

### 2.2 是否至少有兩類 agent-specialized absolute-small capability 值得保留？

**是。判定：`PARTIALLY SUPPORTED`。**

至少保留：

1. **GUI／computer use**：`Tongyi-MAI/MAI-UI-2B` 在 AndroidWorld 報 49.1% end-to-end task success；Fara1.5-4B亦有 dynamic web signal。缺 device P95／energy與跨更新穩定性。
2. **structured multi-turn tool use**：xLAM-2 3B／8B 在 τ-bench 報 38.2／46.7；但 CC-BY-NC license、user simulator與部署數據是限制。
3. **repository coding**：`allenai/SERA-8B` 在 SWE-bench Verified 報 31.7% ±0.9、3 seeds、test evaluator；8B official card 建議80GB A100/H100，但論文 hardware 章節明確描述 SERA-32B，故不能當作一致的8B deployment evidence，也未支持consumer node。

這些 evidence 足以保留 capability classes，不能選出單一勝者，也不能把分數直接互比。完整 metadata與confounds見 [small-model landscape](./agent-specialized-small-model-landscape.md)。

### 2.3 Memory/context 與 loop engineering 是否可能降低所需模型尺度？

**可能，但只部分支持。判定：`PARTIALLY SUPPORTED`。**

- LightMem、DimMem、PrivScope、PlanTwin顯示1B–4B model配合 deterministic parsing／index／schema，能做 bounded extraction、retrieval、typed memory或disclosure judgment。
- Agentless、OneFlow、SWE-agent與CRITIC顯示 interface、fixed pipeline、external verifier可把部分能力從「模型內部」移到 harness。
- 反面是 LongMemEval-V2、MemoryAgentBench 與 AgentCPM-Explore 顯示 controller、summarizer或reader常依賴更強 model；retrieval成功後reader仍可大幅失敗。

所以 engineering 可能降低每一步需要的 model scale，但不等於已證明4B–8B能接手全局 reconciliation／planning／integration。

### 2.4 還是它們本身需要大型遠端模型，導致論證循環？

**存在實質循環，但不是所有元件都循環。**

可以確定不需遠端大模型的部分包括：versioned storage、Git／DB provenance、ACL、transactions、parsers、AST、token budget、schema、pseudonym map、tool execution、tests、rollback、audit。FunctionGemma的手機實測、LightMem online SLM、PrivScope的3B local mediation與PlanTwin heuristic projection也證明部分semantic工作可local。

循環仍集中在：跨episode consolidation、conflict reconciliation、long-horizon controller、open-ended verification與final integration。這正是 `HOLD` 的中心原因。

### 2.5 Dexinode 主要價值較可能來自 distributed specialist network，還是 trusted local control plane？

**較可能先來自 trusted local control plane。判定：`PARTIALLY SUPPORTED`。**

理由不是 specialist network已被否定，而是local plane的責任——workspace、canonical memory、context packet、identity mapping、credentials、tool authority、verification、fallback與audit——不依賴某個 specialist最後勝出，且由CaMeL、PlanTwin、PrivScope、MemSecBench及production confidential-compute architecture共同支持。相對地，distributed specialist network還需證明：absolute-small deployment、fresh-task transfer、成功率預測、handoff cost與human burden。

若後續證據顯示每個重要推理步驟仍需remote，應轉為 `PIVOT TO LOCAL CONTROL PLANE`；本輪尚未到該點，因至少三類absolute-small specialist已有end-to-end signal。

### 2.6 下一個最高決策價值的 bounded question 是什麼？

> **在不讓 Remote Model 承擔每一步 memory/context 管理的前提下，是否存在一個 4B–8B Local Resident Core 的最小責任集合，能在至少一類可回復且可 deterministic 驗證的真實 workflow 中，可靠地完成 intent／state／context／integration，並只把少數明確 subtask 升級給 specialist 或 remote？**

這是本文件唯一提出的下一步 bounded question。本輪不定義其 benchmark、Gate、acceptance threshold或執行計畫。

### 2.7 解答下一問題前最少還缺哪些證據？

最少需要的不是另一張 leaderboard，而是下列 evidence properties：

- 一個真實、bounded、可回復、具 deterministic verifier 的 workflow，且能分開 resident、specialist、remote與human貢獻；
- 4B–8B resident在固定16K–32K packet內的 intent、state、context-selection與final-integration結果，並保留raw provenance；
- 相同 model、tools、context、total budget下的 minimal fixed loop reference，避免把scaffold gain誤認model capability；
- remote依賴的逐步紀錄：哪些步驟因何升級、揭露多少、remote artifact是否被local verifier接受；
- active human minutes、P50/P95 latency、retry／fallback、escaped severe error與recovery，而不只pass@1；
- local memory manager不使用frontier model時的retrieval→reader reconciliation與poison-recovery證據；
- 至少一個有完整硬體、quantization、memory、latency與energy metadata的absolute-small configuration。

這些是 evidence gaps，不是本輪建立的 benchmark或execution plan。

## 3. 為何不是另外三個選項

### 3.1 Worker 原先不選 `PROCEED TO BOUNDED ARCHITECTURE SPEC`

Responsibility split 已可寫清楚，但「哪一部分4B–8B resident真能可靠承擔」仍是核心未知。直接寫 spec 會把 working assumptions（16K–32K、70%、-30%、-50%）不當地固化，並可能把 remote-backed memory evidence誤當 local resident evidence。

Human review 不接受這個門檻映射：bounded spec 可以把上述數值明載為 non-frozen，把未知責任與 falsifiers 明確化，而不宣稱能力成立。要求先有 integrated evidence 才能寫出用來界定 integrated evidence 的 spec，會倒置規格與驗證順序。

### 3.2 尚不選 `PIVOT TO LOCAL CONTROL PLANE`

MAI-UI-2B、xLAM-2 3B／8B與SERA-8B分別提供GUI、tool workflow、repository coding的end-to-end signal；LightMem／DimMem／PrivScope也顯示部分memory/context work可由small local model完成。這些還不足以證明Resident Core，但足以避免過早把local model降為純轉發器。

### 3.3 不選 `STOP / NEGATIVE`

Local layer有可辨識的privacy、state ownership、offline／failure containment、credential isolation、task-scoped disclosure與audit value。即使未來small-model reasoning thesis失敗，trusted local control plane仍與一般cloud agent有 architecture差異；因此目前沒有STOP所需的負面證據。

## 4. Major claims final status

| Claim | Status |
|---|---|
| 完整agent configuration而非孤立model score是正確研究單位 | `ESTABLISHED` |
| raw/versioned memory + derived views + bounded working packet是合理責任拆分 | `ESTABLISHED` |
| memory普遍改善真實project/action success | `OPEN` |
| 1B–4B SLM可完成bounded memory/context subroles | `PARTIALLY SUPPORTED` |
| intrinsic reflection可一般性self-correct | `CONTRADICTED` |
|複雜graph／homogeneous multi-agent一般性優於minimal loop | `CONTRADICTED` |
| 至少兩類absolute-small agent capability值得保留 | `PARTIALLY SUPPORTED` |
| active-small MoE可作absolute-small／edge證據 | `CONTRADICTED` |
| task-scoped local→remote disclosure可保留部分utility | `PARTIALLY SUPPORTED` |
| current evidence足以撰寫可證偽的bounded architecture spec | `PARTIALLY SUPPORTED`；human decision接受 |
| current evidence已驗證完整hybrid architecture | `OPEN` |
| trusted local control plane是Dexinode較穩健的近期價值來源 | `PARTIALLY SUPPORTED` |

## 5. Human-review stop point

Worker 在此停止後，human review 已依 Issue #29 作出 `PROCEED TO BOUNDED ARCHITECTURE SPEC` 決定。以下清單仍描述 Worker 執行時遵守的 stop boundary；新的授權也只限於文件規格化。

本輪在此停止。沒有：

- 解除FIM HOLD或繼續DELULU補件
- 修改Gate A／B evidence或closure
- 新增／凍結Gate、benchmark或acceptance criteria
- 執行模型、下載權重或GPU inference
- 重新開啟routing economics
- 設計routing algorithm、token economy、reputation或settlement
- commit或push Git

Supporting documents：

- [hybrid-agent-evidence-map.md](./hybrid-agent-evidence-map.md)
- [agent-specialized-small-model-landscape.md](./agent-specialized-small-model-landscape.md)
- [dexinode-hybrid-architecture-hypothesis.md](./dexinode-hybrid-architecture-hypothesis.md)
