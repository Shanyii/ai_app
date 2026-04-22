---

# 作業：設計 Skill + 打造線上宮廟與錢包儲值系統

> **繳交方式**：將你的 GitHub repo 網址貼到作業繳交區
> **作業性質**：個人作業

---

## 作業目標

學習使用抗重力 (Antigravity) 系統自訂的六階段 Skill，引導 AI 從零開始規劃並完成一個具備前後端、會員認證與資料庫互動的「線上宮廟抽籤與捐獻系統」。重點在於透過設計專屬的資料夾結構與指令，熟悉以框架化的方式與 AI 協作開發。

---

## 繳交項目

你的 GitHub repo 包含以下內容：

### 1. Skill 設計（`.agents/skills/`）

專案已包含以下六個不同開發階段的 SKILL.md：

| 資料夾名稱        | 對應指令          | 說明                                                                           |
| ----------------- | ----------------- | ------------------------------------------------------------------------------ |
| `prd/`          | `/prd`          | 產出專案的產品需求文件 `docs/PRD.md`                                         |
| `architecture/` | `/architecture` | 產出系統架構與 API 路由規劃 `docs/ARCHITECTURE.md`                           |
| `models/`       | `/models`       | 產出資料庫模型設計 `docs/MODELS.md`                                          |
| `implement/`    | `/implement`    | 產出實際程式碼（**Python Flask + SQLite + HTML前端**）                      |
| `test/`         | `/test`         | 產出手動測試清單 `docs/TEST_PLAN.md`                                           |
| `commit/`       | `/commit`       | 自動打包專案與 Git Push                                |

### 2. 開發文件（`docs/`）

由設計的 Skill 階段所產出的系統開發文件，包含：
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/MODELS.md`
- `docs/TEST_PLAN.md`

### 3. 程式碼

一個可執行的線上宮廟網頁應用，支援以下功能：

| 功能           | 說明                                       | 是否完成 |
| -------------- | ------------------------------------------ | -------- |
| 會員系統       | 註冊、登入與狀態管理 (Flash Session)       | O        |
| 抽籤系統       | 搖籤動畫與結果隨機邏輯，綁定帳號存入資料庫 | O        |
| 雙分頁歷史管理 | 可以動態切換 Modal 來檢視特定分類的紀錄    | O        |
| 錢包儲值機制   | 模擬串接金流，將捐獻金額轉換為帳號點數餘額 | O        |

### 4. 系統截圖（`screenshots/`）

*(提示：可以在上傳作業前，自行於此資料夾補上網站畫面的截圖唷！)*
- `home.png`：宮廟首頁與靈籤筒畫面
- `history.png`：我的紀錄（切換分頁）對話方塊
- `wallet.png`：香火錢儲值模擬畫面

### 5. 心得報告（本 README.md 下方）

在本 README 的**心得報告**區填寫。

---

## 專案結構

```
your-repo/
├── .agents/
│   └── skills/
│       ├── prd/SKILL.md
│       ├── architecture/SKILL.md
│       ├── models/SKILL.md
│       ├── implement/SKILL.md
│       ├── test/SKILL.md
│       └── commit/SKILL.md
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── MODELS.md
│   └── TEST_PLAN.md
├── templates/
│   └── index.html
├── screenshots/
│   └── (請自行放入截圖)
├── app.py
├── config.py
├── models/
│   └── __init__.py
├── requirements.txt
├── .gitignore
└── README.md          ← 本檔案 (含心得報告)
```

---

## 啟動方式

```bash
# 1. 建立虛擬環境 (建議選項)
python -m venv .venv
# Windows 啟動虛擬環境:
.venv\Scripts\activate

# 2. 安裝套件
pip install -r requirements.txt

# 3. 啟動伺服器
python app.py
# 開啟瀏覽器查看：http://localhost:5000
```

---

## 心得報告

**姓名**：
**學號**：

### 問題與反思

**Q1. 你設計的哪一個 Skill 效果最好？為什麼？哪一個效果最差？你認為原因是什麼？**

> （在此填寫）

---

**Q2. 在用 AI 產生程式碼的過程中，你遇到什麼問題是 AI 沒辦法自己解決、需要你介入處理的？**

> （在此填寫）
