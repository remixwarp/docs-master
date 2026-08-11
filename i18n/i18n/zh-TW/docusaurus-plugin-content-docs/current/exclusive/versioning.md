---
title: 版本管理
sidebar_position: 11
---

# 版本管理

RemixWarp 提供了版本管理功能，這是 RemixWarp 中沒有的。

## 1. 版本管理（Version Manager）

一個版本管理工具，用於檢測應用更新並維護版本歷史。

**功能：**
- 檢測應用是否有更新（`checkForUpdate`）
- 維護版本歷史記錄
- 中文提交信息自動翻譯
- 依賴實驗性開關 `enableAutoUpdateCheck`

## 2. 更新日誌彈窗（Update Log Modal）

展示版本更新記錄的彈窗。

**功能：**
- 延遲 2 秒檢查更新
- 從主題提取配色
- 翻譯更新內容
- 關閉時標記版本為已查看（`markVersionAsSeen`）

## 3. 自定義默認角色（Custom Default Sprite）

將用戶上傳的默認角色持久化到 localStorage，加載默認項目時自動應用。

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 版本管理 | `src/lib/version-manager.js` |
| 更新日誌容器 | `src/containers/update-log-modal.jsx` |
| 自定義默認角色 | `src/lib/custom-default-sprite.js` |
