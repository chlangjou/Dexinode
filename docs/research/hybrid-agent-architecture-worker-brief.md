# Dexinode Hybrid Agent Architecture Research — Worker Brief

- Date: 2026-08-10
- Status: Human-authorized pre-Gate research brief
- Decision issue: [#27](https://github.com/chlangjou/Dexinode/issues/27)
- Research-frame decision: [ADR 0001](../decisions/0001-hybrid-resident-agent-research-frame.md)
- Execution type: literature, official metadata, and production evidence only

請用繁體中文執行並交付研究結果。

Continue the Dexinode project from:

`https://github.com/chlangjou/Dexinode`

## 0. 開始前必讀與衝突規則

先讀取 repository 中：

1. `AGENTS.md`
2. `HANDOFF.md`
3. `status/current.md`
4. `docs/decisions/0001-hybrid-resident-agent-research-frame.md`
5. `docs/research/2026-08-10-mvss-routing-evidence-baseline.md`
6. `gates/gate-a-specialization/reviews/gate-a-final-human-decision.md`
7. `gates/gate-b-orchestration/reviews/gate-b-final-human-decision.md`
8. `gates/gate-b-orchestration/reviews/post-closure-math-content-retrospective.md`

`docs/research/2026-08-10-mvss-routing-evidence-baseline.md` 是 repository 內對 MVSS、GCI、routing economics 與 FIM eligibility/HOLD 的 durable consolidation。若執行環境另有原始研究報告，可以作 supporting material；發生衝突時仍以 repository durable state 為準。

若 repository durable state 與本 brief 有實質衝突，先列出衝突並停止。不得自行改寫 Gate evidence、human decisions 或 durable state。

Current state：

- Gate A：`PASS / CLOSED`
- Gate B：`FAIL / CLOSED`
- 沒有活動中的實驗 Gate
- FIM／syntax-aware MVSS eligibility：`HOLD`
- 本輪不解除 FIM HOLD，也不繼續 DELULU 補件
- 不下載模型權重
- 不執行 inference 或 GPU 實驗
- 不建立或凍結 benchmark
- 不凍結 acceptance criteria
- 不修改既有 Gate evidence
- 不 commit、不 push
- 本輪只做 literature、official metadata 與具體 production-evidence research

## 1. 研究立場

Dexinode 是待證偽的研究假說，不是預設成立的產品方案。

不要試圖證明「小模型一定能擊敗大型模型」。真正問題是：

> 在 Local Agent control plane、Local Resident Model、memory/context orchestration、deterministic tools/verifiers、local pseudonymization，以及 Remote Model escalation 的組合下，是否存在一部分真實工作，能以使用者願意採用的品質、成本、延遲、隱私與人工負擔完成？

研究單位必須是完整 agent configuration，而不是孤立模型分數：

`model + memory + context policy + harness/loop + tools + verifier + fallback + human review`

必須辨識 memory manager、workflow search、judge、verifier、retry budget 或 fallback 是否把大型遠端模型的能力與成本藏在模型分數之外。

## 2. v0.1 working assumptions

以下是避免研究漂移的 working assumptions，不是 Gate criteria：

1. 不存在完美模型；最大 context window 只表示可輸入，不表示可可靠利用。
2. Local-first，不是 local-only。
3. Resident Core 定義為：

   `Local general model + memory + context orchestrator + tools/verifiers + task state`

4. 本地 Agent/control plane 擁有：

   - workspace 與長期記憶；
   - context packet 編譯；
   - pseudonymization／restoration mapping；
   - tool credentials、permissions 與 side-effect policy；
   - loop budget、停止條件與稽核紀錄；
   - remote escalation、輸出驗證與最終整合。

5. Remote Model 只取得特定 subtask 所需的最小 context packet。
6. Specialist 正確拒答、要求澄清或 escalation 是正常成功路徑，不要求 standalone replacement。
7. Pseudonymization／restoration 暫列高機率可工程化的元件，不是本輪核心未知數；敏感資訊漏偵測、上下文再識別與語意損失仍須列為限制。
8. v0.1 effective context envelope：

   - Specialist task packet：目標 8K–16K，32K 暫定上限；
   - Resident Core 單次工作集：目標 16K–32K；
   - 64K 以上原則上重新檢索、依語意邊界切分或摘要；
   - repository、歷史與長期記憶保存在 context 外並保留 provenance。

9. 「夠好」的研究篩選定義：

   - bounded task contract 明確；
   - 約 70% in-scope cases 能不修改或一次小修改完成；
   - 相對實際替代流程，主動人工時間降低約 30%；
   - 推論變動成本降低約 50%，或提供替代方案沒有的隱私／離線價值；
   - 不得有未攔截的重大、不可逆錯誤；
   - 使用者看過失敗模式後仍願意再次使用。

上述數值只是研究篩選線。請檢查文獻能否支持其可量測性；不得描述成科學共識，也不得擅自更改或凍結。

## 3. 本輪唯一總問題

> 現有研究與公開模型證據，是否足以形成一個可信的 Dexinode Hybrid Resident-Agent architecture hypothesis，值得下一步撰寫 bounded architecture specification？

本輪不回答哪個模型最終勝出，也不設計正式實驗。

## 4. Research Track A — Agent Memory 與 Context Engineering

研究 memory system 如何協助有限 context 的本地模型完成行動，不要只整理產品功能或 conversational recall。

至少區分：

1. raw episodic memory；
2. structured facts／entity memory；
3. project/task state；
4. procedural／workflow memory；
5. failure／experience memory；
6. code/repository provenance；
7. working memory／current task packet。

依下列生命週期分析：

- representation and storage；
- extraction；
- retrieval and routing；
- reconciliation／conflict handling；
- consolidation；
- update／forgetting／revocation；
- provenance；
- context assembly；
- security、poisoning recovery 與 rollback。

核心問題：

1. Memory 是否改善 downstream action/task success，而不只是 factual QA？
2. Memory manager 使用什麼 backbone？是否依賴大型遠端模型？
3. 是否保留 raw source、version 與撤銷鏈，或只保存可能失真的 LLM summary？
4. 遇到更新、矛盾、stale memory 與 poisoning 時如何處理？
5. Context compression 的品質損失、P95 latency、token cost 與維護成本為何？
6. 有沒有以 absolute-small／SLM 管理 memory 的可信證據？
7. 哪些部分可由 deterministic code、database、search、version control 完成？
8. 哪些部分仍需要模型判斷？
9. Benchmark 測的是 conversational recall，還是 project/workflow/action memory？
10. Retrieval 成功但 reader reconciliation／action 失敗的證據為何？
11. Context selector 如何判斷資訊已足夠、應繼續搜尋、拒答或 escalation？
12. Code/repository packet 是否保留跨檔案依賴、介面、測試與來源定位？

優先查核但不限於：

- MemGPT；
- A-MEM；
- Mem0；
- MemoryAgentBench；
- LongMemEval／LongMemEval-V2；
- RealMem；
- Mem2ActBench；
- LightMem；
- MemMachine；
- “Are We Ready For An Agent-Native Memory System?”；
- retrieval-based agent memory 的負面或限制性研究。

不要做完整 memory survey。選出 6–10 篇最能改變 Dexinode 責任分配的一手研究。

## 5. Research Track B — Loop、Harness、Workflow 與 Graph Engineering

不要把所有 multi-step prompting 視為同一類 Agent。

至少區分：

1. simple fixed pipeline；
2. ReAct／observe-think-act loop；
3. plan-and-execute；
4. verifier／test-feedback loop；
5. reflection／self-repair；
6. tree／graph search；
7. deterministic state machine／DAG；
8. automatically searched workflow；
9. homogeneous multi-agent；
10. heterogeneous multi-model workflow。

對每種方法查核：

- 相對 direct prompting 或 simple fixed loop 的增益；
- 是否固定 backbone、budget、tools、context 與 evaluator；
- token／latency／step／retry 成本；
- error amplification、false consensus 與 correlated failure；
- termination、dead-loop、budget exhaustion；
- 是否能跨模型、跨任務、跨 scaffold 轉移；
- 是否依賴可靠 scalar verifier；
- workflow search 是否 overfit validation benchmark；
- graph complexity 是否必要；
- 能否由單一 Agent 依序模擬 homogeneous multi-agent workflow；
- harness/interface 是否比模型本身更影響結果；
- judge 或 test 是否造成 hidden model calls、false accept 或 reward hacking。

優先查核但不限於：

- ReAct；
- SWE-agent；
- Agentless；
- ADAS；
- AFlow；
- GPTSwarm；
- AgentSquare；
- OneFlow／strong single-agent baseline；
- harness-aware evaluation；
- scaffold effect；
- LoopsBench；
- 2026 workflow-optimization surveys 與 negative studies。

特別尋找「更簡單流程同樣好或更好」的反證。

## 6. Research Track C — Agent-specialized Small Models

截至 2026-08-10 搜尋最新 official model cards、technical reports、official repositories 與 peer-reviewed／preprint papers。Prompt 中的名稱只是 seeds，必須先核實 exact model ID、存在性、版本與最新狀態。

不得只搜尋 Qwen 或 DeepSeek，也不得只抄 leaderboard。

### 6.1 Scale classes

#### A. Edge-small

- 小於 1B total parameters；
- 可在手機、NPU、CPU 或極低資源環境執行。

#### B. Absolute-small

- 1B–8B total parameters；
- dense 或完整模型確實落在此範圍。

#### C. Active-small MoE

- activated parameters ≤8B；
- total parameters >8B；
- 必須同時報 total／active parameters；
- 不得作為 absolute-small 證據。

#### D. Remote／frontier reference

- proprietary API 或大型 open-weight model；
- 只作 remote capability reference；
- 不得列入 Local Model viability。

### 6.2 Capability classes

至少搜尋：

1. function calling／tool selection／argument generation；
2. multi-turn tool use；
3. GUI／mobile／computer use；
4. coding-agent／repository／terminal operation；
5. search／research agent；
6. memory manager／context selector；
7. planner／controller／router；
8. verifier／critic／reward model。

### 6.3 Seed candidates

Seeds 不代表已選定，也不保證 exact name 正確或仍為最新：

- FunctionGemma 270M；
- TinyAgent 1.1B／7B；
- xLAM function-calling family；
- Hammer；
- Fara-7B；
- AgentCPM-GUI-8B；
- MAI-UI 2B／8B；
- current Qwen 3.x dense local models with native tool use；
- Qwen3-Coder-Next；
- Qwen3.x active-small MoE candidates；
- current DeepSeek V4 family；
- current Qwen3.7／later hosted agent models。

任何 DeepSeek V4、Qwen3.7 或後續模型都必須先核實 total/active parameters、是否 hosted-only、license 和 release metadata。不得因 active parameters 小就列為本地 absolute-small。

### 6.4 Candidate record

每個候選記錄：

- exact model ID、revision、release date；
- license／gating／commercial constraints；
- base lineage；
- specialization training method；
- dense／MoE；
- total／active parameters；
- native context length；
- benchmark 實際使用的 context；
- quantization；
- demonstrated hardware／memory／energy／latency；
- task contract；
- benchmark、environment、harness、tool schema；
- retry／pass@k／reasoning budget；
- evaluator 或 LLM judge；
- end-to-end success，而不只是 syntax accuracy；
- abstention／clarification／failure recovery；
- known negative evidence；
- classification：Resident Core candidate、Local Specialist、Remote Reference 或 Ineligible。

不產生跨 capability 的單一總排行榜。

## 7. Research Track D — Hybrid Local／Remote Architecture

只研究 architecture evidence，不重開 routing economics Gate。

回答：

1. 哪些工作必須由可信 deterministic local control plane 執行？
2. 哪些工作需要 Local Resident Model？
3. 哪些 bounded tasks 可交給 Local Specialist？
4. 哪些情況應升級 Remote Model？
5. Remote Model 只回傳建議，或可產生哪些待驗證 artifact？
6. 本地如何驗證、整合、還原結果並約束 side effects？
7. 若每個重要步驟仍依賴 Remote Model，Local Model 還剩什麼實質價值？
8. 本地 memory/context manager 是否能避免傳送完整 history？
9. 最小揭露、task-scoped disclosure、prompt injection persistence 與 poisoned-memory recovery 有哪些證據？
10. 完整 workflow 的人工負擔、P50/P95 latency、fallback、rework 與 failure loss 能否量測？
11. 哪些 Agent functions 可以完全由 deterministic software 完成？
12. 哪些全域／不可切分任務應明確列為 v0.1 不支援？

不要設計新的 routing algorithm，也不要估算尚無證據的去中心化市場經濟。

## 8. Evidence policy

只使用：

- peer-reviewed papers；
- arXiv/OpenReview primary papers；
- official model cards；
- official technical reports；
- official repositories；
- 有具體方法與數字的 production engineering reports。

證據分級：

- `A`：peer-reviewed 或多系統 controlled comparison；
- `B`：可審核 preprint／independent reproduction；
- `C`：vendor-authored benchmark 或 production report；
- `D`：official metadata／model card only；
- `E`：anecdote／community claim。

Major conclusions 不得只依賴 C、D、E。

所有 Agent benchmark 數字盡可能附上：

- model；
- harness；
- context policy；
- tool interface；
- step/token/cost budget；
- retries／sampling；
- environment revision；
- evaluator／judge。

缺少影響比較的重要欄位時，標記 `harness-confounded`，不得直接與其他分數比較。

Major claims 使用：

- `ESTABLISHED`
- `PARTIALLY SUPPORTED`
- `OPEN`
- `CONTRADICTED`

推論必須明示為 inference，不得寫成來源直接證明。

## 9. Deliverables

產出四份可稽核文件。

### 9.1 `hybrid-agent-evidence-map.md`

- Memory/context、loop/harness/graph、hybrid local/remote 的證據矩陣；
- 每項方法真正改善什麼；
- backbone、harness、成本與限制；
- 正面與負面證據；
- deterministic engineering 與 model-dependent judgment 的分界。

### 9.2 `agent-specialized-small-model-landscape.md`

- Edge-small、absolute-small、active-small、remote reference 四層模型表；
- exact metadata、capability contract、部署證據與 benchmark confounds；
- 至少覆蓋八類 capability；
- 不產生單一總排行榜。

### 9.3 `dexinode-hybrid-architecture-hypothesis.md`

建立 responsibility matrix，至少包含：

- deterministic local software；
- Local Resident Model；
- Local Specialist；
- Remote Model；
- human reviewer。

針對下列功能分配責任：

- intent clarification；
- task decomposition；
- memory write/read/update/revocation；
- context selection；
- context packet compilation；
- pseudonymization/restoration；
- tool selection/execution；
- planning；
- verification；
- failure recovery；
- escalation；
- final integration；
- audit logging。

每個分配必須標明 evidence、uncertainty、failure mode。明確列出 v0.1 不支援區域。

### 9.4 `hybrid-agent-research-decision.md`

只能選擇：

- `PROCEED TO BOUNDED ARCHITECTURE SPEC`
- `HOLD`
- `PIVOT TO LOCAL CONTROL PLANE`
- `STOP / NEGATIVE`

並回答：

1. 是否有可信的 Minimum Viable Resident Core region？
2. 是否至少有兩類 agent-specialized absolute-small capability 值得保留？
3. Memory/context 與 loop engineering 是否可能降低所需模型尺度？
4. 還是它們本身需要大型遠端模型，導致論證循環？
5. Dexinode 的主要價值較可能來自 distributed specialist network，還是 trusted local control plane？
6. 下一個最高決策價值的 bounded question 是什麼？
7. 解答下一問題前最少還缺哪些證據？

只能提出一個下一步 bounded question。不得在本輪設計 benchmark、Gate 或執行計畫。

## 10. Decision interpretation

### `PROCEED TO BOUNDED ARCHITECTURE SPEC`

至少存在：

- 一條 credible Local Resident Core 路徑；
- 不需要每一步呼叫 Remote Model；
- 至少兩類有端到端證據的 absolute-small agent capability；
- memory/context/loop 責任可明確拆解；
- 完整 workflow 指標原則上可量測。

### `HOLD`

方向有證據，但主要結果仍被 harness、vendor claims、部署資料、memory-backbone、judge 或 verifier 依賴混淆。

### `PIVOT TO LOCAL CONTROL PLANE`

本地 Agent 的隱私、狀態、context、工具與驗證有價值，但沒有足夠證據支持 Local Model／distributed small specialists 承擔主要推理。

### `STOP / NEGATIVE`

Local layer 相對一般 cloud agent 沒有可辨識的成本、隱私、離線、延遲、稽核或人工負擔優勢。

## 11. Stop point

完成四份文件後停止供 human review。

不得：

- 下載權重；
- 執行模型；
- 建 benchmark；
- 凍結 acceptance criteria；
- 新增 Gate；
- 修改 Gate A／B 結論；
- 解掉 FIM HOLD；
- 繼續 DELULU 前置補件；
- 開始 routing economics；
- 設計 token economy、reputation、settlement 或 governance；
- commit 或 push Git。

本 Worker 的核心不是再找「誰分數最高」，而是找出：**哪些 Agent 元件真的能讓較小模型變得夠用，以及哪些元件其實只是把大模型成本藏到 memory、harness、judge、verifier 或 fallback 裡。**
