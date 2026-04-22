# 系統架構設計文件 (ARCHITECTURE) - 宮廟抽籤與捐獻系統

## 1. 系統概述
本系統採用後端提供 API 與處理業務邏輯，前端專注於互動體驗的架構設計。以滿足線上抽籤、擲筊物理動畫、會員紀錄查詢，以及線上香油錢金流功能。
後端 (Backend) 負責金流 Webhook 驗證、會員狀態管理與資料庫互動；前端 (Frontend) 則專注於建構具有高質感燙金與古典質感的 UI/UX，以及確保擲筊、抽籤等儀式感動畫的流暢度。

## 2. 技術選型 (Tech Stack)
符合先前提及的技術慣例，本次選型如下：
* **後端核心 (Backend)**：Python 3 + Flask (提供輕量有效率的 Web Server 與 API 支援)。
* **資料庫 (Database)**：SQLite (作為本地開發與 MVP 使用) / PostgreSQL (作為未來正式上線的關聯式資料庫)，並搭配 SQLAlchemy 作為 ORM。
* **前端 (Frontend)**：HTML5 / Vanilla CSS / Vanilla JavaScript，若互動狀態較複雜亦可引入 React 或 Vue 工具鏈。
* **金流服務 (Payment Gateway)**：第三方金流 API (如 綠界科技 ECPay 或 LINE Pay)。

## 3. 模組與專案結構
```text
project_root/
├── app.py                 # 後端主程式入口與 API 路由註冊
├── requirements.txt       # Python 依賴套件清單 (Flask, SQLAlchemy 等)
├── config.py              # 系統設定與環境變數 (資料庫 URL, 金流 API Keys)
├── models/                # 資料庫 ORM 實體模型 (User, DivinationRecord, Donation)
├── routes/                # 集中管理的業務邏輯與 API (auth, divination, payment)
├── utils/                 # 工具函式 (密碼雜湊、金流 CheckMacValue 驗算)
├── static/                # 給前端使用的靜態資源 (CSS 樣式, JS 動畫腳本, 圖片)
└── templates/             # 視圖樣板檔案 (HTML)
```

## 4. API 介面規劃清單

### 認證相關 (Authentication)
* `POST /api/auth/register`：會員註冊 (Email, Password)
* `POST /api/auth/login`：會員登入，回傳 Session 或 JWT Token
* `GET /api/auth/me`：取得當前登入者資訊

### 抽籤與紀錄 (Divination & History)
* `GET /api/poems/`：取得籤詩庫資料
* `POST /api/divination/record`：使用者擲筊確認求得籤詩後，將紀錄 (所問事項、籤號) 存入資料庫
* `GET /api/users/me/history`：取得目前登入使用者的過往所有抽籤紀錄

### 金流捐獻 (Donation)
* `POST /api/payments/checkout`：發起添香油錢請求，建立訂單並回傳金流結帳畫面的引導 URL。
* `POST /api/payments/webhook`：此為供第三方金流從背後非同步通知的端點，負責驗證確保交易真實性，並將系統內的捐獻狀態更新為「已付款」。
