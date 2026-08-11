---
title: 擴展開發工具
sidebar_position: 8
---

# 擴展開發工具

RemixWarp 提供了一套完整的擴展開發工具鏈，這是 RemixWarp 中沒有的。

## 1. 擴展編輯器（Extension Editor Window）

獨立的擴展編輯器浮動窗口，用於新建/編輯擴展。

**功能：**
- 支持 `scratch-extension` 和 `turbowarp` 兩種編輯器模式
- 多標籤頁編輯
- 使用 WindowManager 浮動窗口系統
- 通過 `extension-editor-modal` 容器打開

## 2. 擴展加載方式選擇（Extension Load Choice Modal）

加載擴展時，讓用戶選擇加載方式（URL 或本地文件）。

## 3. 超級重構（Super Refactor）

一個強大的項目重構工具，類似 IDE 的項目文件批量編輯/重構窗口。

**功能：**
- 從 VM 運行時動態提取項目全部文件（project.json、圖片、聲音等）
- 提供文件列表瀏覽
- 代碼/JSON 編輯、搜索過濾、SVG 預覽
- 自動換行、語法高亮、暗色主題適配
- `applyChanges` 將編輯後的文件回寫應用到 VM 項目
- `downloadProject` 下載項目

## 4. Gandi 擴展幫助（Gandi Help）

提供 Gandi 擴展庫的使用幫助說明（針對導入轉換項目時擴展未找到的解決方案）。

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 擴展編輯器窗口 | `src/components/extension-editor-window/extension-editor-window.jsx` |
| 加載方式選擇 | `src/components/tw-extension-load-choice-modal/` |
| 超級重構彈窗 | `src/containers/super-refactor-modal.jsx` |
| Gandi 幫助 | `src/components/gandi-help/gandi-help.jsx` |
