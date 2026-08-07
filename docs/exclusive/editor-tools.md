---
title: 编辑器增强工具
sidebar_position: 7
---

# 编辑器增强工具

RemixWarp 提供了一系列编辑器增强工具，这是 Bilup 中没有的。

## 1. 积木计数器（Block Counter）

在舞台区实时显示项目积木数量的计数器徽标（使用像素字体渲染数字）。

**功能：**
- 实时显示积木/脚本块数量
- 提供计数显示的开/关切换按钮（舞台按钮图标）

**入口：** 舞台区显示的积木数量徽标与切换按钮。

## 2. 多工作区（Multi-Workspaces）

支持多角色/多工作区并行编辑，可切换不同角色/舞台的积木工作区。

**功能：**
- 为不同角色/舞台维护独立的积木工作区
- 提供工作区标签切换栏
- 可在多个工作区之间快速切换

## 3. 自定义菜单栏（Custom Menu Bar）

允许隐藏编辑器菜单栏的特定项，或移除其文字标签/图标。

**设置项：**
- `menu-labels`：选择显示"图标和标签 / 仅图标 / 仅标签"（`both` / `icons` / `labels`）

**说明：** 小窗口下文字标签可能自动替换为图标。

## 4. 书签（Bookmark）

为项目添加书签，方便快速在不同代码区域间导航跳转。

**功能：**
- 通过特殊注释存储书签数据（`BOOKMARK_MAGIC`）
- 提供书签添加/跳转交互

## 5. 待办清单（Todo List）

为编辑器添加待办列表功能（分组/任务管理），通过特殊注释持久化到舞台。

**功能：**
- 独立待办窗口（标题显示"项目名 + 的待办"）
- 支持分组、任务、颜色
- 数据以 `_TODO_LIST_` 特殊注释存入舞台，随项目保存

## 6. 每日一句（Daily Quote）

在编辑器状态栏显示每日一句/随机短语。

**设置项：**
- `enable_daily_quote`：启用
- `interval`：切换间隔秒（默认 5）
- `display_mode`：顺序 / 随机显示
- `quote_library`：句库（默认 / 一言 Hitokoto / 古动笔记 / 今日诗词）
- `custom_quotes`：自定义内容（多行文本）

## 7. 终端（Terminal）

添加一个按钮，打开带 xterm.js 的独立终端窗口。

**功能：**
- 点击终端按钮打开独立终端窗口
- 使用 xterm.js 渲染终端

## 8. 语言菜单（Language Menu）

语言选择菜单，支持切换语言、上传语言包、下载语言包模板。

**功能：**
- 切换编辑器语言
- 上传自定义语言包
- 下载语言包模板

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 积木计数器 | `src/components/block-counter/` |
| 多工作区 | `src/components/blocks/multi-workspaces.jsx` |
| 自定义菜单栏插件 | `src/addons/addons/custom-menu-bar/` |
| 书签插件 | `src/addons/addons/bookmark/` |
| 待办清单插件 | `src/addons/addons/todo-list/` |
| 每日一句插件 | `src/addons/addons/daily-quote/` |
| 终端插件 | `src/addons/addons/Terminal/` |
| 语言菜单 | `src/components/menu-bar/language-menu.jsx` |
| 语言服务 | `src/services/LanguageService.js` |
