---
title: 分享您的擴展
sidebar_position: 13
---

# 分享您的擴展

要分享擴展，您需要有地方託管它。

如果您只想在自己的項目中使用自己的擴展，並與[打包器](/packager/overview)一起分發它們，您不需要託管或提交任何東西。打包器總是將擴展捆綁並作為導出項目的一部分以非沙箱方式運行。

## 沙箱擴展

[沙箱擴展](/building-extensions/sandbox)可以託管在任何通過 HTTPS 提供靜態文件的地方。[GitHub Pages](https://pages.github.com/) 是常見選擇。注意 GitHub 的 `raw.githubusercontent.com` 鏈接**不能**作為擴展 URL；請改用 GitHub Pages（或其他靜態主機）。

一旦它在公開的 HTTPS URL 上，就在編輯器中使用"添加擴展"、"自定義擴展"和該 URL 加載它，或用 `?extension=<url>` 自動加載。

## 非沙箱擴展

[非沙箱擴展](/building-extensions/unsandboxed)只從受信任的來源自動以非沙箱方式運行（請參閱[非沙箱頁面](/building-extensions/unsandboxed)上的受信任前綴）。由於您不控制那些畫廊域名，實際可行的選項是：

- **自己託管並讓用戶選擇加入。** 像上面一樣在任何公開 HTTPS URL 上提供服務。當有人加載該 URL 時，RemixWarp 會以沙箱方式加載它，除非他們明確選擇信任它，因此請為您的用戶記錄該步驟。
- **將其放入 RemixWarp 擴展畫廊。** 畫廊位於 [extensions.bilup.org](https://extensions.bilup.org)；從該來源提供的擴展自動以非沙箱方式運行。請遵循畫廊網站上的提交說明。

## 下一步

[結束](/building-extensions/wrapping-up)。
