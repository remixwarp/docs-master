---
title: 插件系統
sidebar_position: 7
---

# 插件系統

插件是修改編輯器的小功能：編輯器調整、額外工具、外觀更改。RemixWarp 的插件框架繼承自 [Scratch Addons](https://scratchaddons.com/) 瀏覽器擴展，適配後在編輯器構建內部運行。本頁描述您最可能使用的兩個部分：設置存儲和窗口系統。

插件代碼位於 `src/addons/`。

## 插件從哪裡來

插件及其翻譯從 Scratch Addons 拉取，併為在 TurboWarp 和 RemixWarp 中使用打補丁。`src/addons/` 的大部分是生成的：`pull.js` 腳本獲取上游源碼、應用補丁並寫入 `addons/`、`addons-l10n/`、`libraries/` 和 `generated/` 文件夾。您通常不手動編輯這些。正如 addons README 所說，功能請求去上游，但由 TurboWarp 或 RemixWarp 移植引起的 bug 在這裡報告。

捆綁插件的列表定義在 `src/addons/addons.js` 中（僅由 `pull.js` 使用，不在運行時使用）。它包含 `editor-devtools`、`debugger`、`variable-manager`、`folders`、`block-switching` 等編輯器工具，以及為自定義積木主題提供動力的 `editor-theme3` 插件。

## 設置存儲

每個插件都有設置（至少包括它是否啟用）。所有這些由一個 `SettingsStore`（`src/addons/settings-store.js`）持有，通過 `src/addons/settings-store-singleton.js` 作為單例使用：

```js
import SettingsStore from './settings-store';

const settingStore = new SettingsStore();
const urlParameters = new URLSearchParams(location.search);
if (urlParameters.has('addons')) {
    settingStore.parseUrlParameter(urlParameters.get('addons'));
} else {
    settingStore.readLocalStorage();
}

export default settingStore;
```

啟動時 store 從 `localStorage`（鍵 `tw:addons`）加載設置，除非 `addons` URL 參數覆蓋它們。`SettingsStore` 擴展一個事件目標墊片，因此應用的其他部分訂閱它並在設置更改時做出反應。

它的主要職責：

- **讀取和持久化。** `readLocalStorage()` 和 `saveToLocalStorage()` 加載和存儲設置，`migrateSettings()` 升級較舊的保存格式（store 當前是第 5 版）。
- **查詢。** `getAddonEnabled(id)`、`getAddonSetting(id, settingId)`、`getAddonManifest(id)` 和 `getDefaultSettings(id)` 回答插件的當前配置是什麼，回退到清單默認值。
- **更改。** `setAddonEnabled(id, enabled)` 和 `setAddonSetting(id, settingId, value)` 更新值、持久化併發出更改事件，讓受影響的插件實時響應。`resetAddon()` 和 `resetAllAddons()` 恢復默認值。
- **導入和導出。** `export({theme})` 和 `import(data)` 在實例之間移動設置，`parseUrlParameter()` 應用在 URL 中傳入的設置。
- **條件。** `evaluateCondition()` 支持只在其他設置持有某些值時應用的插件設置。

設置 UI（在 `src/addons/settings/`）是這個 store 的一個視圖；更改控件調用 `setAddonSetting`，其餘由 store 完成。

## 窗口系統

一些插件打開自己的浮動面板（例如調試器和變量管理器）。與其讓每個插件重新發明，有一個共享窗口系統在 `src/addons/window-system/` 中，以 `window-manager.js` 為中心。

`window-manager.js` 導出一個 `WindowManager` 對象，一個用於創建和跟蹤窗口的小型 API：

```js
const WindowManager = {
    createWindow (options = {}) { /* ... */ },
    getWindow (id) { /* ... */ },
    getAllWindows () { /* ... */ },
    closeWindow (id) { /* ... */ },
    closeAllWindows () { /* ... */ },
    bringToFront (id) { /* ... */ }
};
```

它也作為 `window.wm` 全局暴露。

`createWindow` 根據環境返回兩個實現之一：

- **`AddonWindow`** 是在編輯器內部渲染的頁內可拖動、可調整大小的窗口。這是正常情況。
- **`NativeAddonWindow`** 在真正的操作系統窗口可用時（例如在桌面應用中）使用，通過 `window.open` 打開一個真正的彈出窗口並使其相對於主窗口定位。`createWindow` 只在原生窗口可以使用且窗口的 id 未被強制保持頁內時選擇這條路徑。

無論哪種方式，管理器都保持活動窗口的註冊表，以便查找它們、聚焦它們（`bringToFront`），並單獨或一次性關閉它們。通過此係統創建的窗口共享樣式和行為（滾動條、標題按鈕、焦點處理），因此插件獲得一致的窗口而無需每個都構建自己的。

## 另請參閱

- [編輯器插件](/editor/addons)
- [狀態管理](/internals/state)
- [主題](/internals/theming)
- [架構](/internals/architecture)
