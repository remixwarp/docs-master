---
title: 总览
sidebar_position: 1
---

# RemixWarp 独有功能

本章节介绍了 **RemixWarp 编辑器（scratch-gui）** 相比 **Bilup 编辑器** 额外提供、而 Bilup 中没有的全部功能。

## 为什么存在这些差异

RemixWarp 是基于 TurboWarp 构建的 Scratch 修改版，而 Bilup 是另一个独立的 Scratch 修改版。两者虽然共享大量底层代码，但 RemixWarp 在以下方向拥有更多独有能力：

- **AI 助手与智能创作**
- **成就系统**
- **主题商城（Bilme / WarpTheme）**
- **协作共享背包**
- **扩展开发工具链**
- **版本管理与云端还原点**
- **大量编辑器增强插件（Addons）**

## 功能目录

### 智能创作与 AI
- [AI 助手](./ai-assistant) —— 02agent、Astras Copilot、AI 面板、百度 AI
- [成就系统](./achievements) —— 解锁成就、积累经验
- [AI 增强扩展（AE）](./ae-features) —— README、自定义主题、扩展预览、功能引导

### 主题与商店
- [主题商城](./theme-marketplace) —— Bilme Marketplace 与 WarpTheme Store

### 协作
- [协作共享背包](./shared-backpack) —— 团队共享素材

### 编辑器工具
- [编辑器增强工具](./editor-tools) —— 积木计数、多工作区、自定义菜单栏、书签、待办清单、每日一句、终端
- [调试与运行时工具](./debugging-tools) —— 积木执行高亮、逐帧调试、暂停按钮、积木统计、按名插入积木
- [扩展开发工具](./extension-tools) —— 扩展编辑器、扩展管理器、超级重构

### 账号、安全与系统
- [账号与安全](./account-security) —— 人机验证、登录、语言菜单
- [版本管理与云端还原点](./versioning) —— 更新日志、云端保存
- [其他独有插件](./misc-addons) —— 批量颜色替换、代码风格、注释同步、语言包、视频录制、舞台相机、圣诞等

## 尚未实现/预留的功能

部分独有目录在 scratch-gui 源码中为空或仅有清单文件，属于**预留/未实现**状态：

- `gravity-effect`（重力效果）—— 空目录
- `remixwarp-editor` —— 空目录
- `json-import-export`（JSON 导入导出）—— 仅有清单，无实现代码
