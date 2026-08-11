---
title: URL 參數
sidebar_position: 3
---

# URL 參數

您可以通過向 URL 添加參數來控制 RemixWarp 加載和運行項目的方式。這對於分享可復現的設置、嵌入具有特定選項的項目或自動化測試非常有用。

參數使用標準的查詢字符串語法：URL 後加 `?`，然後是 `name=value` 對，用 `&` 連接。純開關參數不取值：

```
https://remixwarp.pages.dev/123456789?turbo&fps=60&username=alice
```

::::note
當您在編輯器中更改常用設置（渦輪模式、FPS、高質量畫筆、舞臺大小、插值）時，RemixWarp 會替您將它們存儲到 URL 中。下面的參數大多是您需要手動設置的"高級"參數，外加一些常用參數供參考。
::::

## 加載項目

| 參數 | 值 | 作用 |
|-----------|-------|--------------|
| (路徑) | 項目 ID | `remixwarp.pages.dev/123456789` 加載該項目 |
| `project_url` | 直接 URL | 從任意啟用 CORS 的 URL 加載 `.sb3`（或 `project.json`）。不要與項目 ID 組合使用。 |
| `clone` | git 倉庫 URL | 從 RemixWarp git 倉庫克隆項目（請參閱[Git 集成](/user-guide/git)）。 |

`project_url` 需要一個支持 [CORS](/website/cors)（`Access-Control-Allow-Origin: *`）的直接下載。省略協議時默認使用 `https://`；`http://` URL 通常無法工作。[GitHub Pages](https://pages.github.com/) 非常適合此項。

```
https://remixwarp.pages.dev/?project_url=https://example.com/project.sb3
```

## 性能與運行時

| 參數 | 值 | 作用 |
|-----------|-------|--------------|
| `fps` | 數字 | 設置[幀率](/website/custom-fps)。`0` 以顯示器刷新率運行。 |
| `turbo` | 開關 | 啟用[渦輪模式](/website/warp-timer)（不限制每幀節流）。 |
| `interpolate` | 開關 | 啟用[插值](/website/interpolation)以獲得更平滑的運動。 |
| `hqpen` | 開關 | 啟用[高質量畫筆](/website/high-quality-pen)。 |
| `limitless` | 開關 | 移除[雜項限制](/website/remove-limits)。 |
| `offscreen` | 開關 | [移除圍欄](/website/remove-fencing)，讓角色可以離開舞臺。 |
| `clones` | 數字 | 設置最大克隆數（請參閱[無限克隆](/website/infinite-clones)）。 |
| `stuck` | 開關 | 啟用[防卡死計時器](/website/warp-timer)。也接受 `warp_timer`。 |
| `nocompile` | 開關 | [禁用編譯器](/website/disable-compiler)。您幾乎永遠不會想用它。 |

## 顯示

| 參數 | 值 | 作用 |
|-----------|-------|--------------|
| `size` | `寬度x高度` | 設置[自定義舞臺大小](/website/custom-stage-size)，例如 `size=640x360`。 |
| `scale` | 數字 | 限制舞臺允許放大的程度。`scale=1` 保持其原生分辨率。 |
| `fullscreen-background` | CSS 顏色 | 全屏時顯示的背景顏色。將 `#` 轉義為 `%23`，例如 `%23abc123`。 |

## 賬戶與雲 {#accounts-and-cloud}

| 參數 | 值 | 作用 |
|-----------|-------|--------------|
| `username` | 字符串 | 設置 `用戶名` 積木返回的值，並用於[雲變量](/website/cloud-variables)。以這種方式設置的用戶名不會保存。 |
| `cloud_host` | `wss://...` URL | 將[雲變量](/website/cloud-variables#cloud-host)指向不同的服務器。默認為 `wss://clouddata.turbowarp.org`。 |

## 協作

| 參數 | 值 | 作用 |
|-----------|-------|--------------|
| `room` | 房間代碼 | 設置用戶名後自動加入實時[協作](/user-guide/collaboration)房間。參數讀取後會被從 URL 中移除。 |

## 擴展 {#extension}

| 參數 | 值 | 作用 |
|-----------|-------|--------------|
| `extension` | URL | 加載自定義擴展。可以重複以加載多個。 |

```
https://remixwarp.pages.dev/?extension=https://example.com/a.js&extension=https://example.com/b.js
```

這些擴展的用法請參閱[構建擴展](/extensions/introduction)。

## 僅嵌入參數

以下參數僅適用於[嵌入播放器](/website/embedding)：

| 參數 | 值 | 作用 |
|-----------|-------|--------------|
| `autoplay` | 開關 | 項目加載後自動點擊綠旗。 |
| `addons` | 逗號列表 | 在嵌入中啟用特定插件，例如 `addons=pause,gamepad`。 |
| `settings-button` | 開關 | 在嵌入中顯示高級設置按鈕。 |

## 另請參閱

- [嵌入](/website/embedding)
- [雲變量](/website/cloud-variables)
- [CORS](/website/cors)
- [編輯器設置](/user-guide/settings)
