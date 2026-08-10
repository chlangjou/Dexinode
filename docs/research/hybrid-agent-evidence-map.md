# Dexinode Hybrid Agent Evidence Map

- 研究截止：2026-08-10
- 文件狀態：供 human review 的 literature／official metadata research；不是 architecture spec、Gate 或 acceptance criteria
- 研究單位：`model + memory + context policy + harness/loop + tools + verifier + fallback + human review`

## 0. 範圍與 durable-state 邊界

本文件已核對 `AGENTS.md`、`HANDOFF.md`、`status/current.md`、Gate A／B closure、MVSS、GCI、routing 與 eligibility/HOLD 材料。repository 與本輪 prompt **無實質衝突**：Gate A 為 `PASS / CLOSED`，Gate B 為 `FAIL / CLOSED`，目前沒有活動中的實驗 Gate，FIM／syntax-aware MVSS eligibility 維持 `HOLD`。本研究未修改上述結論、既有 evidence 或 acceptance criteria，也未下載權重、執行 inference、建立 benchmark、commit 或 push。

證據等級沿用本輪規則：

- `A`：peer-reviewed，或多系統 controlled comparison
- `B`：可審核 preprint／independent reproduction
- `C`：vendor-authored benchmark／有數字的 production report
- `D`：official metadata／model card only
- `E`：anecdote／community claim；不作主要結論依據

判定詞：`ESTABLISHED`、`PARTIALLY SUPPORTED`、`OPEN`、`CONTRADICTED`。

## 1. 結論先行：claim ledger

| Claim | 判定 | 最強正面證據 | 主要反證／限制 | Dexinode 含義 |
|---|---|---|---|---|
| 對 Dexinode 候選架構而言，將長期狀態留在 context 外、按任務組裝 working packet，是有證據支持的設計約束 | `PARTIALLY SUPPORTED` | [MemGPT](https://arxiv.org/abs/2310.08560)、[LongMemEval-V2](https://arxiv.org/html/2605.12493v1)、[PlanTwin](https://arxiv.org/html/2603.18377v1) | 「可輸入長 context」不等於正確調和；oracle evidence 仍會被 reader 誤讀；文獻未證明這對所有 workload 都是必要或最佳 | Dexinode 不以單一超長 prompt 充當 memory；raw state、索引、衍生記憶與 packet 採分層設計，但保留後續反證空間 |
| 現有 agent memory 普遍改善真實 downstream action success | `OPEN` | [Mem2ActBench](https://arxiv.org/html/2601.19935v1)、[MemoryArena](https://arxiv.org/abs/2602.16313) 開始測 action-dependent memory | 多數高分仍來自 conversational QA；Mem2Act 已給正確 tool，只測參數 grounding | 不得把 LoCoMo／LongMemEval QA 分數換算成可執行 workflow 成功率 |
| 1B–4B SLM 可負責部分 memory／context 管理 | `PARTIALLY SUPPORTED` | [LightMem](https://arxiv.org/html/2604.07798v1)、[DimMem](https://arxiv.org/abs/2605.15759)、[PlanTwin](https://arxiv.org/html/2603.18377v1)、[PrivScope](https://arxiv.org/html/2605.16630v1) | LightMem 的 offline consolidation 用大型 LLM；DimMem 仍以 QA 為主；semantic extraction／necessity judgment 有數秒延遲 | 可將 typed extraction、disclosure judgment 視為候選 bounded specialist；不能假定整個 memory manager 已被小模型解決 |
| 保存 raw source、version 與 provenance 比只存 LLM summary 更可靠 | `ESTABLISHED` | [Agent-native memory comparison](https://arxiv.org/html/2606.24775v1)、[MemMachine](https://arxiv.org/html/2604.04853v1)、[LongMemEval-V2](https://arxiv.org/html/2605.12493v1) | raw retrieval 也可能造成 context noise；需有 reconciliation 與版本選擇 | raw episodic/source record 應為可追溯 source of truth；summary 是可重建、可失效的 derived view |
| 複雜 graph／multi-agent workflow 一般性優於簡單 pipeline／single agent | `CONTRADICTED` | — | [OneFlow](https://arxiv.org/html/2601.12307v1)、[Agentless](https://arxiv.org/html/2407.01489v2)、[Harness Evolution](https://arxiv.org/html/2607.12227v1) 顯示簡化、平行取樣或固定 pipeline 可同樣好或更好 | 預設採最小 deterministic state machine；只有可量測增益才增加 graph／agent 角色 |
| 可靠外部 verifier／test feedback 可改善 self-repair | `PARTIALLY SUPPORTED` | [CRITIC](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fef126cefd7e00292f7a3f4ed815f6f8-Abstract-Conference.html)、SWE-agent／coding tests | [LLMs Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b6b6436d6c5ecf59bbf745c37-Abstract-Conference.html)；noisy verifier 可破壞正確答案 | verifier loop 適用於有獨立、可重跑的 scalar／structural check；純 introspective reflection 不是預設元件 |
| harness/interface 的影響足以使「模型分數」失真 | `ESTABLISHED` | [SWE-agent](https://arxiv.org/abs/2405.15793)、[SWE-Effi](https://arxiv.org/html/2509.09853v1)、[Scaffold Effect](https://arxiv.org/html/2607.22585v1) | 影響大小依 task/model 而異 | 所有能力登錄都必須是 configuration-level；不可建立單一 model leaderboard |
| 本地 gatekeeper 可在保留 cloud utility 時減少揭露 | `PARTIALLY SUPPORTED` | [PrivScope](https://arxiv.org/html/2605.16630v1)、[PlanTwin](https://arxiv.org/html/2603.18377v1)、[CaMeL](https://arxiv.org/abs/2503.18813) | 窄 domain／合成 task；模型式 necessity judgment 增加 latency；多回合 compositional leakage 仍難 | disclosure、credential、tool execution、restoration 必須留在 trusted local plane；privacy benefit 可量測但尚未跨 workflow 建立 |
| memory poisoning 可由「忘記／重寫摘要」充分復原 | `CONTRADICTED` | — | [MemSecBench](https://arxiv.org/html/2607.27080v1)：惡意記憶高度持續，selective repair 只部分成功 | 每次讀取均需 provenance／trust label；衍生索引可重建；應能 quarantine、rollback、re-index，而非只叫模型忘記 |
| 「約 70% 一次可用、人工時間 -30%、變動成本 -50%」是科學共識 | `CONTRADICTED` | 這些量都可操作化；task success、active time、token/call cost 均已有測量方法 | 沒有通用 threshold 共識；[METR RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) 在 mature repos 反見 19% slowdown | 保留為 v0.1 research screening line，不得描述成共識或凍結 criterion |

## 2. Track A — Agent Memory 與 Context Engineering

### 2.1 七類記憶的 representation 與責任邊界

| 記憶類型 | 建議 canonical representation | 主要寫入者 | 主要檢索鍵 | 更新／衝突規則 | 進 working packet 的形式 |
|---|---|---|---|---|---|
| raw episodic memory | append-only event／message／tool-result log；content hash、timestamp、actor、trust label | deterministic runtime | time、task、entity、source | 不覆寫；以 tombstone／supersession 表示撤回 | 只取必要原文 slice，附 source pointer |
| structured facts／entity memory | typed records／triples，加 `valid_from/to`、confidence、source IDs | deterministic extractor + bounded model judgment | entity、relation、valid time | multi-value 並存；衝突不靜默合併；以 source authority 和 recency 排序 | 少量候選 facts + conflict flag + citations |
| project/task state | versioned state machine／DAG、artifacts、open blockers、budgets | deterministic controller；human 可覆核 | project、task、state transition | schema validation；optimistic concurrency；rollback | current state、next legal transitions、budgets |
| procedural／workflow memory | versioned procedure／runbook／tool schema／policy | human + verified extraction | task contract、environment、version | 變更需版本；舊 procedure 不直接覆寫 | 適用步驟、前置條件、停止條件 |
| failure／experience memory | failure signature、attempt、environment、root-cause status、verified remedy | runtime + verifier + human label | symptom、tool、environment revision | 區分 observed correlation 與 confirmed cause；expiry | 相似失敗、已驗證修復、禁止重試項 |
| code/repository provenance | Git commit、path、line/object hash、build/test receipt、dependency graph | Git／filesystem／CI | symbol、path、commit、test | Git history為 source of truth；generated summary 可失效 | exact diff／symbol slices + commit + test state |
| working memory／current packet | ephemeral typed packet：goal、constraints、evidence、capabilities、budget、open uncertainty | local packet compiler | current subtask | task 結束即丟棄或歸檔；不得反向污染 canonical facts | 8K–16K specialist；16K–32K resident working target |

這張表是 architecture hypothesis 的責任拆分，不是已驗證產品設計。其核心依據是受控比較反覆顯示「抽象化越多不必然越好」，以及 raw evidence + provenance 能支援重新解釋、撤銷與 reader reconciliation；不是因為任何單一 memory framework 已完成所有生命週期。

### 2.2 Memory lifecycle：deterministic 與 model judgment 的分界

| 生命週期 | deterministic code／DB／VCS 可承擔 | 仍可能需要模型 | 最主要 failure mode | recovery invariant |
|---|---|---|---|---|
| representation & storage | schema、transactions、hash、encryption、ACL、version、append log | semantic typing、entity linking候選 | schema drift；把猜測寫成 fact | raw source 不可被 summary 取代 |
| extraction | regex、parser、AST、metadata、tool receipts | 非結構化文本的 event/fact/procedure 候選 | omission／hallucinated fact | 每個 derived item 有 source span、extractor revision |
| retrieval & routing | lexical/vector/time/entity filters、ACL、budget | query expansion、task relevance、diversity | retrieval hit 但取錯版本；overspecification | 回傳多候選及 provenance，不只一段摘要 |
| reconciliation／conflict | temporal DB、authority rules、three-way diff | 含義是否矛盾、哪個 evidence 可共同成立 | reader 選錯 truth；過早合併 | conflict 顯式保留，必要時升級 human |
| consolidation | dedupe、rollup、index compaction、Git GC policy | 跨 episode 提煉 procedure／pattern | lossy compression | derived consolidation 可重建、可失效 |
| update／forgetting | TTL、tombstone、revocation、retention policy | 判斷「是否仍有用」 | stale memory 被召回；假 forget | canonical event 不改寫；visibility/index 可撤銷 |
| provenance | source IDs、hash chain、model/version、timestamps | source quality interpretation | citation laundering | 每次 packet 可反查 raw source |
| context assembly | hard token budget、schemas、packet validation、dedupe | relevance ordering、compression、uncertainty summary | 關鍵 constraint 被壓縮掉 | 必含 goal、constraints、source pointers、open conflicts |
| security & poisoning recovery | trust domains、quarantine、least privilege、rollback、re-index | 判斷內容是否惡意／不可信 | prompt injection 成為持久 memory | untrusted content 永不取得控制權；能從 raw safe snapshot 重建 |

### 2.3 影響 Dexinode 決策最大的十項 memory 一手研究

| Evidence | 等級 | 真正測量的 contract | Backbone／context／harness | 成本與主要數字 | 正面證據 | 負面證據／不可外推處 |
|---|---:|---|---|---|---|---|
| [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/html/2606.24775v1) | A | 12 memory systems + 2 baselines，5 workloads／11 datasets；包含 temporal、multi-hop、task success | 依系統原生設計，並以 long-context／RAG baseline 對照；建置、查詢與回答分段計時 | DB-Bench long-context EM 48.20；MemoChat task success 55.40；structured systems 可有 orders-of-magnitude latency | 沒有單一 architecture 全勝；raw long-context 在 time-dependent tasks 常勝 | graph 單跳強但 temporal 弱；append-only 會退化；compression 與細粒度 extraction 都可能害 multi-hop |
| [MemoryAgentBench](https://arxiv.org/html/2507.05257v4) | A | 2,071 questions；accurate retrieval、test-time learning、long-range understanding、selective forgetting | 103K–1.44M context；RAG／commercial memory 多以 GPT-4o-mini 為回答 backbone | indexing cost 未納入主表；以 LLM judge／QA evaluator 為主 | 將「忘記」與 test-time learning 納入 | 所有現有系統均未同時通過四能力；RAG 有時低於 backbone；不是 action benchmark |
| [LongMemEval](https://arxiv.org/abs/2410.10813) | A | 500 curated long-conversation QA；五種 long-term memory ability | indexing→retrieval→reader decomposition；長期交互 | sustained interaction 約 30% accuracy drop | 把錯誤分解到 retrieval 與 reader | 仍主要是 conversational recall；不代表 project execution |
| [LongMemEval-V2](https://arxiv.org/html/2605.12493v1) | A | 451 cases；static／dynamic／workflow／gotcha／premise awareness；最高 500 trajectories／115M tokens | 固定 reader Qwen3.5-9B；RAG controller Qwen3.5-9B + Qwen3-Embedding-8B；coding controller Codex 0.117 + GPT-5.4-mini xhigh | strongest RAG 48.5；off-the-shelf coding 69.3；AgentRunbook-C 72.5；RAG 約 26s，coding 約 177–186s | executable memory controller 顯著高於傳統 RAG；可測 latency | 強 controller／remote backbone 依賴；不是證明小模型獨立完成。Oracle trajectories：Qwen reader 59.6、GPT reader 65.3；整理成 slices+notes 才 82.5/86.3，顯示 reader reconciliation gap |
| [Mem2ActBench](https://arxiv.org/html/2601.19935v1) | A | 400 tool-use tasks／2,029 sessions；91.3% human-confirmed memory-dependent | controlled Qwen2.5 7B／32B／72B、BGE-M3；ground-truth tool 已提供 | A-MEM F1 30.99／33.72／35.93；最佳 passive 約 30.7 vs oracle 53.8 | 將 memory 連到 tool argument grounding；清楚顯示 scaling effect | 不測 tool selection／真實 execution；資料生成依賴 Qwen3-Next-80B-A3B、Kimi-K2-Thinking；仍有 >23 point oracle gap |
| [MemoryArena](https://arxiv.org/abs/2602.16313) | B | human-crafted、跨 session、相依的 web navigation／planning／search／formal reasoning | 多種 memory agents；以實際 task outcomes 為核心 | 論文報告在 LoCoMo 飽和的系統仍於 action tasks 顯著失敗；完整 budget 不宜跨系統直比 | 證明 conversational recall 與 action memory 可分離 | 新 preprint；環境與 harness 複雜，尚無穩定跨版本比較 |
| [LightMem](https://arxiv.org/html/2604.07798v1) | B | lightweight online retrieval + offline consolidation；LoCoMo、DialSim | online default quantized Llama-3.2-1B-Instruct；亦測 Qwen2.5-1.5B；MiniLM embeddings；2K LoRA samples | LoCoMo avg +2.5 F1；median retrieval 83ms、end-to-end 581ms | 直接顯示 1B-class SLM 可做部分 online memory | offline consolidation 使用 large-context LLM；benchmarks 仍偏 conversational，非 project action |
| [DimMem](https://arxiv.org/abs/2605.15759) | B | typed atomic facts：time／location／reason／purpose／keyword | fine-tuned Qwen3-4B extractor；與強 cloud-backed memory 比較 | LoCoMo 81.43、LongMemEval-S 78.20；token cost -24% | 4B extractor 可勝 LightMem + GPT-4.1-mini 組合，為 SLM memory-manager 的直接訊號 | vendor／作者 preprint；主要仍是 QA，沒有 end-to-end workflow 與 poisoning recovery |
| [MemMachine](https://arxiv.org/html/2604.04853v1) | B/C | raw conversational episodes + sentence indexes；避免例行 LLM extraction | retrieval-centered；保存 surrounding context／raw provenance | 作者報告對 Mem0 約 80% fewer tokens 等結果；完整 cross-harness 欄位不足 | architecture 上支持保留 raw source 與 provenance | 數字屬作者系統比較，且仍偏 conversational；不可作 production latency 保證 |
| [MemSecBench](https://arxiv.org/html/2607.27080v1) | A | Write–Execute–Forget；310 cases／48 contexts；24 configurations | 2 harnesses × 4 backends（Native／Mem0／Mem0-Graph／A-MEM）× 3 LLMs（DeepSeek-V4-Pro／MiniMax-M3／GPT-5.5） | malicious memory persistence 84.2%；full attack 50.3%；conditioned selective repair 56.1%；judge audit 約 91% | 首個直接量 memory poisoning persistence／forget recovery 的 controlled signal | 修復遠未可靠；使用 frontier backbones，不能推論 SLM 能安全管理 memory |

上表任何未同時公開 exact prompt、tool interface、step/token budget、retry/sampling、environment revision與 evaluator implementation 的數字均為 **harness-confounded**。尤其 LoCoMo／LongMemEval 類 QA、Mem2Act 的 ground-truth-tool setup、LLM-judge task success不可互相比成單一 memory ranking。

### 2.4 核心問題逐項回答

1. **Memory 是否改善 downstream action success？** `PARTIALLY SUPPORTED`。MemoryArena 與 Mem2ActBench 把題目推向 action；但 Mem2Act 已固定正確 tool，LongMemEval 系列仍以回答為主。現有證據不足以宣稱 project/workflow action success 已被解決。
2. **Memory manager 是否暗中依賴大型遠端模型？** 經常是。MemoryAgentBench 的關鍵比較多固定 GPT-4o-mini；LongMemEval-V2 的 coding controller 是 Codex + GPT-5.4-mini；LightMem offline consolidation 仍用大型模型。這構成 architecture circularity 的主要風險。
3. **raw source 還是 summary？** 最可靠的證據支持 raw source + version + derived views。只存 summary 使撤銷、衝突、poison recovery 與重新解釋失去基礎。
4. **更新／撤銷／矛盾／stale memory？** 研究尚無單一成熟答案。可確定的是：temporal validity、supersession、provenance 與 conflict surfacing 必須由 deterministic storage 支援；不能期待 reader 自行猜對最新狀態。
5. **compression 的 loss／P95 latency／token／維護成本？** loss 與 latency 可測，但公開資料很少同時報 P95、建置與 query。Agent-native comparison 顯示 structured memory latency 可增數個數量級；LongMemEval-V2 顯示 agentic memory quality 上升時 latency 也由約 26s 增至 177s 級。Mem0 的 >90% token、91% P95 改善是 vendor-authored `C`，不作 major conclusion。
6. **SLM 管理 memory？** `PARTIALLY SUPPORTED`，且限定於 extraction、classification、online retrieval／disclosure 等 bounded roles。沒有 1B–4B SLM 獨立承擔跨 project reconciliation、security 與 action success 的可信證據。
7. **哪些可 deterministic？** storage、version、transactions、ACL、parsing、AST、timestamps、dedupe、TTL、budget、provenance、packet schema、tool receipts、rollback。
8. **哪些仍需 judgment？** 非結構化 semantic typing、task relevance、矛盾含義、compression、是否需 clarification、是否應 escalation；其輸出必須可追溯且可覆核。
9. **benchmark 偏 recall 還是 action？** 主流仍偏 conversational recall。MemoryArena、Mem2Act、LongMemEval-V2 workflow slices 是重要進展，但沒有一套涵蓋 full project state + tool execution + human burden 的成熟標準。
10. **retrieval 成功但 reader reconciliation 失敗？** 已有直接證據但尚無通用比例。LongMemEval-V2 的 oracle trajectories 對固定 readers 仍只有 59.6／65.3，而重新組織成 slices+notes 後 82.5／86.3；同一 evidence 的 representation／reader 即可造成 20+ point 差異。

## 3. Track B — Loop、Harness、Workflow 與 Graph Engineering

### 3.1 方法分類與 evidence matrix

| 類型 | 相對 direct／fixed loop 的證據 | 主要成本／依賴 | termination／error risk | Dexinode 預設立場 |
|---|---|---|---|---|
| simple fixed pipeline | Agentless 在 SWE-bench Lite 以 localization→repair→validation 達 32%，約 $0.70／issue（當時價格） | 多 patch sampling、generated tests、reranking；不等於 one-shot | 固定邊界易審核，但步驟錯誤會傳遞 | bounded specialist 的優先 baseline |
| ReAct／observe-think-act | ReAct 在 ALFWorld／WebShop 對先前 baseline +34／+10 absolute | PaLM-540B／GPT-3；narrow APIs；多步 token／latency | observation 誤讀、tool loop、budget exhaustion | 只有環境回饋能改變決策時使用 |
| plan-and-execute | 有助長 horizon 分工，但 controlled general advantage 不穩定 | plan 先錯會擴大；replan cost | stale plan、不可逆 action | plan 為可撤銷 artifact；逐步 local validation |
| verifier／test-feedback loop | CRITIC 與 coding tests 支持外部 feedback | 依賴高 precision verifier／可重跑環境 | noisy verifier 會破壞正確解；fixed retry 浪費 | 可信 verifier 存在時的主要 loop |
| reflection／self-repair | Self-Refine 在 7 tasks 報告平均約 +20 absolute | 多次同模型生成與 feedback | intrinsic self-correction 常退化；假確信 | 不作預設；需獨立 evidence 或 verifier |
| tree／graph search | AFlow／ADAS／AgentSquare 在其 validation/eval 上有 gains | workflow search、meta-model、候選評估成本 | validation overfit、branch explosion | 只有高價值／可驗證 task 才可能成立 |
| deterministic state machine／DAG | LoopsBench 以 DAG 顯示 planning fidelity／regression；OneFlow 顯示簡化可保留效能 | workflow authoring／state schema | schema 漏掉例外，但可 audit／resume | control plane 的預設骨架 |
| automatically searched workflow | AFlow avg +5.7%；AgentSquare +17.2% vs reported designs | 通常需 GPT-4o-class meta-agent；反覆 validation | Harness Evolution held-out 僅 +0.6 avg、無顯著改善 | research option，不是 v0.1 production default |
| homogeneous multi-agent | 多樣 sample 可增加 pass@k；但 OneFlow 可由單 agent sequential simulation | 重複 context、coordination、false consensus | one false testimony 可造成 truth recovery collapse | 先用單 agent + explicit roles／parallel samples 模擬 |
| heterogeneous multi-model workflow | 不同 specialist 的 complementarity 概念成立；MAI-UI DCC 有 local/cloud 分工訊號 | interface conversion、handoff loss、per-model harness tuning | 弱成員污染、judge偏誤、跨模型 context loss | 僅在 distinct capability／cost／trust boundary 時增加 |

### 3.2 主要 loop／harness 研究與反證

| Evidence | 等級 | Model／harness／context／tools | Budget／sampling／environment／evaluator | 結果 | Confound／解讀 |
|---|---:|---|---|---|---|
| [ReAct](https://arxiv.org/abs/2210.03629) | A | PaLM-540B／GPT-3；interleaved reasoning/action；Wikipedia API、ALFWorld、WebShop；few-shot prompt | paper-specific step caps；無現代 agent cost；環境 success／EM evaluator | ALFWorld、WebShop 相對既有 baseline +34、+10 absolute | backbone 極大、tools 窄；證明 observation loop 可有用，不證明任意 agent graph |
| [SWE-agent](https://arxiv.org/abs/2405.15793) | A | LM + custom Agent-Computer Interface；repository shell/editor | SWE-bench revision／test evaluator；pass@1；原報告 budget 依 model setup | SWE-bench 12.5% pass@1；HumanEvalFix 87.7% | interface 是 intervention 本身；不能當裸模型分數 |
| [Agentless](https://arxiv.org/html/2407.01489v2) | A | fixed localization→repair→validation；hierarchical repo retrieval；LLM samples patches | multiple patches + generated tests + reranking；SWE-bench Lite environment；tests | 96／300 = 32%，約 $0.70／issue（當時） | simple pipeline 的強反證，但仍有 sampling／reranking，且價格會變 |
| [ADAS](https://arxiv.org/abs/2408.08435) | A | meta-agent 以 code 建立 agent；多 domain／model transfer | search budget 與 evaluator 依 benchmark；meta-model 依賴 | 作者報告跨 domain／model 的 discovered agents 優於 hand-designed | meta-search cost 與 validation coupling；不可作 resident loop 的低成本證據 |
| [AFlow](https://arxiv.org/abs/2410.10762) | A | MCTS 搜 code workflows；6 datasets | 20% validation；最多 20 iterations；benchmark evaluators | avg +5.7%；小模型在作者成本估計以 GPT-4o 4.55% dollar cost 競爭 | search/eval coupling；價格非穩定；沒有證明複雜 graph 必要 |
| [AgentSquare](https://arxiv.org/html/2410.06153v1) | A | GPT-3.5-turbo-0125／GPT-4o；search planning/reasoning/tool/memory modules；6 agent tasks | 同 few-shot count；search + performance predictor；environment scores | 相對作者選定 human designs +17.2% | 無充分 strong simple baseline；search cost／predictor confounded |
| [OneFlow](https://arxiv.org/html/2601.12307v1) | A | GPT-4o-mini 與 Qwen3-8B；同一模型依序模擬 homogeneous roles；KV reuse；7 benchmarks | Qwen vLLM 16K；相同 workflow family；task evaluators | GPT-4o-mini single-agent 常 match/slightly exceed MAS；HumanEval token 488+205 vs AFlow 2863+1880；Qwen OneFlow latency約 4.83s vs AFlow約 53.5s | heterogeneous pilot 很小；不能消除真正不同工具／模型的價值，但反駁「多 agent 身分本身必要」 |
| [LoopsBench](https://arxiv.org/html/2608.00267v1) | A | 112 tasks／5,300 units／DAG；多 coding harness + frontier models | 2–24h/task；Claude max iterations 10K；部分 cost uncapped；repo tests | strongest configuration 25%；fixed GPT-5.4：Codex continuation 18.75、Claude Code 17.86、OpenHands 9.82、SWE-agent 8.93 | budget 遠超 Dexinode envelope；最有價值的是 planning fidelity／regression／resume 指標，不是絕對分數 |
| [SWE-Effi](https://arxiv.org/html/2509.09853v1) | A | 5 scaffolds × GPT-4o-mini／Llama-3.3-70B／Qwen3-32B；SWE-bench | token、time、cost、resolved；repo tests | Agentless+Qwen3-32B resolved 48 vs OpenHands 34／SWE-agent 28；unresolved 可耗 >4× successful | 強烈 model×scaffold coupling；跨 harness 排名不可移植 |
| [Scaffold Effect](https://arxiv.org/html/2607.22585v1) | A | 2 models × 3 harnesses × 50 Terminal-Bench Pro = 300 trials | 同 benchmark；token／solved／failure fingerprints | 每 solved token 可差 40×；pass-rate 差 0–8pp，多數 CI 含 0 | scaffold 改善不只反映 capability；應登錄 harness-model pair |
| [Harness Evolution](https://arxiv.org/html/2607.12227v1) | A | 3 frontier models；相同 initial harness；Terminal-Bench 2.1；direct／parallel／sequential／evolution | K=5；128K；high reasoning；2 runs；45 train／10 val／34 held-out | 無 tests 時 direct 68.2、parallel 72.3、evolution 67.4；held-out evolution 僅 +0.6 avg、無顯著 gain | 本輪最直接「searched workflow overfits／更簡單同樣好」反證 |
| [Self-Refine](https://papers.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html) + [LLMs Cannot Self-Correct](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b6b6436d6c5ecf59bbf745c37-Abstract-Conference.html) | A | 同模型 feedback→refine；7 tasks；對照 intrinsic correction studies | task-specific round cap/evaluator；無外部 ground-truth feedback的 setting另測 | Self-Refine avg約 +20 absolute；intrinsic reasoning correction 常下降 | 結論不是 reflection 永遠無效，而是必須區分外部訊號與模型自評 |
| [CRITIC](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fef126cefd7e00292f7a3f4ed815f6f8-Abstract-Conference.html) | A | LLM + search／code／calculator等外部 tools | tool-feedback iterations；task evaluators | 外部互動 feedback 提升修正 | verifier precision、tool availability 決定收益；無 verifier 不可類推 |
| [False-consensus study](https://arxiv.org/abs/2608.03421) | A | 3 homogeneous systems；120 five-agent tasks；注入一個 false testimony | controlled communication rounds；truth recovery evaluator | truth recovery 72.50%→14.17%，deceiver 離開後仍持續 | multi-agent 多數並非獨立證據；shared-context contamination 會放大錯誤 |

以上任何缺少 exact prompt、step cap、temperature、environment commit 或 evaluator implementation 的分數均視為 **harness-confounded**；表中數字只在各自 configuration 內解讀，不作跨研究排行榜。

### 3.3 Loop engineering 的可採與不可採結論

- `ESTABLISHED`：environment interface、tool schema、context policy 與 termination policy 足以顯著改變結果；能力登錄必須綁定 harness revision。
- `ESTABLISHED`：更複雜 workflow 不保證更好；固定 pipeline、parallel candidates 或單 agent sequential roles 是必要 baseline。
- `PARTIALLY SUPPORTED`：test/verifier-feedback loop 對可執行、可判定任務有價值；對 open-ended judge task 的可靠性較低。
- `CONTRADICTED`：只靠模型 intrinsic reflection 就能一般性 self-correct。
- `OPEN`：automatically searched workflow 能否在 held-out real workflows、固定 total budget 下跨模型轉移。
- `OPEN`：heterogeneous small specialists 的 interface cost 是否低於真實 capability complementarity；OneFlow 只否定「同模型換身份」的必要性。

## 4. Track D — Hybrid Local／Remote Architecture Evidence

### 4.1 Architecture evidence matrix

| 方法／系統 | 等級 | Local side 真正保留 | Remote side 真正取得／回傳 | 效果與成本 | 限制／failure mode |
|---|---:|---|---|---|---|
| [PrivScope](https://arxiv.org/html/2605.16630v1) | B | persistent state、identifier binding、payload unit extraction、necessity／abstraction（3B default） | task-minimized medical provider-search payload；回候選資訊 | 100 workflows、3 cloud LLMs；profile leakage 17.7%→0；attacker recovery 64.3%→23.1%；Llama-3.2-3B mediation 3.13s | 單一 medical-booking domain、合成 prompt；三-judge majority；Claude utility 很低；仍有 current-request verbatim leakage；step/retry與environment不完整，**harness-confounded** |
| [PlanTwin](https://arxiv.org/html/2603.18377v1) | B | raw state、heuristic／optional SLM extraction、schema projection、policy、execution、output sanitization、cumulative disclosure | typed abstract graph + capability catalog；回 declarative plan | 60 tasks／10 domains／4 cloud planners；SND=1.0，3/4 planners PQS>0.79，utility loss <2.2%；deterministic projection <1ms | tasks／PQS 為作者設計；optional SLM extraction 13–34s；full e2e 45–120s；結構仍可 re-identify；budget/retry不完整，**harness-confounded** |
| [CaMeL](https://arxiv.org/abs/2503.18813) | A/B | trusted query 的 control/data flow、capabilities、policy enforcement | LLM 處理不可信 data，但不能改 program flow／未授權 flow | AgentDojo 67% tasks 兼具 task solution 與可證 security | 需可抽出 control/data flow；coverage sacrifice 33%；open-ended task policy authoring 未解 |
| [MemSecBench](https://arxiv.org/html/2607.27080v1) | A | memory backends／forget-repair mechanisms | frontier models read persistent memory | 24 configs；malicious persistence 84.2%、full attack 50.3% | 表明 local memory 並不天然安全；prompt injection 可跨 session 持續 |
| [MAI-UI DCC](https://arxiv.org/html/2512.22047v1) | C | MAI-UI-2B 執行較簡單 GUI steps、保留 local observation | 32B cloud 處理較難 steps；回 action／summary | AndroidWorld 相對提升 33.4%；42.7% steps local、40.5% tasks 全 local、cloud calls -42.7%；error summary +6.9 | vendor benchmark；router／privacy 只小型分析；無 device latency/energy；step/retry不完整，**harness-confounded**；不是 general Resident Core proof |
| [Apple Private Cloud Compute](https://security.apple.com/blog/private-cloud-compute/) | C | device request construction、attestation validation；on-device 優先 | attested stateless node 僅收 inference request；不保留 user data | production security architecture：stateless、no privileged runtime access、non-targetability、verifiable transparency | 不公開 task-scoped semantic minimization效果；是 confidential remote execution，不證明 local model capability |
| [METR experienced OSS developer RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | A | human 對自己 mature repo 的完整 context／review | frontier coding assistance（主要 Cursor + Claude 3.5/3.7） | 16 developers、246 real issues；AI allowed 反而 19% slower；使用者仍以為快 20% | early-2025 snapshot、特定 experienced cohort；不證明所有 workflow 都變慢，但否定以 benchmark 分數代理人工負擔 |

### 4.2 十個 architecture 問題的 evidence-based 回答

1. **可信本地 control plane 必須做什麼？** Workspace、canonical memory、identity/restoration map、credentials、ACL/capability、tool execution、budget/termination、artifact version、audit、rollback。CaMeL／PlanTwin 顯示這些是 trust boundary，不是模型偏好。
2. **哪些工作需要 Local Resident Model？** 對自然語言 intent 的有限澄清、task decomposition、semantic context relevance、可逆 planning、讀取 verifier 結果與整合。證據只支持 bounded working set，尚未支持無界 autonomous core。
3. **哪些可交 Local Specialist？** 明確 schema／action space／verifier 的 function calling、GUI next-action、code patch、search、critic/reranker；詳見 model landscape。正確拒答／升級是成功路徑。
4. **何時升級 Remote？** local uncertainty 高、packet 超出 envelope、跨域整合、沒有 local capability、local verifier 反覆否決、或需要 frontier search/reasoning。這是責任邊界，非新的 routing algorithm。
5. **Remote 回什麼？** 優先回 declarative recommendation、bounded plan、candidate artifact 或 patch；不持有 credentials，不直接執行不可逆 tool。所有 artifact 必須在本地解析、掃描、測試、policy-check。
6. **本地如何驗證／整合／還原？** schema validation→static/deterministic check→sandbox/test→policy/permission→pseudonym restoration→diff/receipt→必要時 human approval。LLM judge 只可補充，不可成為不可逆 action 唯一 verifier。
7. **若每步都需 remote，本地模型還剩什麼？** 若 local model 只做轉發，其推理價值近乎消失；仍有 trusted control plane 價值，但那會支持 `PIVOT TO LOCAL CONTROL PLANE`，不是 Resident Core thesis。現有 specialist signals 使此結論尚未成立。
8. **local memory/context 能否避免完整 history 上傳？** `PARTIALLY SUPPORTED`。PrivScope／PlanTwin 顯示 task packet minimization 可保留部分 utility；但跨真實 project、長期多回合的 disclosure composition 尚未建立。
9. **minimum disclosure 與 persistent injection 證據？** task-scoped abstraction 有 B-grade 正面訊號；MemSecBench 有 A-grade負面訊號。最小揭露不等於安全，還需 trust labels、capabilities、data/control-flow separation 與可重建 memory。
10. **human burden／latency／fallback／failure loss 可量測嗎？** 原則上可以：active human minutes、clarification/review/edit time、end-to-end latency P50/P95、local/remote calls、retry、abstention、fallback recovery、reverted actions、uncaught severe loss。METR 證明人時必須直接量，而不能由 pass rate 推估。

## 5. v0.1 working assumptions 的可量測性

這裡只檢查「能否量」，不更改或認可數值。

| Working assumption | 可操作化指標 | 文獻是否支持可量測 | 是否有 threshold 共識 |
|---|---|---|---|
| 約 70% in-scope cases 不改或一次小改完成 | first-pass accepted；one-small-edit accepted；contract-scoped success；Wilson／bootstrap CI | 是；coding／GUI／tool benchmarks可記 pass@1 與 edit count | 否；70% 是本專案 screening line |
| active human time 約 -30% | screen/task telemetry；clarification、review、repair、waiting 分開 | 是；METR RCT 直接量 task time | 否；甚至存在 19% slowdown 的反例 |
| inference variable cost 約 -50% | local energy/latency amortization、remote input/output tokens、call/retry count；固定時點價格 | 是，但價格與硬體會變；應同時報非貨幣 units | 否；50% 非共識 |
| 不得有未攔截重大不可逆錯誤 | severity taxonomy；irreversible action receipt；prevented／escaped incidents | 是；需 deterministic policy + human checkpoint | 「零」可作 safety invariant，但什麼算重大需 task contract 定義 |
| 使用者看過 failure modes 後仍願再用 | post-task willingness-to-reuse、actual repeat use、calibration survey | 是，HCI 方法成熟 | 否；需 domain／user population 校準 |
| 8K–16K specialist、16K–32K resident、>64K 重檢索 | actual packet tokens、compression loss、retrieval recall、reader accuracy、P95 latency | 是；LongMemEval-V2 可分離 retrieval/reader | 沒有通用 envelope 共識；保留為 v0.1 assumption |

## 6. 對 architecture hypothesis 的約束

1. canonical memory 不能是 LLM summary store；必須是 versioned raw evidence + typed derived views。
2. context manager 不是單一模型角色：deterministic filtering／ACL／budget 與 semantic relevance／compression 必須拆開。
3. Resident Core 不應「思考所有事情」；它在 bounded packet 上做 judgment，control plane 保持 authority。
4. verifier-first：能以 compiler、test、schema、policy、database constraint 判定者，不用 reflection 取代。
5. minimal loop-first：fixed pipeline／state machine 是 baseline；增加 agent、branch 或 search 必須以相同 model、context、tool、total budget 證明 marginal gain。
6. remote 是 untrusted advisor/artifact producer；不可直接擁有 tool credentials、restoration map 或 canonical memory write authority。
7. poisoning recovery 是 architecture invariant：quarantine、source revocation、derived-index rebuild、snapshot rollback 與 audit 缺一不可。
8. 完整配置的指標可量測，但現有文獻尚未把 quality、active human time、P95 latency、privacy、variable cost 與 severe failure 合在同一真實 workflow 評估。

## 7. Evidence gaps（不轉換成新 Gate）

- 缺少 4B–8B resident model 在 versioned project memory、bounded packet、deterministic tools／verifier、remote fallback 下的 end-to-end controlled evidence。
- 缺少 memory retrieval hit 後，reader reconciliation failure 的跨 model／跨 task 分解數據。
- 缺少同時報 memory build、P50/P95 query、compression loss、token、maintenance/recovery effort 的公開研究。
- 缺少 task-scoped disclosure 在真實 multi-project、multi-turn、adversarial memory 條件下的研究。
- 缺少固定 total compute／latency 下，heterogeneous small-model workflow 對 strong single-agent／fixed-pipeline 的 controlled comparison。
- 缺少把 human active time、review burden、fallback loss 與 user reuse intent 納入同一 agent configuration 的公開資料。
