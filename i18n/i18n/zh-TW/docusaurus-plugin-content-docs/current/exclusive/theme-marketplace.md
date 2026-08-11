---
title: 主題商城
sidebar_position: 5
---

# 主題商城

RemixWarp 內置了兩個主題商城，允許用戶在編輯器中搜索、下載並應用其他用戶分享的主題。這是 RemixWarp 中沒有的功能。

## 1. Bilme Marketplace

從 `https://theme.bilup.org/api/theme/export` 拉取像素主題的主題商城。

**功能：**
- 搜索、排序、篩選主題
- 下載/應用他人主題
- 自動補齊主題默認值（name / gui / blocks）
- 使用 `CustomTheme.import` 創建主題並 `applyTheme` + `setTheme` 應用

**入口：** 菜單欄"Bilme Marketplace"菜單項（`openBilmeModal`）。

## 2. WarpTheme Store

從 `https://warptheme.mistium.com/api/theme/export` 拉取像素主題的主題商城（另一平臺入口）。

**功能：**
- 搜索、下載並應用主題
- 導出 API 失敗時提供回退方案（直接用列表數據）

**入口：** 菜單欄"WarpTheme Store"菜單項（`openWarpthemeModal`）。

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| Bilme 商城組件 | `src/components/bl-bilme/bilme-modal.jsx` |
| WarpTheme 商城組件 | `src/components/bl-bilme/warptheme-modal.jsx` |
| 菜單項 | `src/components/menu-bar/bl-bilme-menu.jsx`、`bl-warptheme-menu.jsx` |
| 容器 | `src/containers/bl-bilme-modal.jsx`、`warptheme-modal.jsx` |
