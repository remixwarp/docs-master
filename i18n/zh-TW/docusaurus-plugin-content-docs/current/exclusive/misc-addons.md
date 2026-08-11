---
title: 其他獨有插件
sidebar_position: 10
---

# 其他獨有插件

RemixWarp 還提供了一系列 RemixWarp 中不存在的獨立插件（Addons）。

## 1. 批量顏色替換（Batch Color Replace）

批量替換當前角色所有造型中的指定顏色。

**功能：**
- 在顏色選擇器面板添加"批量替換"按鈕（綠色）
- 點擊後彈出 prompt 輸入新顏色（`#RRGGBB` 格式）
- 支持 SVG 造型（位圖/PNG 暫未實現）

## 2. 代碼風格（Coder Style）

極簡主義積木風格——僅彩色文本、無可見邊框、輸入框採用括號風格。

**設置項：**
- `block-opacity`：積木透明度（默認 0.02）
- `c-shape-opacity`：C 形積木透明度
- `boolean-opacity`：布爾積木透明度
- `input-opacity`：輸入積木透明度

## 3. VS Code 註釋同步（Comment VSCode Sync）

在 Scratch 編輯器與 VS Code 之間同步註釋（通過 WebSocket 連接 VS Code 擴展調試服務）。

**功能：**
- 檢測 `window.ScratchExtensionDebug` 連接狀態
- 同步工作區註釋與積木註釋

## 4. 語言包管理（Language Package）

允許加載和管理額外的語言包。

**功能：**
- 在"編輯"菜單添加"語言包管理"菜單項（lucide-globe 圖標）
- 打開 850×600 的窗口（WindowManager）
- 配合 `services/LanguageService.js` 實現：
  - 加載/保存用戶上傳的語言包（localStorage `userLanguagePackages`）
  - 生成包含全部翻譯鍵的語言包模板
  - 上傳語言包校驗（locale/name/translations 必填）
  - 多級回退翻譯（用戶包 → 系統文件 → 默認英文 → 原始鍵名）
  - 生成可用語言列表（支持用戶自定義 locale，如 `zh-cn-custom`）

**設置項：** `languagePackage`（啟用語言包，默認開啟）

## 5. 視頻錄製（Media Recorder）

在編輯器菜單欄添加"開始錄製"按鈕，錄製項目舞臺畫面為視頻。

**功能：**
- 菜單欄錄製按鈕
- 環境不支持 MediaRecorder 時標記為 `unsupported`

## 6. 自制積木增強（My Blocks Plus）

增強自定義積木（"我的積木"）的功能和靈活性。

**功能：**
- 創建項目時自動加載"我的積木增強"擴展
- 可隱藏自定義積木分類（`hideCustomBlocks` 設置）
- 隱藏 `scratchCategoryId-more` 分類

**警告：** 會加載新擴展，且無法從擴展管理器移除。

## 7. 舞臺相機（Stage Camera）

為舞臺添加相機控制功能，支持縮放、平移和全屏。使用視頻偵測或人臉檢測擴展時特別有用。

**功能：**
- 舞臺選擇器區域添加相機控制面板：放大/縮小/重置按鈕、窗口模式按鈕、縮放百分比輸入框

**設置項：**
- `showControls`：顯示相機控制（默認 false）
- `autoHide`：不使用時自動隱藏

## 8. 視頻彈窗（Video Modal）

視頻教程播放彈窗，讀取 `modals.videoModal` 與 `modals.videoModalData`（教程數據）。

## 9. 教程彈窗（Tutorial Modal）

教程內容彈窗，讀取 `modals.tutorialModal`。

## 10. Markdown 渲染器（Markdown Renderer）

通用 Markdown 渲染組件，支持標題/代碼/表格/公式，代碼可複製下載。

**入口：** 被 AI 面板、README 閱讀器等組件複用。

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 批量顏色替換 | `src/addons/addons/batch-color-replace/` |
| 代碼風格 | `src/addons/addons/coder-style/` |
| 註釋同步 | `src/addons/addons/comment-vscode-sync/` |
| 語言包管理 | `src/addons/addons/language-package/`、`src/components/language-package/LanguagePackageManager.jsx` |
| 視頻錄製 | `src/addons/addons/mediarecorder/` |
| 自制積木增強 | `src/addons/addons/my-blocks-plus/` |
| 舞臺相機 | `src/addons/addons/stage-camera/` |
| 視頻彈窗 | `src/containers/video-modal.jsx` |
| 教程彈窗 | `src/containers/tutorial-modal.jsx` |
| Markdown 渲染器 | `src/components/markdown-renderer/markdown-renderer.jsx` |
