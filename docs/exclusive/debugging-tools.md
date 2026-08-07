---
title: 调试与运行时工具
sidebar_position: 8
---

# 调试与运行时工具

RemixWarp 提供了一系列调试与运行时控制工具，这是 Bilup 中没有的。

## 1. 积木执行高亮（Editor Stepping）

为当前正在执行的积木添加彩色高亮边框，便于调试观察程序执行流程。

**设置项：**
- `highlight-color`：高亮颜色（默认 `#0000ff`）

## 2. 逐帧调试（Frame Stepper）

添加逐帧步进按钮（暂停时显示），允许精确地一次前进一帧，用于精确调试。

**功能：**
- 在舞台控制区（停止按钮旁）插入逐帧按钮
- 仅在暂停时显示（图标 `step.svg`）
- 依赖 debugger 模块

## 3. 暂停按钮（Pause）

在绿色旗帜旁添加暂停按钮，暂停/恢复项目。

**功能：**
- 在绿旗后添加暂停/播放按钮（`pause.svg` / `play.svg`）
- 快捷键 **Alt+X**（macOS 为 Option+X）可暂停/恢复

## 4. 积木统计（Block Count）

在编辑器菜单栏显示项目积木总数及详细复杂度分析。

**功能：**
- 点击积木计数可查看详细统计窗口（嵌套深度、脚本复杂度、积木类型分布等）
- 使用 WindowManager 窗口系统

**设置项：**
- `show_complexity_score`：显示复杂度评分
- `show_costume_count`：显示造型数
- `show_sound_count`：显示声音数
- `hide_block_count`：隐藏积木数

## 5. 按名称插入积木（Middle Click Popup）

中键/Shift+点击代码区，或按 Ctrl+Space 弹出积木搜索窗口，输入积木名（或部分）可搜索并拖入代码区添加积木。

**功能：**
- 中键 / Shift+点击代码区、Ctrl+Space 唤起搜索框
- 支持方向键、PageUp/Down、Home/End、Enter 导航
- Tab 自动补全
- 按住 Shift 拖出积木可防止菜单关闭
- 搜索支持数学计算和单位换算

**设置项：**
- `popup_scale`：弹窗积木尺寸（默认 48）
- `popup_width`：弹窗宽度（默认 16）
- `popup_max_height`：弹窗最大高度（默认 40）

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 积木执行高亮插件 | `src/addons/addons/editor-stepping/` |
| 逐帧调试插件 | `src/addons/addons/frame-stepper/` |
| 暂停插件 | `src/addons/addons/pause/` |
| 积木统计插件 | `src/addons/addons/block-count/` |
| 按名插入积木插件 | `src/addons/addons/middle-click-popup/` |
