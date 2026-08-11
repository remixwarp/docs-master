---
title: 插件 API
sidebar_position: 7
---

插件是修改編輯器和播放器的 userscript 和 userstyle。每個插件是 `scratch-gui/src/addons/addons/` 下的一個文件夾，帶有一個清單和一個或多個腳本。當插件的 userscript 運行時，它接收一個 API 對象。本頁是該對象的參考，定義在 `scratch-gui/src/addons/api.js`。插件是什麼以及如何使用請參閱[插件](/editor/addons)。

## userscript 入口點

插件 userscript 導出一個接收 API 對象的默認異步函數：

```js
export default async function ({addon, console, msg}) {
    const vm = addon.tab.traps.vm;
    // ... 修改編輯器 ...
}
```

傳入的對象具有以下成員：

- `addon`：插件 API，分為 `addon.tab`、`addon.settings` 和 `addon.self`（見下文）。
- `console`：瀏覽器控制台。
- `global`：全局對象。
- `msg(key, vars)`：來自插件翻譯的本地化消息。
- `safeMsg(key, vars)`：相同，但經過 HTML 轉義。

## addon.tab

`addon.tab` 是觸及頁面的主要表面。它是一個事件目標。

- `tab.traps`：到編輯器內部的逃生艙口：
  - `traps.vm`：實時的 [`VirtualMachine`](/api-reference/vm-api)。
  - `traps.getBlockly()`：在 Blockly 實例就緒後解析它。
  - `traps.getWorkspace()`：當前的 Blockly 工作區。
  - `traps.getPaper()`：在造型編輯器打開時解析 paper.js 作用域。
- `tab.redux`：訪問 GUI 的 Redux store，包括 `tab.redux.state` 和 `statechanged` 事件。
- `tab.waitForElement(selector, options)`：在匹配的 DOM 元素出現後解析它。選項包括 `markAsSeen`（這樣同一元素不會返回兩次）、`condition` 回調、`reduxCondition` 回調和 `reduxEvents` 以等待特定的 store 操作。
- `tab.appendToSharedSpace({space, element, order, scope})`：將元素插入已知的編輯器區域（例如 `stageHeader`），相對於其他插件保持在穩定位置。
- `tab.createBlockContextMenu(callback, {workspace, blocks, flyout, comments})`：向積木或工作區上下文菜單添加項目。
- `tab.scratchClass(...names, {others})`：將 RemixWarp 的哈希 CSS 類名（例如 `green-flag`）解析為它們真實的運行時類名，讓您的樣式和查詢匹配。
- `tab.scratchMessage(id)`：查找編輯器自己本地化字符串之一。
- `tab.copyImage(dataURL)`：將 PNG 數據 URL 複製到剪貼板。
- `tab.createModal(title, {isOpen})`、`tab.confirm(...)`、`tab.prompt(...)`：編輯器風格的對話框。
- `tab.displayNoneWhileDisabled(el, options)`：在插件被禁用時隱藏元素。
- `tab.editorMode`：當前編輯器模式字符串。
- `tab.direction`：當前語言環境的 `'ltr'` 或 `'rtl'`。
- `tab.recolorable()`：一個 `<img>`，其 SVG 根據當前主題強調色重新著色。

## addon.settings

`addon.settings` 讀取插件自己的設置，按其清單聲明。它是一個事件目標。

- `settings.get(id)`：設置的當前值。
- 監聽 `change` 事件以在用戶更改設置時做出反應：

```js
addon.settings.addEventListener('change', () => {
    const speed = addon.settings.get('speed');
    // ... 應用新值 ...
});
```

## addon.self

`addon.self` 是插件自己的狀態。它是一個事件目標。

- `self.id`：插件的 ID。
- `self.disabled`：插件當前是否被禁用。
- `self.getResource(path)`：將捆綁的資源路徑解析為可用的 URL。
- 當用戶打開編輯器時切換插件時，會觸發 `disabled` 和 `reenabled` 事件，因此插件無需重新加載即可清理或重新應用其更改：

```js
addon.self.addEventListener('disabled', () => { /* 撤銷更改 */ });
addon.self.addEventListener('reenabled', () => { /* 重做更改 */ });
```

## Userstyles

插件還可以攜帶 CSS。靜態樣式表自動應用，設置可以驅動 CSS 自定義屬性：清單設置產生名為 `--<addonId>-<settingId>` 的變量，清單 `customCssVariables` 可以計算在設置更改時更新的顏色（混合、增亮、閾值等）。

## 另請參閱

- [插件](/editor/addons) 瞭解面向用戶的功能
- [內部：插件系統](/internals/addons-system)
- [VM API](/api-reference/vm-api)
