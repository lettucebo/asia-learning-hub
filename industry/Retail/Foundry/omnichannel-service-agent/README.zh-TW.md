# Juniper Lane 全通路服務 Agent

[English](README.md)

**Microsoft Foundry Prompt Agent｜門市履約與客服｜候選版示範**

在虛構的 Juniper Lane Retail，門市同仁需要判斷是要處理取貨異常，還是將退換貨需求交給適當的人員評估。訂單狀態不等於目前確定可以取貨；標示為不適用一般退貨的商品，若有故障通報，仍須優先交由專人處理。這個 agent 會區分兩類需求、列出依據，並建議由哪位同仁接手。

| 痛點 | 示範效益 |
| --- | --- |
| 使用過期的訂單快照，可能讓顧客白跑一趟。 | 先核對訂單編號與快照時間，再建議下一步。 |
| 商品標示為 `final-sale`，容易讓同仁忽略已通報的故障。 | 引用適用政策，將故障案件交由品管小組（Quality Desk）審查。 |

## 示範

先完成[環境設定](setup.zh-TW.md)。每個提示都在新的 Playground 對話中執行。

| 輸入實測用英文提示 | 預期判斷 |
| --- | --- |
| `Review CC-101 at the fixed demo time.` | 備貨已達承諾時間；請門市履約主管（Store Fulfilment Lead）緊急確認 `CC-101` 的狀態（`CR-3`），不要請顧客前往門市。 |
| `Is CC-106 ready?` | 快照已舊 180 分鐘。先取得新狀態，再評估是否可取貨（`CC-106`、`CR-1`）。 |
| `Final-sale item reported faulty after 45 days with no receipt.` | 依 `RP-2` 交由品管小組審查，不套用一般退貨條件駁回。 |

[Playground 驗收操作指南](evaluation/playground.zh-TW.md) 收錄完整 22 案、23 輪提示及 v3 實測的 22 張英文畫面。指南同時提供繁體中文提示供參考，並逐案標註實際結果、差異以及未執行的隔離案例。

示範只使用六筆虛構訂單與虛構政策。它不存取即時資料，也不發送訊息、修改訂單、保留庫存或退款。草稿只供同仁覆核。File Search 用於檢索佐證資料，不是訂單資料庫，也不是授權機制；請勿上傳真實顧客資料。

本案例沿用 [Click & Collect Recovery Agent](../../Copilot%20Studio/Click%20%26%20Collect%20Recovery%20Agent/README.md) 與 [Returns & Exchange Policy Coach](../../Agent%20Builder/Returns%20%26%20Exchange%20Policy%20Coach/README.md) 的素材，不必部署這兩個來源案例。

**交付狀態：** 操作指南記錄一次 v3 實測，不等同正式驗收。仍待同儕驗證、匯出版本與 SDK 重建。
