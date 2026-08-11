---
title: 貢獻概覽
sidebar_position: 1
---

# 為 RemixWarp 做貢獻

RemixWarp 是構建在 TurboWarp 之上的 Scratch 修改版，而 TurboWarp 本身構建在 Scratch 之上。這個譜系對貢獻者很重要：您將閱讀的大部分代碼是普通的 Scratch/TurboWarp 代碼，RemixWarp 特有的部分位於其上層。如果您以前為 Scratch 或 TurboWarp 做過貢獻，您已經掌握了大部分所需知識。

本節面向想參與 RemixWarp 本身開發的人：修復編輯器中的 bug、向 VM 添加積木、編寫插件，或運行自己的構建。如果您只想為自己的項目構建自定義擴展，請改讀[構建擴展](/building-extensions/introduction)，那不需要檢出源碼。

## 各部分在哪裡

RemixWarp 不是單一倉庫。它是幾個分叉的 Scratch 包加上少量 RemixWarp 專用服務的集合，並排檢出。詳細信息請參閱[項目結構](/contributing/project-structure)頁面，簡而言之：

- **scratch-gui** 是編輯器和社區站點，構建在同一個 webpack 構建中。這是您花大部分時間的地方。
- **scratch-vm** 運行項目並包含編譯器。積木在這裡定義。
- **scratch-render**、**scratch-blocks**、**scratch-paint** 和 **scratch-audio** 是其他分叉的引擎包。
- **packager** 將項目變成獨立的 HTML/可執行文件。
- **mistwarp-api** 是社區平臺後端。
- **docs** 就是這個站點。

## 開始之前

- RemixWarp 是一個大型應用。構建編輯器可能需要幾個 GB 的磁盤空間和內存。
- 您需要 [Git](https://git-scm.com/) 和較新的 [Node.js](https://nodejs.org/)（我們以 v20 作為開發目標；v18 或更高版本可能也可以）。
- scratch-gui 使用 [pnpm](https://pnpm.io/) 作為包管理器，而不是 npm。請參閱[構建與運行](/contributing/building-running)。

## 如何閱讀本節其餘部分

1. [項目結構](/contributing/project-structure) 解釋多倉庫佈局以及各包如何鏈接。
2. [構建與運行](/contributing/building-running) 是實際操作：克隆、安裝、鏈接、運行。
3. [測試](/contributing/testing) 涵蓋 scratch-gui 和 scratch-vm 中的測試套件。
4. [貢獻](/contributing/guidelines) 涵蓋工作流程：分支、樣式規則和拉取請求。
5. [部署](/contributing/deploying) 解釋構建如何發佈，以防您運行自己的實例。

如果您想在修改之前理解編輯器是如何組成的，[內部](/internals/overview) 部分是它的配套。

## 另請參閱

- [內部概覽](/internals/overview)
- [構建擴展](/building-extensions/introduction)
