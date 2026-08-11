---
title: AI 助手
sidebar_position: 2
---

# AI 助手

RemixWarp 內置了多種 AI 輔助編程能力，這是 RemixWarp 中不具備的功能。主要包括四套 AI 組件。

## 1. 02agent（AI 智能體）

02agent 是基於 Gandi IDE AI assistant 二次開發的 AI 助手插件，由 02engine 團隊改造，能夠編寫 Scratch 代碼。

**功能：**
- AI 對話與代碼生成
- 擴展加載
- 工程快照
- 可編寫完整的 Scratch 積木代碼

**界面入口與設置：**
- `showButtonInEditor`：是否將按鈕添加到編輯器右上角（默認開啟）
- `showButtonInToolsMenu`：是否添加到"工具-AI"菜單（默認開啟）
- 編輯器右上角會懸浮一個 AI 助手按鈕/入口

## 2. Astras Copilot

為 Scratch 添加 AI 輔助編程功能（Astras Copilot v4.0），內置 **ScratchDSL 代碼生成** 能力，可將 AI 生成的積木代碼一鍵導入工作區。

**功能：**
- 在菜單欄注入 🤖 AstrasCopilot 聊天按鈕
- 彈出 AI 聊天窗口（含標題、模型選擇、輸入框、發送/清空/生成按鈕）
- 生成的代碼可一鍵"導入"到工作區

## 3. AI 面板（ai-panel）

接入 **SiliconFlow 等大模型 API** 的通用 AI 智能助手面板，是 RemixWarp 中最完整的 AI 組件。

**功能：**
- **AI Chat 對話**：與 AI 多輪對話
- **多步驟 AI Agent**：分步驟執行復雜創作任務
- **造型/圖片生成**：生成 SVG、上傳造型，生成素材可一鍵添加到舞臺
- 浮動面板支持多標籤：`chat` / `costume` / `control`

**界面入口：**
- 編輯器內浮動 AI 聊天/繪圖面板
- 通過多種彈窗容器打開：`ai-modal`（通用）、`ai-chat-modal`（聊天）、`ai-agent-modal`（智能體）

## 4. 百度 AI（Baidu AI）

內嵌 **百度 AI（文心一言）** iframe 對話面板。

**功能：**
- 在編輯器中新增"百度 AI"標籤頁
- 通過 iframe 方式接入百度文心大模型對話

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 02agent 插件 | `src/addons/addons/02agent/` |
| Astras Copilot 插件 | `src/addons/addons/astras-copilot/` |
| AI 面板組件 | `src/components/ai/ai-panel.jsx` |
| 百度 AI 面板 | `src/components/ai/baidu-ai-panel.jsx` |
| AI 彈窗容器 | `src/containers/ai-modal.jsx`、`ai-chat-modal.jsx`、`ai-agent-modal.jsx`、`baidu-ai-modal.jsx` |
| 積木滾動輔助 | `src/utils/block-helper.ts` |
