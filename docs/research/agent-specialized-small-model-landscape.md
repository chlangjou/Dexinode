# Agent-Specialized Small-Model Landscape

- 研究截止：2026-08-10（Asia/Taipei）
- 文件用途：Dexinode hybrid resident-agent architecture hypothesis 的官方 metadata／一手研究盤點
- 非用途：模型採購建議、單一總排行榜、正式候選凍結、FIM HOLD 重審
- Coverage：非窮舉 evidence landscape；不是候選 registry，也不代表已選定任何 checkpoint

## 0. 口徑與查核規則

本文件嚴格使用四層：

- **Edge-small**：`total parameters < 1B`
- **Absolute-small**：`1B <= total parameters <= 8B`
- **Active-small MoE**：`active parameters <= 8B` 且 `total parameters > 8B`；必須同報 total／active
- **Remote／frontier reference**：proprietary API 或大型 open-weight；不得作 Local Model viability 證據

模型名稱中的 `2B`、`8B`、`35B` 只是名稱，優先以 config／safetensors metadata／technical report 交叉核對。若 official sources 自相矛盾，保留衝突而不自行選一個「較好看」的數字。`revision` 欄優先列 immutable hash；官方頁未公開 hash 時，列 named release 或「main snapshot 2026-08-10」，並標成 metadata gap。未下載任何權重，也未執行 inference。

分類：`Resident Core candidate`、`Local Specialist`、`Remote Reference`、`Ineligible`。`Local Specialist` 只表示值得保留研究，不表示已達 production quality。

## 1. 名稱與層級核實摘要

| Prompt seed／常見名稱 | 截止日核實結果 | 層級影響 |
|---|---|---|
| FunctionGemma 270M | 存在；exact ID `google/functiongemma-270m-it` | Edge-small |
| TinyAgent 1.1B／7B | 存在；exact IDs `squeeze-ai-lab/TinyAgent-1.1B`、`squeeze-ai-lab/TinyAgent-7B` | Absolute-small |
| xLAM function-calling | 存在；本輪以 xLAM-2 的 1B／3B／8B artifact 為主 | Absolute-small；non-commercial license |
| Hammer | 存在；本輪核實 Hammer 2.1 0.5B／1.5B／3B／7B | 0.5B Edge；其餘 Absolute；Qwen Research license |
| Fara-7B | 存在但已非最新；current family 是 `microsoft/Fara1.5-4B`／`Fara1.5-9B` | 4B 名稱 artifact 約 5B，仍 Absolute；9B Ineligible |
| AgentCPM-GUI-8B | 存在；exact ID `openbmb/AgentCPM-GUI` | 8B 邊界；官方只報 8B，保留 exact instantiated count gap |
| MAI-UI 2B／8B | IDs 存在；`MAI-UI-8B` artifact metadata 約 9B | 2B Absolute；8B 名稱不得作 Absolute-small 證據 |
| current Qwen 3.x dense local | `Qwen/Qwen3.5-0.8B`、`Qwen3.5-2B`、`Qwen3.5-4B`、`Qwen3.5-9B` 於 2026-03-02 公開；Qwen3.6 dense current release是27B | 0.8B Edge；2B與4B artifact（HF顯示5B）為 Absolute；9B／27B Ineligible作Absolute；不能把hosted alias當open local |
| Qwen3-Coder-Next | 存在；80B total／3B active | Active-small MoE，不是 Absolute-small |
| Qwen3.6-35B-A3B | 存在；paper/card 35B／3B，artifact metadata 約 36B | Active-small MoE，不是 Absolute-small |
| DeepSeek-V4-Flash／Pro | 存在；Flash-0731 為 current named release，Pro 仍標 preview | 13B／49B active，兩者均不是 Active-small；Remote Reference |
| Qwen3.7／Qwen3.8 hosted | API aliases `qwen3.7-flash`、`qwen3.8-max` 存在 | Remote Reference；不得作 local viability |

## 2. 四層模型表

### 2.1 A — Edge-small

| Exact model ID | Revision／release | License／lineage | Params／type／native context | Specialization／task contract | Quantization與部署證據 | Evidence／classification |
|---|---|---|---|---|---|---|
| [`google/functiongemma-270m-it`](https://huggingface.co/google/functiongemma-270m-it) | gated `main` snapshot 2026-08-10；public release 2025-12-18；immutable SHA 在未接受 gate 前不可見 | Gemma Terms；Gemma 3 270M；可依條款 commercial use，需接受 gating | 270M dense；32K native | function selection／arguments；官方明示應針對 task fine-tune，不是 general chat | dynamic INT8；Samsung S25 Ultra CPU、LiteRT/XNNPACK 4 threads：model 288MB、peak RSS 551MB、decode 125.9 tok/s、TTFT 0.3s；量測用 512 prefill + 32 decode（表中 context 1,024），不是 32K | `D/C`；`Local Specialist`。唯一有可信手機實測的 edge candidate；BFCL／Mobile Actions 仍非完整執行 |
| [`MadeAgents/Hammer2.1-0.5b`](https://huggingface.co/MadeAgents/Hammer2.1-0.5b) | `main` snapshot；family release 2024-12-13、2025-06 更新；immutable SHA 未取得 | Qwen Research License；Qwen2.5-Coder-0.5B lineage；commercial eligibility 不清／受限 | 約 0.5B dense；32K family context | multi-turn／multi-step function calling、irrelevance，function masking training | official Google AI Edge integration；未報 device、RSS、latency、energy；quantized artifacts不等於部署測量 | `D/C`；`Ineligible` 作商用路徑，research-only `Local Specialist`；benchmark 主要在圖片且欄位不足 |
| [`Qwen/Qwen3.5-0.8B`](https://huggingface.co/Qwen/Qwen3.5-0.8B) | `main` snapshot 2026-08-10；official family release 2026-03-02；immutable SHA未擷取 | Apache-2.0；Qwen3.5 native multimodal dense family | 0.8B language model，HF總artifact仍列0.8B；dense + vision encoder；262,144 native | general multimodal model；million-agent-environment RL；native `qwen3_coder` tool parser | BF16 official；tp=1 serving recipe與community quantizations；無device RSS／latency／energy measurements | official BFCL-V4 25.3、TAU2-Bench 11.6；vendor `C`、harness-confounded。`Local Specialist` research baseline，不是可信 Resident Core |

**Edge-small 結論：** `PARTIALLY SUPPORTED`。FunctionGemma 證明 sub-1B 在明確 schema 下可於旗艦手機低延遲執行；Qwen3.5-0.8B 提供 general/native-tool metadata，但其 TAU2 signal低且無device測量。沒有證據支持 sub-1B Resident Core、長期 memory reconciliation 或 repository agent。

### 2.2 B — Absolute-small

| Exact model ID | Revision／release | License／base lineage | Params／type／native context | Specialization method／task contract | Quantization／hardware／latency evidence | Key evidence／known negatives／classification |
|---|---|---|---|---|---|---|
| [`squeeze-ai-lab/TinyAgent-1.1B`](https://huggingface.co/squeeze-ai-lab/TinyAgent-1.1B) | `c7271d8c24c010af5f50c27133a09f9c3b8fc138`；paper 2024-09；EMNLP 2024 demo | repo MIT；TinyLlama-1.1B-Instruct-32K；base terms亦適用 | 1.1B dense；32K | synthetic MacOS 16-function planning；80K train，ToolRAG retrieves function schemas | FP16：M3 MacBook 2.2GB／3.9s；4-bit 0.68GB／2.9s；paper test prompt約 1,397 tokens | plan-DAG success 80.06（ToolRAG）；只比 tool set／dependency graph，不執行工具、非真實 user distribution。`Local Specialist` |
| [`squeeze-ai-lab/TinyAgent-7B`](https://huggingface.co/squeeze-ai-lab/TinyAgent-7B) | HF tree short revision `682226e`（full hash未公開於擷取頁）；2024-09 | MIT repo；paper稱 Wizard-2-7B／artifact Mistral architecture；lineage metadata不一致 | 約 7B dense；context依 base，artifact未完整核實 | 同上 | FP16：M3 14.5GB／19.5s；4-bit 4.37GB／13.1s | plan-DAG success 84.95；仍非 end-to-end execution；`Local Specialist` |
| [`Qwen/Qwen3.5-2B`](https://huggingface.co/Qwen/Qwen3.5-2B) | current short revision `15852e8`（full hash未於tree頁顯示）；official release 2026-03-02 | Apache-2.0；Qwen3.5 native multimodal dense family | 2B total（card與HF metadata一致）；dense + vision encoder；262,144 native | general model；million-agent-environment RL；native multi-turn tool parser；card定位prototyping／task fine-tuning | BF16 artifact 4.57GB；tp=1 serving；community quantizations但無audited device latency／energy | official BFCL-V4 43.6、TAU2-Bench 48.8；card明示thinking mode較易不終止。`Resident Core candidate` only at `C/D` metadata level |
| [`Qwen/Qwen3.5-4B`](https://huggingface.co/Qwen/Qwen3.5-4B) | current short revision `851bf6e`；official release 2026-03-02 | Apache-2.0；Qwen3.5 native multimodal dense family | language model 4B；HF instantiated artifact顯示5B total；dense + vision encoder；262,144 native、可延約1.01M | general multimodal agent model；million-agent-environment RL；native tool calling | BF16 artifact 9.34GB；tp=1 serving；無實測device RSS／P95／energy；card建議 complex thinking維持至少128K context | official BFCL-V4 50.3、TAU2-Bench 79.9、VITA-Bench 22.0、DeepPlanning 17.6；`Resident Core candidate`，但全為vendor harness且16–32K效能未驗證 |
| [`Salesforce/xLAM-2-1b-fc-r`](https://huggingface.co/Salesforce/xLAM-2-1b-fc-r) | HF short revision `6870fcf`；family released 2025-03-26 | CC-BY-NC-4.0；Qwen2.5 family | paper label 1B；BF16 artifact約 3.09GB，暗示約 1.5B；dense；32K，YaRN可延伸128K | APIGen-MT filtered behavioral cloning；synthetic multi-turn tool trajectories | BF16 official；無端側硬體、RSS、energy、latency；未審核 quantized deployment | BFCL-v3 58.90 overall；τ-bench 21.8 pass@1。`Local Specialist`，但 non-commercial |
| [`Salesforce/xLAM-2-3b-fc-r`](https://huggingface.co/Salesforce/xLAM-2-3b-fc-r) | `main` snapshot 2026-08-10；release 2025-03-26；immutable hash未擷取 | CC-BY-NC-4.0；Qwen2.5 family | 約 3B dense；32K／YaRN 128K | 同上 | 無 audited device evidence | BFCL-v3 65.11；τ-bench 38.2。工具類中相對強的 end-to-end signal，但 license／部署未解；`Local Specialist` |
| [`Salesforce/Llama-xLAM-2-8b-fc-r`](https://huggingface.co/Salesforce/Llama-xLAM-2-8b-fc-r) | `main` snapshot；release 2025-03-26；immutable hash未擷取 | CC-BY-NC-4.0 + Meta Llama terms；Llama 3.1 8B family | 約 8B dense；128K | 同上 | 無 audited device evidence | BFCL-v3 72.83；τ-bench 46.7。`Local Specialist`，non-commercial；不當 Resident Core 證據 |
| [`MadeAgents/Hammer2.1-1.5b`](https://huggingface.co/MadeAgents/Hammer2.1-1.5b)、[`MadeAgents/Hammer2.1-3b`](https://huggingface.co/MadeAgents/Hammer2.1-3b)、[`MadeAgents/Hammer2.1-7b`](https://huggingface.co/MadeAgents/Hammer2.1-7b) | 3B short revision `702ce42`；其餘`main` snapshot；family release 2024-12-13／2025-06 update | Qwen Research License；Qwen2.5-Coder | 1.5B／3B／7B dense；32K family context | function masking、multi-step／multi-turn／irrelevance | model cards／edge integrations；沒有可審核 device numbers | official BFCL 圖表缺 prompt、budget、retries、environment；`Ineligible` 商用，research-only `Local Specialist` |
| [`microsoft/Fara1.5-4B`](https://huggingface.co/microsoft/Fara1.5-4B) | captured revision `3a80b97b41797b8cfc92dd268fcc33601f1ec9a1`（2026-07-27）；repo release note 2026-07-22，card date與repo另有差異 | MIT；Qwen3.5-4B multimodal lineage | 名稱 4B；HF instantiated metadata約 5B；dense VLM；262,144 | FaraGen1.5 SFT；web GUI action；critical-point ask／pause／sandbox | BF16；A6000／A100／H100／B200 tested；無 consumer device、RSS、latency、energy | WebVoyager 80.8、Online-Mind2Web 57.3、WebTailBench 27.4；dynamic web + judge，run variance／prompt injection／error accumulation。`Local Specialist`，deployment evidence incomplete |
| [`openbmb/AgentCPM-GUI`](https://huggingface.co/openbmb/AgentCPM-GUI) | `433b33feda9fed1e13b509cfd65d73f0a3fc4dff`；release 2025-05-13；report update 2025-06-17 | Apache-2.0；MiniCPM-V-2_6 | official 8B dense multimodal；exact instantiated count未在 card 分解，故為邊界 provisional；native context未明確報告 | grounding pretraining + SFT + GRPO/RFT；single next GUI action；可輸出 impossible／interrupt／need_feedback | BF16，artifact約16.2GB；README只示範 CUDA；無手機 latency／energy；OOM建議 max 2,048 | AC-low EM 90.20、AC-high 69.17 等為 static next-action，不實際執行。`Local Specialist`；若 exact total >8B 則改列 Ineligible |
| [`Tongyi-MAI/MAI-UI-2B`](https://huggingface.co/Tongyi-MAI/MAI-UI-2B) | `503050934809558c8dfd2ddedaf9621fa74ac2de`；paper 2025-12 | Apache-2.0；Qwen3-VL | 2B dense multimodal；262,144 | GUI SFT/RL；action space含 GUI、`ask_user`、MCP；另有 dynamic cloud collaboration | BF16，artifact約4.27GB；無實機 RSS／latency／energy | AndroidWorld 49.1% end-to-end；2B 是最直接 absolute-small GUI signal之一。無端側部署測量；`Local Specialist` |
| [`openbmb/AgentCPM-Explore`](https://huggingface.co/openbmb/AgentCPM-Explore) | `b7bd7bd084f15feb5d48ae22a41f00c49153d74a`；paper 2026-02 | Apache-2.0；Qwen3-4B-Thinking-2507 | 4B dense；training context 128K；eval max output 16,384 | SFT merging + RL reward denoising + context refinement；deep-search agent | BF16，artifact約8.84GB；training 8×／32×A800；無 inference deployment數據 | 8 search benchmarks有 pass@1 signal；headline 97.09 是 pass@64，不得當 reliability。summarizer teacher／reader circularity；`Local Specialist` |
| [`allenai/SERA-8B`](https://huggingface.co/allenai/SERA-8B) | `359cef1e06dc791ac775bee5dd88073502c93434`；paper 2026-01 | Apache-2.0；Qwen3-8B；teacher GLM-4.6 357B | 8B dense；32K | SWE-agent trajectory distillation／repository repair | BF16；8B official model card 建議 1×80GB A100/H100 @32K，但論文 hardware 章節明確描述 SERA-32B，不能視為對 8B footprint 的獨立佐證；quantization只稱可能，無 accuracy／latency測量 | SWE-bench Verified 31.7% ±0.9，3 seeds、tests；強 end-to-end coding signal，但 consumer-local deployment 未建立。`Local Specialist` |
| [`ZYao720/WebArbiter-7B`](https://huggingface.co/ZYao720/WebArbiter-7B) | `f0a7e46a79a7d08416bd87695f221be5ed277d85`；ICLR 2026 | Apache-2.0；Qwen2.5-7B-Instruct | base約7.6B／HF顯示8B；dense；base 32K | o3-distilled SFT 9,642 + GRPO 18,921 pairs；web trajectory reward/verifier | BF16；training 8×A100-80G；無 local inference latency/energy | WebArena-Lite：GPT-4o-mini policy 23.48→40.52 with local verifier，Best-of-5；safe-action bias／element hallucination。`Local Specialist` verifier，不是 standalone agent |
| [`katanemo/Arch-Router-1.5B`](https://huggingface.co/katanemo/Arch-Router-1.5B) | `main` snapshot 2026-08-10；immutable hash未擷取；paper 2025-06 | Apache-2.0；Qwen2.5-1.5B-Instruct | 約1.5B dense；base context | preference-aligned routing到 user-defined domain／action labels | 未報 audited deployment hardware／latency／energy | conversational routing overall 93.17；不預測 downstream success。kNN 受控研究可 match/outperform learned routers；`Local Specialist` 只作 semantic labeler，不作成功率 router |

**Absolute-small 結論：** 至少三個 capability regions 有 end-to-end signal：GUI（MAI-UI-2B）、repository coding（SERA-8B）、multi-turn tool workflow（xLAM-2 3B／8B 的 τ-bench）。Qwen3.5-2B／4B 進一步提供 general/native-tool `Resident Core candidate`，但其agent分數是vendor `C`、缺完整harness與device data，且4B公開建議的128K thinking context超過Dexinode envelope。這支持「保留resident與specialist candidate classes」，不支持「consumer resident network 已可行」。

### 2.3 C — Active-small MoE

| Exact model ID | Revision／release | License／lineage | Total／active／context | Agent specialization | Deployment evidence | Classification／confounds |
|---|---|---|---|---|---|---|
| [`Qwen/Qwen3.6-35B-A3B`](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | official public release 2026-04-16（blog／repo／HF dates略有差異）；`main` snapshot 2026-08-10，immutable hash未擷取 | Apache-2.0；Qwen3.6 MoE | report 35B total／3B active；HF instantiated metadata約36B；native 262,144，可延至約1.01M | native tool use；coding／terminal／MCP agent evaluations | official serving recipes以 8 GPUs；無 consumer memory／latency／energy；card建議 >=128K 保留 thinking能力 | `Active-small`、不是 Absolute；可作 larger local/datacenter reference。SWE-bench Verified 73.4 等屬 vendor harness；128K建議與 Dexinode 16–32K envelope衝突 |
| [`Qwen/Qwen3-Coder-Next`](https://huggingface.co/Qwen/Qwen3-Coder-Next) | release 2026-02-03；`main` snapshot 2026-08-10；immutable hash未擷取 | Apache-2.0；Qwen3-Next | 80B total／3B active；native 262,144 | executable task synthesis、environment interaction、RL；no-thinking agentic coder | SGLang／vLLM examples以 tensor parallel 2；可把 server context降至32K但沒有等效能力證據 | `Active-small`、不是 Absolute。official SWE-bench Verified 70.6／Terminal-Bench 2 36.2；harness-confounded、無 edge deployment |

**Active-small 結論：** active parameters 不能替代 total weight、memory bandwidth、KV cache、expert parallel 與 runtime footprint。這兩個模型可支持「relative-small agent model」，不得支持 absolute-small／edge decentralization。

### 2.4 D — Remote／frontier reference

| Exact API／model ID | Revision／release | Params／context／license | Agent evidence | 為何只能是 reference |
|---|---|---|---|---|
| [`deepseek-ai/DeepSeek-V4-Flash-0731`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)；API alias `deepseek-v4-flash` | named release 2026-07-31；MIT | technical report architecture 284B total／13B active；0731 artifact metadata 304B（含 DSpark module）；1M；FP4+FP8 mixed | official Terminal-Bench 2.1 82.7、Toolathlon-Verified 70.3；minimal DeepSeek Harness尚未發布、max effort、temp1/top_p .95 | active 13B >8B、4×GB300 serving recipe；remote／datacenter reference，不能列 Active-small |
| [`deepseek-ai/DeepSeek-V4-Pro`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)；API alias `deepseek-v4-pro` | Preview，2026-04-24；截至截止日 official release仍標「將推出」；MIT | 1.6T total／49B active；1M；FP4+FP8 mixed | technical report agent／coding benchmark；API function/tool integrations仍有格式與 support caveats | frontier open-weight/API reference；遠超 local viability |
| API [`qwen3.7-flash`](https://help.aliyun.com/en/model-studio/qwen3-7-flash)；snapshot `qwen3.7-flash-2026-07-15` | official hosted snapshot 2026-07-15 | proprietary hosted；1M context；total／active undisclosed | function calling、structured output、web search | 無 open checkpoint／local deployment metadata；`Remote Reference` |
| API [`qwen3.8-max`](https://help.aliyun.com/en/model-studio/qwen3-8-max) | official hosted release 2026-08-02；immutable snapshot ID未在擷取頁取得 | proprietary hosted；official total約2.4T MoE，active undisclosed | function calling、structured output、web search；vendor claims | 只有 hosted evidence，且 harness欄位不足；`Remote Reference` |
| [`Qwen/Qwen3.5-9B`](https://huggingface.co/Qwen/Qwen3.5-9B)／[`Qwen/Qwen3.6-27B`](https://huggingface.co/Qwen/Qwen3.6-27B) | releases 2026-03-02／2026-04-22 | Apache-2.0；dense general models；262,144 context | native tool use／agent benchmarks | >8B total，故`Ineligible`作Absolute；large-local／remote upper references |
| `Tongyi-MAI/MAI-UI-8B` | `e00a0097abb9cc621cac5172d8c4809f0839c94e` | name 8B、artifact metadata約9B；Apache-2.0 | official card有GUI agent benchmark，但本表不引用其分數 | 嚴格定義下 total >8B，故 `Ineligible` 作 Absolute-small；可作 GUI upper reference |
| `microsoft/Fara1.5-9B` | official 2026-07 family release | 9B-class multimodal；MIT | official card有dynamic web benchmark，但本表不引用其分數 | >8B，`Ineligible` 作 Absolute-small；large-local／remote reference |

## 3. Capability coverage；不作總排行榜

| Capability class | Edge-small evidence | Absolute-small evidence | Active／remote upper reference | 本輪判定 |
|---|---|---|---|---|
| function selection／arguments | FunctionGemma；Hammer 0.5B與Qwen3.5-0.8B metadata | Qwen3.5-2B/4B、TinyAgent、xLAM-2、Hammer | DeepSeek／Qwen hosted tool calling | `PARTIALLY SUPPORTED`；syntax／BFCL遠強於真實 action evidence |
| multi-turn tool use | Qwen3.5-0.8B TAU2很低 | Qwen3.5-2B/4B與xLAM-2 τ/TAU benchmark；TinyAgent synthetic DAG | DeepSeek／Qwen | `PARTIALLY SUPPORTED`；Qwen為vendor harness，xLAM license與部署是 blocker |
| GUI／mobile／computer use | 無 sub-1B end-to-end | MAI-UI-2B、Fara1.5-4B；AgentCPM static action | MAI-UI actual9B、Fara9B | `PARTIALLY SUPPORTED`；2B end-to-end signal成立，device evidence未成立 |
| coding agent／repo／terminal | 無 | SERA-8B 31.7% SWE-bench Verified | Qwen Coder Next、Qwen3.6、DeepSeek-V4 | `PARTIALLY SUPPORTED`；8B end-to-end，但 80GB 建議只有 model card，論文 hardware 章節是 SERA-32B，consumer-node footprint 仍無實證 |
| search／research agent | 無 | AgentCPM-Explore-4B | DeepSeek／Qwen web search | `PARTIALLY SUPPORTED`；summarizer/backbone circularity與pass@64需拆開 |
| memory manager／context selector | FunctionGemma不適用 | LightMem 1B、DimMem 4B、PrivScope 3B是 research systems，無成熟通用 model card | frontier controller in LongMemEval-V2 | `OPEN` 作 Resident component；bounded extraction／necessity `PARTIALLY SUPPORTED` |
| planner／controller／router | 無 | Qwen3.5-4B general-agent signal；Arch-Router 1.5B只做 semantic route；MAI DCC local/cloud | remote planners、Qwen active-small | Resident planning仍`OPEN`；domain label accuracy不能代理 P(success) |
| verifier／critic／reward model | 無 | WebArbiter-7B；deterministic tests優先 | frontier LLM judges | `PARTIALLY SUPPORTED`；local verifier可增益，但 Best-of-5與remote policy confounded |

## 4. Benchmark configuration audit

所有被引用的 agent 數字在此綁回 configuration；任一重要欄缺失即標 `harness-confounded`。

| ID | Model／score | Harness／context policy | Tool interface | Step／token／cost budget | Retry／sampling | Environment revision | Evaluator／judge | 可比性判定 |
|---|---|---|---|---|---|---|---|---|
| B1 | FunctionGemma；BFCL simple 61.6、multiple 63.5、parallel 39.0、parallel-multiple 29.5 | BFCL official evaluation；0-shot；實際 prompt context未逐題報 | BFCL function schemas／JSON calls | max tokens／wall time未完整報 | decoding／retry未完整報 | BFCL revision在card未鎖 commit | deterministic AST／category metrics | **harness-confounded**；只可在同 card內看類別差異 |
| B2 | TinyAgent-1.1B 80.06；7B 84.95 | 1K synthetic MacOS test；ToolRAG 16→約3.97 tools；prompt約1,397 tokens | 16 mocked MacOS functions；輸出 plan DAG | 單次 plan；token cap未報 | sampling／retry未報 | synthetic dataset generated by GPT-4-Turbo；無 live OS | tool-set + dependency DAG isomorphism | **非 end-to-end**、generator contamination、harness-confounded |
| B3 | xLAM-2 1B／3B／8B：BFCL 58.90／65.11／72.83；τ-bench 21.8／38.2／46.7 | BFCL-v3；τ-bench retail+airline；native 32/128K但實際 used context未逐項報 | benchmark function schemas；τ-bench只給官方 tools，model可用 think tool | τ-bench episode cap／tokens未完整報 | 至少5 trials、pass@1 aggregate；temperature細節未完整 | τ-bench environment版本在paper；service simulator | BFCL deterministic；τ-bench user simulator + state/action check | τ-bench是較強 end-to-end signal；跨論文仍 **harness-confounded** |
| B4 | Fara1.5-4B：80.8／57.3／27.4 | MagenticLite/Fara harness；latest 3 screenshots；temp0、max output2,048 | screenshot + browser GUI actions；critical ask/pause | total step cap／cost未完整報 | run count／variance未完整報 | WebVoyager／Online-Mind2Web／WebTailBench dynamic snapshots | universal verifier／LLM judge + environment signals | dynamic web但 revision與retries不足；**harness-confounded** |
| B5 | MAI-UI-2B AndroidWorld 49.1 | official MAI-UI agent；AndroidWorld 116 tasks／20 apps；actual context未報 | GUI + ask_user + MCP action schema | rollout step/token cap未完整報 | run count／sampling未完整報 | Android emulator/app benchmark revision由paper定義 | AndroidWorld task-state evaluator | 有 end-to-end環境；仍為 vendor、**harness-confounded** |
| B6 | AgentCPM-GUI AC-low 90.20、AC-high 69.17 | static screenshot/history→next action；max output2,048 | compact JSON action；n=1、temp0.1、top_p0.3 | one next action | no retry | AC／GUI-Odyssey／AITZ/CAGUI paper versions | Exact Match／Type Match | **不是 execution success**；不可與 AndroidWorld比較 |
| B7 | SERA-8B SWE-bench Verified 31.7% ±0.9 | SWE-agent exact interface；32K；Python subset特性 | shell/editor/search/submit tool | paper training avg35 API calls；evaluation max steps／cost未完整列 | 3 seeds；pass@1 | SWE-bench Verified environment/tests | deterministic repo tests | end-to-end；仍 **harness-confounded** 於 step cap與SWE-agent format |
| B8 | AgentCPM-Explore：GAIA 63.9 等；97.09 headline | paper agent harness；128K training、max output16,384 | search/fetch；Jina webpage trunc95K；server timeout120/180s | search auto-retry×3；overall step/cost未完整報 | 主表多為 pass@1；97.09是 pass@64 | eight search benchmarks各自revision | exact/LLM judge依dataset；summarizer可看到question | **harness-confounded**；pass@64不得作 reliability；summarizer可能解題 |
| B9 | WebArbiter：GPT-4o-mini policy 23.48→40.52 | WebArena-Lite；local reward model reranks trajectories | browser actions由remote policy產生；arbiter只看AXTree trajectory | Best-of-5 knockout，故5× generation cost | deterministic arbiter max2,048；policy sampling依harness | WebArena-Lite version | benchmark outcome／judge | 證明 verifier augmentation，不證明 7B standalone agent；**policy-confounded** |
| B10 | Qwen3.6-A3B SWE Verified73.4、TerminalBench2 51.5等 | internal SWE scaffold；Terminal Harbor/Terminus2；card建議>=128K | bash/file edit／terminal／MCP schemas | SWE max200K；Terminal 3h、max80K、32CPU/48GB | temp1/top_p.95/top_k20；retries依benchmark未全報 | benchmark/card revisions，部分 internal | tests／benchmark judges | vendor `C`；多GPU、長context；**harness-confounded** |
| B11 | Qwen3-Coder-Next SWE Verified70.6、TerminalBench2 36.2 | official agent harness；262K native；可啟動32K但未證等效 | coding/terminal tools | exact step/token budget未在card完整報 | sampling/retry未完整報 | benchmark revisions由card連結 | tests／benchmark evaluator | vendor `C`；**harness-confounded** |
| B12 | DeepSeek-V4-Flash-0731 TerminalBench2.1 82.7、Toolathlon 70.3 | unreleased minimal DeepSeek Harness；max reasoning；recommended max output可達384K | coding／terminal／tool schemas | benchmark實際 token/step/cost未公開 | temp1、top_p.95；retry未報 | public benchmarks，另含 internal sets | tests／benchmark-specific evaluators | harness未發布，**不可審核／harness-confounded**；只作 frontier ceiling |
| B13 | Arch-Router overall 93.17 | synthetic conversational turn/full-dialogue routing；base context | label list，不執行 downstream tool | one routing decision；token/cost未報 | sampling/retry未完整報 | paper dataset | exact route-label match | 只測 semantic label；**不能當 success router** |
| B14 | Qwen3.5 0.8B／2B／4B：BFCL-V4 25.3／43.6／50.3；TAU2 11.6／48.8／79.9 | official Qwen3.5 harness；thinking mode；native262K，但benchmark實際context未報；TAU2 airline套用Claude Opus 4.5 system-card fixes | Qwen-Agent／`qwen3_coder` tool-call parser；TAU2 domain tools | step、token、wall-time、cost未完整報；card generation上限示例可達32K/81,920，非benchmark budget | top_p.95、top_k20、presence1.5、temp1；retry／runs未報 | BFCL-V4／TAU2 benchmark revisions未鎖commit於card | BFCL deterministic；TAU2 user/environment evaluator | vendor `C`；**harness-confounded**。2B有thinking-loop warning；4B於16–32K未驗證 |

## 5. Known negative evidence 與部署陷阱

1. **名稱參數陷阱**：MAI-UI-8B 的 artifact顯示約9B；Fara1.5-4B 的 multimodal artifact約5B；Qwen3.6-35B-A3B artifact約36B；DeepSeek Flash-0731 因 DSpark module 約304B，而 report core architecture 284B。
2. **active params陷阱**：Qwen 3B active models仍需載入35/80B total weights；不能用 3B active 估算手機可部署性。
3. **native context陷阱**：262K／1M 是可輸入上限，不是 legacy repo comprehension保證。Qwen3.6 card甚至建議 >=128K維持 thinking；與 Dexinode 16–32K packet假設尚未相容。
4. **function syntax陷阱**：BFCL／Exact Match沒有測 credentials、tool side effects、recovery、clarification或 human burden。
5. **quantization陷阱**：「有 GGUF／4-bit」不等於 accuracy、RSS、P95 latency、energy已驗證。FunctionGemma與TinyAgent是少數有具體 device measurements。
6. **teacher循環**：TinyAgent資料由 GPT-4-Turbo生成；xLAM資料由 frontier models生成/驗證；SERA teacher 357B；AgentCPM-Explore summarizer受 DeepSeek/GPT能力影響。小模型可部署不等於 training/evaluation論證不依賴大模型。
7. **pass@k陷阱**：AgentCPM-Explore 97.09 是 pass@64；WebArbiter用 Best-of-5。Dexinode若只允許小 retry budget，不能引用這些 headline。
8. **router陷阱**：[RouteLLM kNN controlled study](https://arxiv.org/html/2505.12601v1) 顯示簡單 kNN在標準化場景可 match/outperform learned routers；Arch-Router的 domain/action label accuracy不等於 `P(success | model, task)`。
9. **research-agent反證**：[LiteResearcher](https://arxiv.org/html/2604.17931v5) 在作者比較的八個 search benchmarks 全勝 AgentCPM-Explore（例如 GAIA 71.3 vs 63.9），並指出其 RL 在 online noise下增益有限；單一 vendor leaderboard不可當穩定優勢。
10. **commercial eligibility**：xLAM-2 是 CC-BY-NC；Hammer沿用 Qwen Research License。即使能力可行，也不構成一般 commercial Local Specialist path。
11. **current general-model陷阱**：Qwen3.5-4B 的語言模型標4B、完整artifact顯示5B；雖仍在Absolute範圍，官方agent分數未報step／retry／實際context，且card建議complex thinking保留至少128K。Qwen3.5-2B則明示thinking loop可能無法終止。

## 6. 對 Dexinode 的保留候選區域

這不是 model selection；只是 architecture hypothesis 中尚未被證偽的 capability contracts。

| Contract | 最低具有 end-to-end signal 的 absolute-small evidence | 仍缺什麼 | 暫定角色 |
|---|---|---|---|
| bounded GUI workflow + ask／abstain | MAI-UI-2B，AndroidWorld 49.1 | device P95／energy、irreversible-action safety、跨app更新、human takeover | Local Specialist |
| multi-turn structured tool workflow | xLAM-2-3B，τ-bench 38.2 | commercial license、real API failures、clarification／abstention、hardware | Local Specialist；research-only artifact |
| repository issue repair | SERA-8B，SWE-bench Verified 31.7 ±0.9 | consumer deployment、non-Python transfer、active human time、32K packet adequacy | Local Specialist；datacenter-local today |
| bounded deep search | AgentCPM-Explore-4B，multi-benchmark pass@1 signal | independent reproduction、citation quality、summarizer isolation、latency | Local Specialist |
| trajectory verification | WebArbiter-7B + remote policy增益 | local policy pairing、Best-of-1、safe-action calibration、deterministic verifier comparison | Local verifier specialist |
| phone-class function call | FunctionGemma 270M device measurement | task-specific fine-tune、real execution、security／clarification | Edge Specialist |
| memory/context controller | LightMem／DimMem／PrivScope research systems | stable model artifact、project-action success、poison recovery、P95 | `OPEN`；不得升格 Resident Core proof |
| general local intent／tool／integration | Qwen3.5-4B（artifact 5B）TAU2/BFCL vendor signal；Qwen3.5-2B較弱 | independent harness、16–32K能力、memory integration、device P95／energy、loop termination | `Resident Core candidate`，尚未validated |

## 7. Landscape-level conclusion

- `ESTABLISHED`：edge 270M function-call model可在手機CPU高吞吐執行；active-small MoE 與 absolute-small 是不同部署類別。
- `PARTIALLY SUPPORTED`：至少 GUI、tool workflow、repository coding 三類 absolute-small 能力有 end-to-end signal；其中證據品質、license、硬體與 harness各有不同缺口。
- `OPEN`：Qwen3.5-2B／4B等任何1B–8B general model + memory/context manager + tools/verifiers 是否能成為可信 Resident Core；native tool benchmark不等於integrated resident evidence。
- `OPEN`：同一 specialist在 Dexinode 8K–32K packet、低 retry、固定 latency／human-review budget下能否保留 published success。
- `CONTRADICTED`：從 leaderboard headline、native context或 active parameter數直接推論 local viability。

## 8. Primary source index

- FunctionGemma：[official model card](https://huggingface.co/google/functiongemma-270m-it)、[official developer guide](https://ai.google.dev/gemma/docs/functiongemma)
- TinyAgent：[EMNLP 2024 demo paper](https://aclanthology.org/2024.emnlp-demo.9/)、[full paper](https://arxiv.org/html/2409.00608v1)
- xLAM-2：[technical paper](https://arxiv.org/html/2504.03601v2)、[official repository](https://github.com/SalesforceAIResearch/xLAM)
- MAI-UI：[technical paper](https://arxiv.org/html/2512.22047v1)
- AgentCPM-Explore：[technical paper](https://arxiv.org/html/2602.06485v1)
- SERA-8B：[technical paper](https://arxiv.org/html/2601.20789v1)
- WebArbiter：[ICLR 2026 paper](https://arxiv.org/html/2601.21872v2)
- Arch-Router：[technical paper](https://arxiv.org/html/2506.16655v1)
- Qwen3.5／3.6／Coder-Next：各 row 的 official model card；[official release repository](https://github.com/QwenLM/Qwen3.6)
- DeepSeek-V4：[technical report](https://arxiv.org/html/2606.19348v1)、[official API changelog](https://api-docs.deepseek.com/updates/)
