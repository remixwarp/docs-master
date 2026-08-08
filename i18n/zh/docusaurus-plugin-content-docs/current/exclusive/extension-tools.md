---
title: 扩展开发工具
sidebar_position: 8
---

# 扩展开发工具

RemixWarp 提供了一套完整的扩展开发工具链，这是 RemixWarp 中没有的。

## 1. 扩展编辑器（Extension Editor Window）

独立的扩展编辑器浮动窗口，用于新建/编辑扩展。

**功能：**
- 支持 `scratch-extension` 和 `turbowarp` 两种编辑器模式
- 多标签页编辑
- 使用 WindowManager 浮动窗口系统
- 通过 `extension-editor-modal` 容器打开

## 2. 扩展加载方式选择（Extension Load Choice Modal）

加载扩展时，让用户选择加载方式（URL 或本地文件）。

## 3. 超级重构（Super Refactor）

一个强大的项目重构工具，类似 IDE 的项目文件批量编辑/重构窗口。

**功能：**
- 从 VM 运行时动态提取项目全部文件（project.json、图片、声音等）
- 提供文件列表浏览
- 代码/JSON 编辑、搜索过滤、SVG 预览
- 自动换行、语法高亮、暗色主题适配
- `applyChanges` 将编辑后的文件回写应用到 VM 项目
- `downloadProject` 下载项目

## 4. Gandi 扩展帮助（Gandi Help）

提供 Gandi 扩展库的使用帮助说明（针对导入转换项目时扩展未找到的解决方案）。

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 扩展编辑器窗口 | `src/components/extension-editor-window/extension-editor-window.jsx` |
| 加载方式选择 | `src/components/tw-extension-load-choice-modal/` |
| 超级重构弹窗 | `src/containers/super-refactor-modal.jsx` |
| Gandi 帮助 | `src/components/gandi-help/gandi-help.jsx` |
