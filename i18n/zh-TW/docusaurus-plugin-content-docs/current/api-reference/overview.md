---
title: API 參考概覽
sidebar_position: 1
---

RemixWarp 由一組 JavaScript 包構建：`scratch-vm`（運行項目的引擎）、`scratch-render`（WebGL 渲染器）、`scratch-blocks`（積木編輯器）和 `scratch-gui`（將它們整合在一起並同時提供社區站點的 React 應用）。本節記錄這些包暴露的程序化表面。

它面向高級用戶、擴展作者以及在自己的頁面中嵌入 RemixWarp 的人。如果您只想製作項目，您不需要這些。如果您想編寫腳本控制運行中的項目、構建擴展或自己驅動 VM，從這裡開始。

## 訪問運行中的實例

編輯器或播放器打開時，scratch-gui 將兩個對象放在 `window` 上用於調試和腳本編寫：

- `window.vm` 是實時的 [`VirtualMachine`](/api-reference/vm-api) 實例。VM 管理器掛載後設置一次（請參閱 `src/lib/components/vm-manager-hoc.jsx`）。
- `window.ReduxStore` 是應用的 Redux store（請參閱 `src/lib/components/app-state-hoc.jsx`），對檢查 GUI 狀態很有用。

在編輯器上打開瀏覽器控制台並嘗試：

```js
// 運行當前項目的 VM
window.vm

// 啟動項目，就像點擊了綠旗
window.vm.greenFlag();

// 渲染器，如果已附加
window.vm.renderer

// 引擎運行時（目標、線程、積木、IO 設備）
window.vm.runtime
```

這些全局變量用於交互式使用。它們不是穩定的、帶版本的 API，並且可能隨構建而更改。擴展應該改用[擴展 API](/api-reference/extension-api)，它會顯式傳遞 `Scratch.vm`。

## 各層

- [VM API](/api-reference/vm-api)：公開的 `VirtualMachine` 類。加載和保存項目、控制播放、管理角色/造型/聲音，以及讀取狀態。這是嵌入者對話的對象。
- [GUI API](/api-reference/gui-api)：scratch-gui 導出的 React 入口點，讓您可以在自己的應用中渲染編輯器或播放器。
- [擴展 API](/api-reference/extension-api)：擴展作者針對其編寫的 `Scratch` 對象（`BlockType`、`ArgumentType`、`Scratch.extensions.register` 以及沙箱權限輔助工具）。
- [積木註冊](/api-reference/block-registration)：操作碼和帽子如何接入運行時。
- [線程](/api-reference/threads)：實際執行腳本的線程和序列器模型。
- [運行時 API](/api-reference/runtime)：持有目標、IO 設備、監視器並啟動線程的引擎（`vm.runtime`）。
- [插件 API](/api-reference/addon-api)：userscript 接收的 `addon` 對象。
- [事件](/api-reference/events)：VM 發出的事件。
- [實用工具](/api-reference/utilities)：`Cast`、`Color` 和 `MathUtil` 等輔助模塊。

## 嵌入

如果您想在自己的頁面上放置 RemixWarp 項目，通常不需要直接針對 VM 構建；您使用[打包器](/packager/overview)或[嵌入 iframe](/advanced/embedding)。只有當您需要這些工具不給您的控制時，才直接針對 VM/GUI 構建。

## 另請參閱

- [構建擴展](/building-extensions/introduction)
- [內部：架構](/internals/architecture)
- [項目中的 JavaScript](/advanced/javascript)
