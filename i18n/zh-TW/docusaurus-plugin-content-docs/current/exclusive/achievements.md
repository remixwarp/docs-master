---
title: 成就係統
sidebar_position: 3
---

# 成就係統

RemixWarp 內置了一套完整的**成就係統**，這是 RemixWarp 中沒有的功能。玩家在使用編輯器、創建項目、與 AI 交互時，會根據行為自動解鎖成就並積累經驗值。

## 核心組件

### 1. 成就展示面板（Achievements）

一個展示所有成就的獎盃面板。

**功能：**
- 列出全部成就
- 按分類展示
- 顯示解鎖狀態與經驗值
- 可切換分類

**入口：** 編輯器內成就/獎盃面板彈窗。

### 2. 成就監聽器（Achievement Tracker）

後臺運行的成就監聽器，根據 VM 運行時行為自動解鎖成就。

**可觸發成就的行為包括：**
- 循環積木執行
- 運動積木執行
- 控制積木執行
- AI 對話
- 高幀率運行
- 贊助（Sponsor Intent）
- 協作聊天

### 3. 成就核心（lib/achievements.js）

成就係統的核心數據與邏輯模塊。

**功能：**
- 成就定義列表
- 解鎖邏輯
- 經驗值管理
- 本地存儲
- 記錄 AI 對話、贊助、高幀率、協作聊天等成就

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 成就展示面板 | `src/components/achievements/achievements.jsx` |
| 成就監聽器 | `src/components/achievements/achievement-tracker.jsx` |
| 成就核心邏輯 | `src/lib/achievements.js` |
