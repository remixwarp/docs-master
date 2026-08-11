---
title: 賬號與安全
sidebar_position: 9
---

# 賬號與安全

RemixWarp 提供了賬號登錄與 RemixWarp 社區接入相關的功能，這是 RemixWarp 中沒有的。

## 1. RemixWarp 社區賬號登錄

RemixWarp/RemixWarp 賬號登錄彈窗，支持雲同步、動態發佈與編輯狀態分享。

**功能：**
- 登錄 RemixWarp/RemixWarp 賬號
- 雲同步設置
- 動態發佈
- 編輯狀態分享

**入口：** 菜單欄登錄按鈕彈出登錄彈窗（`bilup-login-modal`）。

## 2. Rotur 會話與登錄

通過 Rotur 會話接入社區平臺，支持登錄後發佈項目、關注他人、跨設備同步設置。

## 3. 新手引導（Onboarding）

首次進入編輯器時展示的分步新手引導教程覆蓋層。

**功能：**
- 分步引導（上一步/下一步/關閉）
- 聯動打開"設置/工具/AI/文件"菜單
- 首次進入時通過 localStorage `mw:has-seen-onboarding` 判斷觸發
- 監聽 `show-onboarding` 事件可重播

**狀態管理（reducer：onboarding）：**
- 狀態：`{ visible, step }`
- 動作：`SHOW` / `HIDE` / `NEXT` / `PREV` / `SKIP_ONBOARDING`

## 4. 兼容性轉換（TV/平臺兼容性）

將項目轉換為其他編輯器的兼容格式並下載。

**功能：**
- 通過 `window.__remixWarpMenuBarInstance.getCompatibilityIssues()` 獲取兼容性問題
- 通過 `handleCompatibilitySave()` 保存轉換結果

## 5. 關於窗口與免責聲明

"關於 RemixWarp"信息彈窗，說明與 RemixWarp 的關係及免責聲明。

## 相關代碼位置

| 模塊 | 路徑 |
|---|---|
| 登錄彈窗 | `src/components/menu-bar/bilup-login-modal.jsx` |
| Rotur 登錄 | `src/components/mw-rotur-login-modal/rotur-login-modal.jsx` |
| Rotur 會話 | `src/containers/rotur-session.jsx` |
| 新手引導容器 | `src/containers/onboarding.jsx` |
| 新手引導 reducer | `src/reducers/onboarding.js` |
| 兼容性轉換 | `src/components/tw-compatibility-modal/` |
| 關於窗口 | `src/components/mw-info-modal/info-window.jsx` |
