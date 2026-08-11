---
title: 主題
sidebar_position: 6
---

# 主題

RemixWarp 主題是一組顏色和選項，變成文檔上的 CSS 自定義屬性，外加一組為工作區重新著色的積木顏色。本頁描述主題如何表示、如何應用，以及在主題系統附近工作時要注意的事項。

引擎位於 `src/lib/themes/`。

## 主題是什麼

主題是 `src/lib/themes/index.js` 中 `Theme` 類的一個實例。它是一個小的、不可變的選擇包：

- `accent`：強調色集合（來自 `src/lib/themes/accent/`）。
- `gui`：界面配色方案，`light`、`dark` 或 `midnight` 之一（來自 `src/lib/themes/gui/`）。
- `blocks`：積木調色板，`three`（默認）、`dark`、`high-contrast` 或 `custom` 之一。
- `menuBarAlign`、`wallpaper`、`fonts` 和一個用於更細選項的 `appearance` 對象。

`Theme` 是不可變的：`set(property, value)` 和 `setAppearance(changes)` 等方法返回一個新的 `Theme`，而不是修改現有的。它還按需計算派生的顏色映射，最重要的是：

- `getGuiColors()` 將強調色、GUI 和積木顏色合併到界面調色板中。
- `getBlockColors()` 產生積木調色板。
- `isDark()` 報告結果方案是否是深色的。

每個 GUI 方案的默認主題被預計算為 `Theme.defaults.light`、`Theme.defaults.dark` 等。

## 檢測起始主題

啟動時，`src/lib/themes/themePersistance.js` 決定使用哪個主題。它從 `localStorage`（`tw:theme`）讀取存儲的偏好，遷移遺留的 `"light"` / `"dark"` 值、按 UUID 恢復保存的自定義主題，或導入內聯的自定義主題。如果沒有存儲任何內容，它回退到系統偏好：`prefers-color-scheme: dark` 和 `prefers-contrast: more` 會被尊重。這就是 `theme` reducer 開始的值。

## 應用主題：CSS 自定義屬性

應用主題由 `src/lib/themes/guiHelpers.js` 中的 `applyGuiColors(theme)` 完成。它將 CSS 自定義屬性寫到文檔根（`document.documentElement`）上，使整個應用一次重新樣式化。粗略來說它：

- 將每個 GUI 顏色寫成根上的 `--<name>` 屬性（以及一個 `--<name>-default` 回退），例如 `--ui-primary`、`--looks-secondary`、`--text-primary`。
- 派生一些額外的，例如用於半透明覆蓋層的 `--ui-primary-rgb`。
- 將積木顏色寫成 `--editorTheme3-*` 屬性（按分類：primary、secondary、tertiary、字段背景，加上工作區、工具箱、浮動框、滾動條和網格顏色）。
- 計算菜單欄背景，並從其亮度計算可讀的 `--menu-bar-foreground`，然後用同樣方式計算 `--accent-foreground`。
- 更新 `<meta name="theme-color">` 標籤使瀏覽器 chrome 匹配。
- 應用壁紙並加載主題字體。

因為這些是設置在 `documentElement` 上的裸屬性名（不限作用域、無前綴），任何組件都可以用 `var(--...)` 消費它們。這是刻意的，也是社區站點必須將自己的自定義屬性加 `--mw-*` 前綴的原因：`--text` 這樣的無前綴名稱會與編輯器的衝突。請參閱[貢獻](/contributing/guidelines)中的 CSS 說明。

`applyGuiColors` 在主題首次設置時從 `theme` reducer 調用，並在主題更改時再次調用。`TWThemeManagerHOC` 位於頂層 HOC 棧的早期（請參閱[架構](/internals/architecture)），正是為了讓主題在圖標渲染前應用，避免錯誤顏色的閃現。

## 重新著色積木

界面從 CSS 變量即時重新樣式化，但積木工作區由 scratch-blocks（Blockly 分叉）繪製，需要的比 CSS 更多。`--editorTheme3-*` 屬性供注入的積木樣式表使用，更改積木顏色需要重新創建或重新著色工作區。編輯器在主題的積木身份（`theme.getBlocksThemeId()`）上重新鍵控 `Blocks` 組件，因此切換積木調色板會用新顏色重建工作區，而不是嘗試就地修改。

舞臺自己的積木顏色（在"碰到顏色"樣式功能運行時使用）來自 `getStageBlockColors()`，對於不是用來影響舞臺的積木主題，它回退到淺色調色板。

## 自定義主題

在內置方案之外，用戶可以構建自定義主題。它們在 `src/lib/themes/custom-themes.js`（`customThemeManager` 和 `CustomTheme` 類）中管理並按 UUID 存儲。自定義主題也可以嵌入到項目中，使打開項目時提供應用它的選項；該提示流程由 `mwProjectTheme` reducer 支撐（請參閱[狀態管理](/internals/state)）並由 VM 監聽器處理。

## 另請參閱

- [架構](/internals/architecture)
- [狀態管理](/internals/state)
- [插件系統](/internals/addons-system)
- [貢獻](/contributing/guidelines)
