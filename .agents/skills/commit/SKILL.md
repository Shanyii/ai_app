---
name: commit
description: 提交推送，執行 Git 狀態分析與 Commit、Push
---
# 提交推送指令 (Commit Skill)

當使用者呼叫此 skill 時，你的任務是負責開發流程的最後一個階段：「提交與推送 (Commit & Push)」。

## 執行目標
你將協助使用者將這段時間新增、修改的文件與程式碼變更加入版本控制。

## 步驟要求
1. **分析當前變更**：透過終端機執行指令分析專案更動的內容 (如 `git status`, `git diff`)。如果專案尚未初始化 git，先協助執行 `git init`。
2. **撰寫 Commit Message**：根據你總結出的變動內容（如完成 PRD、建立資料模型及生成程式碼等），自動撰寫出精準且符合慣例的 commit 訊息。
3. **執行版控指令**：
   - 將變更加入暫存 (`git add .`)
   - 提交日誌 (`git commit -m "你的訊息"`)
   - 推送至遠端庫 (`git push`，若已有設定 remote)。
4. 如果有任何 Git 衝突或遠端未設定的問題，請向使用者提問以尋求解方。
