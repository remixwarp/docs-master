---
title: 編輯器增強工具
sidebar_position: 7
---

# 編輯器增強工具

RemixWarp 提供了一系列編輯器增強工具，這是 RemixWarp 中沒有的。

## 1. 積木計數器（Block Counter）

在舞臺區實時顯示項目積木數量的計數器徽標（使用像素字體渲染數字）。

**功能：**
- 實時顯示積木/腳本塊數量
- 提供計數顯示的開/關切換按鈕（舞臺按鈕圖標）

**入口：** 舞臺區顯示的積木數量徽標與切換按鈕。

## 2. 多工作區（Multi-Workspaces）

支持多角色/多工作區並行編輯，可切換不同角色/舞臺的積木工作區。

**功能：**
- 為不同角色/舞臺維護獨立的積木工作區
- 提供工作區標籤切換欄
- 可在多個工作區之間快速切換

## 3. 自定義菜單欄（Custom Menu Bar）

允許隱藏編輯器菜單欄的特定項，或移除其文字標籤/圖標。

**設置項：**
- `menu-labels`：選擇顯示"圖標和標籤 / 僅圖標 / 僅標籤"（`both` / `icons` / `labels`）

**說明：** 小窗口下文字標籤可能自動替換為圖標。

## 4. 書籤（Bookmark）

為項目添加書籤，方便快速在不同代碼區域間導航跳轉。

**功能：**
- 通過特殊註釋存儲書籤數據（`BOOKMARK_MAGIC`）
- 提供書籤添加/跳轉交互

## 5. 待辦清單（Todo List）

為編輯器添加待辦列表功能（分組/任務管理），通過特殊註釋持久化到舞臺。

**功能：**
- 獨立待辦窗口（標題顯示"項目名 + 的待辦"）
- 支持分組、任務、顏色
- 數據以 `_TODO_LIST_` 特殊註釋存入舞臺，隨項目保存

## 6. 每日一句（Daily Quote）

在編輯器狀態欄顯示每日一句/隨機短語。

**設置項：**
- `enable_daily_quote`：啟用
- `interval`：切換間隔秒（默認 5）
- `display_mode`：順序 / 隨機顯示
- `quote_library`：句庫（默認 / 一言 Hitokoto / 古動筆記 / 今日詩詞）
- `custom_quotes`：自定義內容（多行文本）

## 7. 終端（Terminal）

添加一個按鈕，打開帶 xterm.js 的獨立終端窗口。

**功能：**
- 點擊終端按鈕打開獨立終端窗口
- 使用 xterm.js 渲染終端

## 8. 語言菜單（Language Menu）

語言選擇菜單，支持切換語言、上傳語言包、下載語言包模板。

**功能：**
- 切換編輯器語言
- 上傳自定義語言包
- 下載語言包模板

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 積木計數器 | `src/components/block-counter/` |
| 多工作區 | `src/components/blocks/multi-workspaces.jsx` |
| 自定義菜單欄插件 | `src/addons/addons/custom-menu-bar/` |
| 書籤插件 | `src/addons/addons/bookmark/` |
| 待辦清單插件 | `src/addons/addons/todo-list/` |
| 每日一句插件 | `src/addons/addons/daily-quote/` |
| 終端插件 | `src/addons/addons/Terminal/` |
| 語言菜單 | `src/components/menu-bar/language-menu.jsx` |
| 語言服務 | `src/services/LanguageService.js` |
