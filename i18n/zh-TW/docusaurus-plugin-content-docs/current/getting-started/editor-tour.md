---
title: 編輯器導覽
sidebar_position: 4
---

# 編輯器導覽

這是 RemixWarp 編輯器的導覽。每個區域都鏈接到其完整的參考頁面。關於各區域如何組合的概述，請參閱[編輯器界面](/editor/interface)。

編輯器在頂欄下方分為三列：

- 頂部是**菜單欄**，
- 左側和中間是**積木區**和**工作區**（位於代碼標籤頁），
- 右側是**舞臺**和**角色區**。

## 菜單欄

頂部的橫條包含**文件**和**編輯**菜單、項目標題、**設置**菜單，以及（登錄後）您的賬戶和通知。從這裡您可以創建、保存、加載、打包和發佈項目，也可以訪問插件、還原點、git 和教程。

- 文件與編輯菜單、保存、發佈和打包：[菜單欄](/editor/menu-bar)
- 編輯器自身的偏好設置：[設置](/editor/settings)

## 三個編輯器標籤頁

積木區上方有三個標籤頁，用於切換左側和中間列顯示的內容：

- **代碼**顯示積木區和工作區（見下文）。
- **造型**顯示所選角色造型的畫板編輯器（選中舞臺時顯示**背景**）。請參閱[造型](/editor/costumes)。
- **聲音**顯示聲音編輯器。請參閱[聲音](/editor/sounds)。

## 積木區

在代碼標籤頁中，左側列出所有積木，按類別分組（運動、外觀、聲音、事件、控制、偵測、運算、變量、自制積木），擴展位於下方。將積木從拖到這裡到工作區。

- 積木區本身：[積木區](/editor/blocks-palette)
- 每個分類的用途：[積木概覽](/blocks/overview)
- 添加擴展積木：[擴展概覽](/extensions/overview)

## 工作區

中間區域用於通過吸附積木來組裝腳本。它支持右鍵菜單、註釋和清理，以及 RemixWarp 自己用於查找和組織代碼的工具。

- 工作區本身：[工作區](/editor/workspace)
- 跳轉到任意積木或變量：[查找欄](/editor/find-bar)
- 在大型項目中保存並跳轉到指定位置：[書籤](/editor/bookmarks)
- 定義自己的積木：[自制積木](/editor/custom-blocks)

## 舞臺

右上方是舞臺，項目在其中運行，其上方有綠旗和停止按鈕。舞臺下方是用於選擇和編輯背景的**舞臺選擇器**。

- 舞臺及其控制：[舞臺](/editor/stage)
- 運行限制和渲染選項：[自定義舞臺大小](/advanced/custom-stage-size)和[自定義 FPS](/advanced/custom-fps)

## 角色區

右側舞臺下方是角色列表，上方是角色信息控制（名稱、位置、大小、可見性），角落有添加角色按鈕。

- 管理角色：[角色](/editor/sprites)
- 跨項目複用角色、造型、聲音和腳本：[背包](/editor/backpack)

## 變量與數據

變量和列表在積木區的**變量**類別中創建，並作為監視器顯示在舞臺上。RemixWarp 增加了一個管理器，可同時處理大量變量。

- 使用變量和列表：[變量](/editor/variables)
- 批量編輯和檢查：[變量管理器](/editor/variable-manager)

## RemixWarp 工具

以下是從菜單和設置中訪問的、RemixWarp 在標準編輯器之外新增的功能：

- 可選的編輯器和播放器功能：[插件](/editor/addons)
- 配色方案和深色模式：[主題](/editor/themes)
- 單步執行運行中的項目：[調試器](/editor/debugger)
- 自動保存和手動快照：[還原點](/editor/restore-points)
- 版本控制：[Git](/editor/git)
- 實時協作編輯項目：[協作](/editor/collaboration)
- 構建獨立版本：[打包](/editor/packaging)
- 重新綁定編輯器快捷鍵：[快捷鍵](/editor/shortcuts)

## 另請參閱

- [編輯器界面](/editor/interface)
- [快速開始](/getting-started/quick-start)
- [項目管理](/editor/project-management)
