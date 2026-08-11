---
title: 項目結構
sidebar_position: 2
---

# 項目結構

RemixWarp 是一個多倉庫工作區。每個包都是自己的 Git 檢出，它們作為同一個父目錄中的同級放置，以便相互鏈接。父目錄本身不是一個倉庫。

```
bilup/
├── scratch-gui/       # 編輯器 + 社區站點（同一個 webpack 構建）
├── scratch-vm/        # 運行時和編譯器；積木在這裡定義
├── scratch-blocks/    # 積木編輯器（Blockly 分叉）
├── scratch-render/    # WebGL 舞臺渲染器
├── scratch-paint/     # 造型和背景編輯器
├── scratch-audio/     # Web Audio 播放
├── packager/          # 獨立項目打包器
├── unpackager/        # 打包器的逆向
├── mistwarp-api/      # 社區平臺後端
├── turbowarp-desktop/ # 編輯器的桌面包裝
└── docs/              # 本文檔站點（Docusaurus）
```

## 各包

Scratch 被拆分為分別實現應用一部分的包。RemixWarp 分叉了其中幾個。

- **scratch-gui** 實現大部分界面（菜單欄、角色列表、標籤頁），將它們組合在一起，並且是插件所在的地方。它是一組 React 組件加上一個 Redux store。RemixWarp 獨有的，同一個構建還提供社區站點。
- **scratch-vm** 運行項目。它持有積木定義（`src/user-guide/scratch3_*.js`）、擴展（`src/extensions/`）以及將積木變成 JavaScript 的編譯器（`src/compiler/`）。
- **scratch-render** 繪製舞臺：角色、畫筆、文本氣泡和"碰到"等碰撞積木。注意變量監視器等覆蓋層由 scratch-gui 繪製，而不是 scratch-render。
- **scratch-blocks** 是積木區和工作區，Google Blockly 的一個分叉。其 `core/` 目錄下的編輯需要 Closure 重新編譯（請參閱[構建與運行](/development/building-running)）。
- **scratch-paint** 是造型和背景編輯器。
- **scratch-audio** 處理聲音播放。

另外兩個支持包作為 npm 依賴而不是本地檢出引入，但您會看到它們的引用：**scratch-parser**（驗證 sb2/sb3 文件）和 **@turbowarp/scratch-storage**（用於下載資產的 fetch 抽象）。

## scratch-gui 內部

scratch-gui 是大多數編輯器工作發生的地方。重要的源目錄：

```
scratch-gui/src/
├── components/    # 展示性 React 組件（foo/foo.jsx + foo.css）
├── containers/    # 圍繞組件的 Redux 連接包裝
├── reducers/      # Redux reducer，每個狀態切片一個文件
├── lib/           # 共享服務層、HOC、主題、持久化
├── addons/        # 插件系統（設置存儲、窗口系統、插件）
├── playground/    # webpack 入口點（編輯器、播放器、社區、嵌入、...）
└── community/     # 社區單頁應用
```

- `components/` 持有純 UI。每個組件是一個帶 `.jsx` 和匹配 CSS 模塊的文件夾。
- `containers/` 將組件連接到 Redux store。請參閱[容器模式](/gui-internals/containers)。
- `reducers/` 是 Redux 狀態。請參閱[狀態管理](/gui-internals/state)。
- `lib/` 是最大的目錄：`lib/components/` 下的高階組件、`lib/themes/` 下的主題引擎、`lib/persistence/` 下的項目持久化，加上編輯器與社區站點都使用的 RemixWarp 服務層 `lib/community/` 和 `lib/rotur/`。
- `addons/` 是插件框架，從 Scratch Addons 移植。請參閱[插件系統](/gui-internals/addons-system)。

構建產生幾個入口點，定義在 `src/playground/` 下：`editor`、`player`、`community`、`fullscreen`、`embed`、`addons` 和 `credits`。路由被處理為 `/editor` 提供編輯器，`/embed.html` 提供嵌入播放器，`/project/*` 和 `/explore` 等客戶端路由提供社區應用。

## 各包如何鏈接

開發期間引擎包不是從 npm 獲取的。它們從本地檢出 symlink 鏈接，因此例如 scratch-vm 的更改會出現在編輯器中而無需重新發布。scratch-gui 在其 `pnpm.overrides` 中聲明這些鏈接並暴露一個輔助腳本：

```bash
pnpm run link
# 運行：pnpm link ../scratch-vm ../scratch-blocks ../scratch-render ../scratch-paint
```

這意味著您的目錄佈局很重要：引擎包必須是 scratch-gui 的同級，如上所示。

## RemixWarp 專用服務

兩個部分根本不是 Scratch 或 TurboWarp 代碼：

- **mistwarp-api** 是社區後端（賬戶、項目、評論、通知、設置同步）。它用 OSL 編寫，將數據存儲為扁平 JSON，對項目 blob 使用 Cloudflare R2。前端在 `https://mwapi.mistium.com/api` 與它通信。
- 身份和社交功能通過 **Rotur** 運行。登錄將 Rotur 令牌換成 RemixWarp 會話；社交功能（帖子、點贊、關注）轉到 `https://api.rotur.dev`。

您不需要兩者都運行來參與編輯器本身的工作。它們在做社區站點時才有意義。

## 另請參閱

- [構建與運行](/development/building-running)
- [內部概覽](/gui-internals/overview)
