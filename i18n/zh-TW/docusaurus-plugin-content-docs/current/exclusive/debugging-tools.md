---
title: 調試與運行時工具
sidebar_position: 8
---

# 調試與運行時工具

RemixWarp 提供了一系列調試與運行時控制工具，這是 RemixWarp 中沒有的。

## 1. 積木執行高亮（Editor Stepping）

為當前正在執行的積木添加彩色高亮邊框，便於調試觀察程序執行流程。

**設置項：**
- `highlight-color`：高亮顏色（默認 `#0000ff`）

## 2. 逐幀調試（Frame Stepper）

添加逐幀步進按鈕（暫停時顯示），允許精確地一次前進一幀，用於精確調試。

**功能：**
- 在舞臺控制區（停止按鈕旁）插入逐幀按鈕
- 僅在暫停時顯示（圖標 `step.svg`）
- 依賴 debugger 模塊

## 3. 暫停按鈕（Pause）

在綠色旗幟旁添加暫停按鈕，暫停/恢復項目。

**功能：**
- 在綠旗後添加暫停/播放按鈕（`pause.svg` / `play.svg`）
- 快捷鍵 **Alt+X**（macOS 為 Option+X）可暫停/恢復

## 4. 積木統計（Block Count）

在編輯器菜單欄顯示項目積木總數及詳細複雜度分析。

**功能：**
- 點擊積木計數可查看詳細統計窗口（嵌套深度、腳本複雜度、積木類型分佈等）
- 使用 WindowManager 窗口系統

**設置項：**
- `show_complexity_score`：顯示覆雜度評分
- `show_costume_count`：顯示造型數
- `show_sound_count`：顯示聲音數
- `hide_block_count`：隱藏積木數

## 5. 按名稱插入積木（Middle Click Popup）

中鍵/Shift+點擊代碼區，或按 Ctrl+Space 彈出積木搜索窗口，輸入積木名（或部分）可搜索並拖入代碼區添加積木。

**功能：**
- 中鍵 / Shift+點擊代碼區、Ctrl+Space 喚起搜索框
- 支持方向鍵、PageUp/Down、Home/End、Enter 導航
- Tab 自動補全
- 按住 Shift 拖出積木可防止菜單關閉
- 搜索支持數學計算和單位換算

**設置項：**
- `popup_scale`：彈窗積木尺寸（默認 48）
- `popup_width`：彈窗寬度（默認 16）
- `popup_max_height`：彈窗最大高度（默認 40）

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 積木執行高亮插件 | `src/addons/addons/editor-stepping/` |
| 逐幀調試插件 | `src/addons/addons/frame-stepper/` |
| 暫停插件 | `src/addons/addons/pause/` |
| 積木統計插件 | `src/addons/addons/block-count/` |
| 按名插入積木插件 | `src/addons/addons/middle-click-popup/` |
