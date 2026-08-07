---
title: AI 增强扩展（AE）
sidebar_position: 4
---

# AI 增强扩展（AE）

RemixWarp 提供了一组"AI 增强"（AE）扩展功能，围绕 README、自定义主题、扩展预览与功能引导展开。这些是 Bilup 中没有的。

## 1. 项目 README 阅读器（AEReadme）

一个项目/造型说明（README）阅读器，能够渲染 Markdown 注释说明。

**功能：**
- 读取编辑目标注释信息
- 渲染 Markdown 说明（支持代码块、标题、图片）
- 弹出式 README 查看面板

**入口：** 编辑器内点击 README 按钮弹出查看面板。通过 `readmeModalVisible` 状态控制显示。

## 2. 自定义主题编辑器（AECustomTheme）

一个自定义主题编辑器，允许用户设置界面配色与积木颜色。

**功能：**
- 编辑界面配色方案
- 编辑积木分类颜色
- 应用到编辑器

**入口：** 编辑器内自定义主题编辑面板。

## 3. 扩展预览（AEPreviewExt）

一个用于预览扩展积木的弹窗，展示扩展的 SVG 积木块。

**功能：**
- 预览扩展的积木外观（SVG）
- 通过 `openPreviewExt` 动作触发

**入口：** 扩展管理相关弹窗。

## 4. 功能引导弹窗（AEFeaturesModal）

在首次进入或版本更新时展示的新功能介绍弹窗。

**功能：**
- 展示版本特性（含版本号）
- 首次进入或版本更新时触发

## 5. AE 设置（AESettings）

一个配置类，用于读写 localStorage 中的 AI 增强设置。

**可配置项包括：**
- README 自动显示
- HTML 支持
- 扩展预览
- VS Code 布局
- 移动端布局

## 相关代码位置

| 模块 | 路径 |
|---|---|
| README 阅读器 | `src/components/ae-readme/ae-readme.jsx` |
| 自定义主题编辑器 | `src/components/ae-custom-theme/custom-theme.jsx` |
| 扩展预览 | `src/components/ae-preview-ext/ae-preview-ext.jsx` |
| 功能引导弹窗 | `src/components/ae-features-modal/ae-features-modal.jsx` |
| AE 设置 | `src/lib/settings.js` |
| 版本信息 | `src/lib/ae-version.js` |
| 容器 | `src/containers/ae-readme.jsx`、`ae-features-modal.jsx` |
