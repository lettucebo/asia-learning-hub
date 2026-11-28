# 設定：Juniper Lane 全通路服務 Agent

[English](setup.md)

## 開始前

使用既有且已核准的非生產 [Microsoft Foundry](https://ai.azure.com/) 專案。確認區域、相容的模型部署、配額，以及 File Search 與請求佐證資料的存取權限。使用 Microsoft Entra 登入，並確認具備該專案的 **Foundry User** 角色。若使用專案連結的儲存體，確認該儲存體上具備必要的 **Storage Blob Data Contributor** 權限。請先由專案擁有者核准建立資源、上傳虛構檔案及模型與 File Search 費用。不為本示範新增或變更共用基礎設施。

[Foundry 角色型存取控制](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) · [File Search 設定與支援格式](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/file-search)

## A. 在 Foundry 入口網站建立並驗收

如果授權操作人員已透過 Azure CLI 建立候選版，可跳過步驟 1、2。先確認已儲存的版本、已核准的模型部署、指示詞與 File Search 綁定。用 CLI 建立不等同完成 Playground 驗收。

1. 開啟新版 Foundry。從專案首頁的 **Build an agent** 選取 **Create an agent**。使用新的名稱，例如 `juniper-lane-omnichannel-portal`；若同名就停止。保留預設的受管 Prompt Agent 執行環境，不選 Copilot harness。選擇已核准的部署，貼上 [instructions.txt](portal/instructions.txt)。
2. 新增 **File Search** 及本案例專用的向量存放區。只上傳下列四份檔案，等待所有檔案完成索引。驗收時不要更動索引，也不要新增其他工具、來源或技能。如果入口網站無法完成設定就停止，不要改用 SDK 取代這個建立步驟。如果入口網站只能透過 Toolbox 綁定，採用前須確認 SDK 可獨立重建所需依賴。
3. 儲存並記錄確切版本。用該版本執行[驗收案例](evaluation/README.zh-TW.md)；`FD-04` 使用另行隔離的配置。逐一比對回應詳細資料、引文或追蹤記錄，自稱已引用不代表查到正確資料。請另一位團隊成員重現設定並記錄結果。不要發佈到管道。
4. 驗收通過後，才透過 [Get an agent version](https://learn.microsoft.com/en-us/azure/foundry/reference/rest/agents-get-agent-version) API 取得該 agent 的確切版本，而不是 `latest`。在清理後的版本 JSON 保留行為與工具設定，並附上素材清單（路徑、雜湊、模型、工具及重建綁定所需的向量存放區或 Toolbox 設定）和驗收記錄。以文件中的邏輯名稱代替專案專屬 ID、私人端點和部署名稱。不包含權杖、租用戶 ID 或原始 trace。這是版本快照和依賴清單，不是可直接匯入的 ZIP。

| 上傳檔案 | 用途 |
| --- | --- |
| [orders_lookup.txt](knowledge/orders_lookup.txt) | 依訂單編號整理的六筆[原始 CSV 訂單](data/orders.csv)。File Search 使用文字檔，不使用 CSV。 |
| [recovery_policy.txt](knowledge/recovery_policy.txt) | 取貨政策 `CR-1` 至 `CR-6` 及固定情境時間 `2026-11-13 12:00`。 |
| [returns_policy.txt](knowledge/returns_policy.txt) | 退換貨評估、例外情形與轉交規則 `RP-1` 至 `RP-6`。 |
| [service_playbook.txt](knowledge/service_playbook.txt) | 退換貨回應格式、草稿措辭與資料使用邊界。 |

原始 CSV 與三份政策文字檔保留來源內容；來源請見[案例首頁](README.zh-TW.md)。查單文字檔由 CSV 整理而來，沒有新增紀錄。[SHA256SUMS](SHA256SUMS) 記錄資料、知識檔案與沿用的驗收檔案的相對路徑及 SHA-256，雜湊以 LF 換行的正式檔案為準。不要將驗收提示或答案當作知識上傳。

## B. 匯出版本確認後用 SDK 重建

尚未執行。入口網站基準版獲得驗收核准後，再用 [Azure AI Projects Python SDK](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent) 在 Foundry Agent Service 重建知識依賴，並建立另一個受管 Prompt Agent。SDK 版必須能在不依賴入口網站版 agent 或其知識資源的情況下執行同一套驗收。此候選版文件未包含 SDK 實作。
