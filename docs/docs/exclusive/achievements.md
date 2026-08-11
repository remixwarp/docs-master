---
title: 成就系统
sidebar_position: 3
---

# 成就系统

RemixWarp 内置了一套完整的**成就系统**，这是 RemixWarp 中没有的功能。玩家在使用编辑器、创建项目、与 AI 交互时，会根据行为自动解锁成就并积累经验值。

## 核心组件

### 1. 成就展示面板（Achievements）

一个展示所有成就的奖杯面板。

**功能：**
- 列出全部成就
- 按分类展示
- 显示解锁状态与经验值
- 可切换分类

**入口：** 编辑器内成就/奖杯面板弹窗。

### 2. 成就监听器（Achievement Tracker）

后台运行的成就监听器，根据 VM 运行时行为自动解锁成就。

**可触发成就的行为包括：**
- 循环积木执行
- 运动积木执行
- 控制积木执行
- AI 对话
- 高帧率运行
- 赞助（Sponsor Intent）
- 协作聊天

### 3. 成就核心（lib/achievements.js）

成就系统的核心数据与逻辑模块。

**功能：**
- 成就定义列表
- 解锁逻辑
- 经验值管理
- 本地存储
- 记录 AI 对话、赞助、高帧率、协作聊天等成就

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 成就展示面板 | `src/components/achievements/achievements.jsx` |
| 成就监听器 | `src/components/achievements/achievement-tracker.jsx` |
| 成就核心逻辑 | `src/lib/achievements.js` |
