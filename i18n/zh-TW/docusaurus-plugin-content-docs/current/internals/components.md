---
title: 組件
sidebar_position: 3
---

# 組件

scratch-gui 將其 React 代碼拆分為兩個扮演非常不同角色的目錄：`src/components/` 用於展示，`src/containers/` 用於接線。本頁描述組件側以及兩者之間的拆分。容器側在[容器](/internals/containers)中介紹。

## 容器/組件拆分

規則很簡單：

- **組件**（`src/components/`）渲染 UI。它通過 props 接收它需要的一切，不導入 Redux store 或 VM。給定相同的 props 它渲染相同的內容，這使它容易推理和複用。
- **容器**（`src/containers/`）知道 store 和 VM。它選擇組件需要的狀態、綁定回調，並用那些 props 渲染匹配的組件。

讓展示不知道數據來自哪裡，這就是同一個視覺組件可以在編輯器中被 Redux 驅動、在播放器中被不同狀態驅動、或在測試中被 props 驅動的原因。

並非每個文件都完美地落在線的一側。一些組件用 React hooks 或 `useState` 持有本地 UI 狀態（佈局測量、懸停、拖動），因為那種狀態不值得放進 Redux。`src/components/gui/gui.jsx` 是一個大例子：它在本地管理舞臺面板調整大小和窄佈局檢測，同時仍然從連接的容器接收其數據 props。組件避免的是直接觸及全局 store。

## 組件如何組織

每個組件是一個包含 `.jsx` 文件和同名匹配 CSS 模塊的文件夾，例如 `menu-bar/menu-bar.jsx` 和 `menu-bar/menu-bar.css`。JSX 將其樣式作為模塊導入：

```js
import styles from './menu-bar.css';
```

css-loader 對類名做哈希和駝峰化，因此 `styles.someClass` 解析為一個唯一的生成名。這使樣式作用於組件，這也是真正的全局 CSS 必須以不同方式導入的原因（請參閱[主題](/internals/theming)和[貢獻](/contributing/guidelines)中的 CSS 說明）。

顯示給用戶的文本通過 react-intl 的 `FormattedMessage` 和 `defineMessages`，而不是硬編碼字符串，因此界面可以翻譯。

## 主要組件樹

`src/components/gui/gui.jsx`（`GUIComponent`）是編輯器展示的根。它組合界面的主要區域，其中大多數本身是容器：

- 頂部的 `MenuBar`。
- 帶三個面板的標籤條：積木工作區（`Blocks`）、`CostumeTab` 和 `SoundTab`。
- `StageWrapper`，持有舞臺畫布，以及 `TargetPane`，角色和舞臺列表。
- 帶搜索和添加擴展按鈕的積木區頁腳，以及 `Watermark`。
- 每個模態框和覆蓋層：素材庫（造型、聲音、背景、擴展）、設置、git 模態框、還原點、調試器、警報、卡片等。許多隻在對應的 `...Visible` prop 為真時渲染。

設置 `isPlayerOnly` 時，同一個組件只渲染 `StageWrapper` 而不是完整編輯器，這就是播放器和嵌入視圖複用編輯器代碼的方式。

## 去哪裡看

一些您經常遇到的組件目錄：

- `components/gui/` 是頂層佈局。
- `components/menu-bar/` 是頂欄及其菜單。
- `components/stage/`、`components/stage-header/`、`components/target-pane/` 和 `components/sprite-selector/` 構建舞臺側。
- `components/loader/`、`components/box/`、`components/modal/` 等是小型共享積木。

許多編輯器功能（設置、自定義擴展、git 模態框、還原點等）以 `tw-` 或 `mw-` 為前綴，標記它們是在原始 Scratch 組件之上的 TurboWarp 或 RemixWarp 添加。

## 另請參閱

- [容器](/internals/containers)
- [架構](/internals/architecture)
- [狀態管理](/internals/state)
- [主題](/internals/theming)
