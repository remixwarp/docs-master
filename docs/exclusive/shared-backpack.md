---
title: 协作共享背包
sidebar_position: 6
---

# 协作共享背包

RemixWarp 在协作模式中提供了**共享背包（Shared Backpack）** 功能，允许团队中的多个成员共享素材。这是 Bilup 中没有的功能。

## 功能

- **创建共享背包**：为协作房间创建共享背包，支持命名、添加成员、设置角色
- **共享素材列表**：查看背包内成员与物品数量
- **多用户实时同步**：通过 `CollaborationService` 发送/监听 `shared-backpack-create` / `shared-backpack-updated` / `shared-backpack-deleted` 事件，实现多用户实时同步
- **加载共享背包**：通过 `sharedBackpackAPI` 创建/加载共享背包

## 界面组件

### 1. 共享背包列表（SharedBackpack）

协作房间内共享的背包面板，展示成员与物品数量。

### 2. 创建共享背包对话框（SharedBackpackCreateDialog）

创建共享背包的对话框，包含命名、添加成员、角色设置。

## 状态管理

对应的 reducer（`shared-backpack.js`）已在根 reducer 中正式接入：

- 状态：`{ backpacks: [], selectedBackpackId, createDialogOpen }`
- 动作：`SET` / `ADD` / `UPDATE` / `REMOVE` / `SELECT_SHARED_BACKPACK` / `OPEN` / `CLOSE_CREATE_DIALOG`

## 相关代码位置

| 模块 | 路径 |
|---|---|
| 共享背包组件 | `src/components/backpack/shared-backpack.jsx` |
| 创建对话框 | `src/components/backpack/shared-backpack-create-dialog.jsx` |
| 容器 | `src/containers/shared-backpack.jsx` |
| Reducer | `src/reducers/shared-backpack.js` |
| API | `src/lib/api/shared-backpack.js` |
| 协作服务 | `src/lib/collaboration-service.js` |

## 说明

共享背包的 UI 容器（`shared-backpack.jsx`）在源码中尚未挂载到主界面，但其 reducer 已正式接入根 reducer，功能逻辑完整，属于"已实现但界面待启用"的模块。
