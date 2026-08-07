---
title: AI 助手
sidebar_position: 2
---

# AI 助手

RemixWarp 内置了多种 AI 辅助编程能力，这是 Bilup 中不具备的功能。主要包括四套 AI 组件。

## 1. 02agent（AI 智能体）

02agent 是基于 Gandi IDE AI assistant 二次开发的 AI 助手插件，由 02engine 团队改造，能够编写 Scratch 代码。

**功能：**
- AI 对话与代码生成
- 扩展加载
- 工程快照
- 可编写完整的 Scratch 积木代码

**界面入口与设置：**
- `showButtonInEditor`：是否将按钮添加到编辑器右上角（默认开启）
- `showButtonInToolsMenu`：是否添加到"工具-AI"菜单（默认开启）
- 编辑器右上角会悬浮一个 AI 助手按钮/入口

## 2. Astras Copilot

为 Scratch 添加 AI 辅助编程功能（Astras Copilot v4.0），内置 **ScratchDSL 代码生成** 能力，可将 AI 生成的积木代码一键导入工作区。

**功能：**
- 在菜单栏注入 🤖 AstrasCopilot 聊天按钮
- 弹出 AI 聊天窗口（含标题、模型选择、输入框、发送/清空/生成按钮）
- 生成的代码可一键"导入"到工作区

## 3. AI 面板（ai-panel）

接入 **SiliconFlow 等大模型 API** 的通用 AI 智能助手面板，是 RemixWarp 中最完整的 AI 组件。

**功能：**
- **AI Chat 对话**：与 AI 多轮对话
- **多步骤 AI Agent**：分步骤执行复杂创作任务
- **造型/图片生成**：生成 SVG、上传造型，生成素材可一键添加到舞台
- 浮动面板支持多标签：`chat` / `costume` / `control`

**界面入口：**
- 编辑器内浮动 AI 聊天/绘图面板
- 通过多种弹窗容器打开：`ai-modal`（通用）、`ai-chat-modal`（聊天）、`ai-agent-modal`（智能体）

## 4. 百度 AI（Baidu AI）

内嵌 **百度 AI（文心一言）** iframe 对话面板。

**功能：**
- 在编辑器中新增"百度 AI"标签页
- 通过 iframe 方式接入百度文心大模型对话

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 02agent 插件 | `src/addons/addons/02agent/` |
| Astras Copilot 插件 | `src/addons/addons/astras-copilot/` |
| AI 面板组件 | `src/components/ai/ai-panel.jsx` |
| 百度 AI 面板 | `src/components/ai/baidu-ai-panel.jsx` |
| AI 弹窗容器 | `src/containers/ai-modal.jsx`、`ai-chat-modal.jsx`、`ai-agent-modal.jsx`、`baidu-ai-modal.jsx` |
| 积木滚动辅助 | `src/utils/block-helper.ts` |
