---
title: 防卡死計時器
sidebar_position: 12
---

# 防卡死計時器

防卡死計時器讓腳本檢查是否卡在長循環或無限循環中，並降到低幀率，而不是讓整個項目凍結直到循環結束。這可以防止大多數"項目無響應"的崩潰，但它有真實的性能代價，因此默認只在編輯器中開啟，播放器中不開啟。可以在[編輯器設置](/user-guide/settings)或通過 [`stuck` URL 參數](/website/url-parameters)（也接受 `warp_timer`）切換。

作為演示，考慮一個在"不刷新屏幕"積木內有無限循環的項目。開啟防卡死計時器後，項目會以低幀率（每秒幾幀）繼續渲染。關閉時，腳本永遠不會讓出，項目看起來像凍結了。

防卡死計時器以前被稱為"卡死檢查"。

## 另請參閱

- [自定義 FPS](/website/custom-fps)
- [URL 參數](/website/url-parameters)
- [編輯器設置](/user-guide/settings)
