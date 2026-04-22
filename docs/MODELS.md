# 資料模型設計 (MODELS) - 宮廟抽籤與捐獻系統

基於先前的產品需求 (PRD) 與系統架構 (ARCHITECTURE) 規劃，系統將需要以下三張核心資料表來儲存會員、抽籤紀錄與金流訂單等動態數據。

## 1. 資料表定義 (Schema Definition)

| 表名稱 (Table Name) | 商業用途 (Description) |
|---|---|
| **Users** | 儲存註冊會員的基本資訊與密碼驗證。 |
| **DivinationRecords** | 儲存使用者歷次的求籤結果與所問事項。 |
| **Donations** | 儲存線上添香油錢（捐獻）的金流交易資訊與狀態。 |

> **架構建議**：系統中的 60 首籤詩文本資料 (Poems) 因為屬於靜態不會變動的唯讀資料，建議直接置於 `static/data/poems.json` 當中讓前端靜態讀取即可，不需存入資料庫以減少 I/O 開銷。

---

## 2. 屬性與欄位 (Fields & Columns)

### 2.1 會員表 (`Users`)
| 欄位名稱 (Field) | 資料型別 (Type) | 限制與屬性 (Constraints) | 說明 (Description) |
|---|---|---|---|
| `id` | Integer | Primary Key, Auto Increment | 會員唯一內部識別碼 |
| `email` | String(120) | Unique, Not Null | 登入帳號及聯絡用信箱 |
| `password_hash` | String(255) | Not Null | 經 bcrypt 雜湊加密的密碼 |
| `created_at` | DateTime | Default Current Time | 會員初次註冊的時間 |

### 2.2 抽籤紀錄表 (`DivinationRecords`)
| 欄位名稱 (Field) | 資料型別 (Type) | 限制與屬性 (Constraints) | 說明 (Description) |
|---|---|---|---|
| `id` | Integer | Primary Key, Auto Increment | 該筆紀錄唯一識別碼 |
| `user_id` | Integer | Foreign Key (`Users.id`), Not Null| 發起抽籤的所屬會員 |
| `question` | String(255) | Nullable | 在心中默念的問題敘述 (選填) |
| `poem_id` | Integer | Not Null | 使用者最終擲筊求得的籤號 (1~60) |
| `created_at` | DateTime | Default Current Time | 抽籤日期與發生的時間 |

### 2.3 捐獻紀錄表 (`Donations`)
| 欄位名稱 (Field) | 資料型別 (Type) | 限制與屬性 (Constraints) | 說明 (Description) |
|---|---|---|---|
| `id` | Integer | Primary Key, Auto Increment | 捐獻訂單系統主鍵 |
| `user_id` | Integer | Foreign Key (`Users.id`), Nullable | 捐獻者會員 ID (若設計開放匿名訪客隨喜則可為 null) |
| `amount` | Integer | Not Null | 捐獻金額數量 (新台幣) |
| `status` | String(20) | Default 'PENDING' | 交易與結帳狀態 (`PENDING`, `SUCCESS`, `FAILED`) |
| `trade_no` | String(100) | Unique, Nullable | 綠界或行動支付端返回的非同步訂單編號 |
| `created_at` | DateTime | Default Current Time | 點選結帳的建立時間 |
| `paid_at` | DateTime | Nullable | 第三方金流 Webhook 通知付款成功的時間 |

---

## 3. 關聯性 (Relationships)

1. **`Users` ↔ `DivinationRecords` (一對多, 1:N)**
   - 一個使用者 (`Users`) 可以擁有無數次的歷史抽籤紀錄 (`DivinationRecords`)。
   - 紀錄表透過 `user_id` 指向使用者資料表。當建立會員個人中心時，我們能利用這個外鍵提取個人的抽籤歷史清單。

2. **`Users` ↔ `Donations` (一對多, 1:N)**
   - 一個使用者 (`Users`) 可以發起多次捐獻 (`Donations`) 操作。
   - `user_id` 在此表設定為 `Nullable` 的目的在於預留彈性：您未來可能會想鼓勵未註冊會員同樣也可以做零星隨喜捐獻；若強制綁定，則非 Null。
