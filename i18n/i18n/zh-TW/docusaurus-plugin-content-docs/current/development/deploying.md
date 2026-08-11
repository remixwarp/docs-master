---
title: 部署
sidebar_position: 6
---

# 部署

RemixWarp 的編輯器是一個靜態站點。生產構建是一個 HTML、JavaScript 和資產文件夾，可以由任何靜態主機提供。本頁介紹如何構建和發佈該文件夾，這是您運行自己的編輯器實例時需要的。

貢獻更改不需要這個。只有當您想自己託管構建時它才重要。

## 構建輸出

scratch-gui 的生產構建由以下命令產生：

```bash
NODE_ENV=production pnpm run build
```

這會清理之前的輸出並運行 webpack，將可部署的站點寫入 `build/` 目錄。`build/` 下的所有內容都是靜態且自包含的。

## 部署腳本

scratch-gui 附帶一個 `deploy` 腳本，一步構建併發布到 `gh-pages` 分支：

```bash
pnpm run deploy
```

在底層它運行：

```bash
NODE_ENV=production pnpm run build && \
  touch build/.nojekyll && \
  cp -r functions build/functions && \
  gh-pages -t -d build -m "Build for <commit hash>"
```

按順序，它：

- 做一次生產構建，
- 添加 `.nojekyll` 標記，讓主機不在輸出上運行 Jekyll，
- 將 `functions/` 目錄複製到構建中（這些是用於路由和動態行為的 Cloudflare Pages Functions），
- 用 `gh-pages` 工具將整個 `build/` 目錄推送到 `gh-pages` 分支。

提交到默認分支不會部署任何東西。發佈是刻意的 `pnpm run deploy`。

## 託管構建

因為輸出是靜態的，您可以從任何靜態主機提供它。RemixWarp 的設置發佈 `gh-pages` 分支並將主機指向它。

### Cloudflare Pages

構建中的 `functions/` 目錄是為 [Cloudflare Pages Functions](https://developers.cloudflare.com/pages/functions/) 編寫的，因此 Cloudflare Pages 是預期的主機。典型設置：

1. 創建一個連接到您的 `scratch-gui` fork 的 Pages 項目。
2. 在項目設置中，將生產分支設置為 `gh-pages` 併為其啟用自動部署。
3. 每當您想發佈時在本地運行 `pnpm run deploy`。Cloudflare 檢測 `gh-pages` 上的新提交併部署它。

因為您在本地構建並推送完成的 `build/` 目錄，Cloudflare 不需要運行自己的構建步驟。

### 其他靜態主機

任何可以提供目錄的主機都可以：GitHub Pages、普通 Web 服務器、帶靜態託管的對象存儲等。要保留兩件事：

- 保留 `.nojekyll` 標記（或主機的等價物），使以下劃線開頭的文件名不被剝離。
- 復現路由。同一個構建從一組文件提供多個應用（`/editor`、`/embed.html`、社區客戶端路由和遺留播放器路由）。在 Cloudflare Pages 上 `functions/` 目錄處理此問題；在另一個主機上您必須實現等價的重寫，否則客戶端路由會在重新加載時 404。

## 社區後端

編輯器構建只是前端。如果您也運行社區平臺，後端（mistwarp-api）是一個單獨的 OSL 服務，不是這個靜態構建的一部分。它單獨部署和運行；它是什麼請參閱[項目結構](/development/project-structure)。僅託管編輯器不需要它。

## 另請參閱

- [構建與運行](/development/building-running)
- [項目結構](/development/project-structure)
- [貢獻](/development/guidelines)
