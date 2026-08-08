---
title: 主题商城
sidebar_position: 5
---

# 主题商城

RemixWarp 内置了两个主题商城，允许用户在编辑器中搜索、下载并应用其他用户分享的主题。这是 RemixWarp 中没有的功能。

## 1. Bilme Marketplace

从 `https://theme.remixwarp.pages.dev/api/theme/export` 拉取像素主题的主题商城。

**功能：**
- 搜索、排序、筛选主题
- 下载/应用他人主题
- 自动补齐主题默认值（name / gui / blocks）
- 使用 `CustomTheme.import` 创建主题并 `applyTheme` + `setTheme` 应用

**入口：** 菜单栏"Bilme Marketplace"菜单项（`openBilmeModal`）。

## 2. WarpTheme Store

从 `https://warptheme.mistium.com/api/theme/export` 拉取像素主题的主题商城（另一平台入口）。

**功能：**
- 搜索、下载并应用主题
- 导出 API 失败时提供回退方案（直接用列表数据）

**入口：** 菜单栏"WarpTheme Store"菜单项（`openWarpthemeModal`）。

## 相关代码位置

| 模块 | 路径 |
|---|---|
| Bilme 商城组件 | `src/components/bl-bilme/bilme-modal.jsx` |
| WarpTheme 商城组件 | `src/components/bl-bilme/warptheme-modal.jsx` |
| 菜单项 | `src/components/menu-bar/bl-bilme-menu.jsx`、`bl-warptheme-menu.jsx` |
| 容器 | `src/containers/bl-bilme-modal.jsx`、`warptheme-modal.jsx` |
