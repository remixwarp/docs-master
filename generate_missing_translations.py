from pathlib import Path
import re

source_root = Path(r'e:\RemixWarp\docs-master\docs')
target_root = Path(r'e:\RemixWarp\docs-master\i18n\zh\docusaurus-plugin-content-docs\current')

missing = [
    'development/components/extensions-library/adding-tags.md',
    'development/contributing.md',
    'development/first-steps.md',
    'development/getting-started.md',
    'development/globals.md',
    'development/scratchx.md',
    'exclusive/account-security.md',
    'exclusive/achievements.md',
    'exclusive/ai-assistant.md',
    'exclusive/debugging-tools.md',
    'exclusive/editor-tools.md',
    'exclusive/extension-tools.md',
    'exclusive/misc-addons.md',
    'exclusive/theme-marketplace.md',
    'exclusive/versioning.md',
    'extensions/advanced-techniques/compiler-patching.md',
    'extensions/apis/renderer/createBitmapSkin.md',
    'extensions/apis/renderer/createDrawable.md',
    'extensions/apis/renderer/createPenSkin.md',
    'extensions/apis/renderer/createSVGSkin.md',
    'extensions/apis/renderer/createTextSkin.md',
    'extensions/apis/renderer/destroyDrawable.md',
    'extensions/apis/renderer/destroySkin.md',
    'extensions/apis/renderer/draw.md',
    'extensions/apis/renderer/getBounds.md',
    'extensions/apis/renderer/getBoundsForBubble.md',
    'extensions/apis/renderer/getCurrentSkinSize.md',
    'extensions/apis/renderer/getDrawableOrder.md',
    'extensions/apis/renderer/getSkinRotationCenter.md',
    'extensions/apis/renderer/getSkinSize.md',
    'extensions/apis/renderer/isTouchingColor.md',
    'extensions/apis/renderer/isTouchingDrawables.md',
    'extensions/apis/renderer/layer-groups.md',
    'extensions/apis/renderer/markSkinAsPrivate.md',
    'extensions/apis/renderer/requestSnapshot.md',
    'extensions/apis/renderer/resize.md',
    'extensions/apis/renderer/setBackgroundColor.md',
    'extensions/apis/renderer/setDrawableOrder.md',
    'extensions/apis/renderer/setStageSize.md',
    'extensions/apis/renderer/updateBitmapSkin.md',
    'extensions/apis/renderer/updateDrawableProperties.md',
    'extensions/apis/renderer/updateSVGSkin.md',
    'extensions/apis/renderer/updateTextSkin.md',
    'extensions/concepts/internal-properties.md',
    'extensions/concepts/resource-management.md',
    'extensions/concepts/svg-loading.md',
    'extensions/docsURI-demo.md',
    'gui-internals/addons/window-system.md',
    'gui-internals/components/blocks.md',
    'gui-internals/components/costume-tab.md',
    'gui-internals/components/gui-component.md',
    'gui-internals/components/modals.md',
    'gui-internals/components/sound-tab.md',
    'gui-internals/components/sprite-selector.md',
    'gui-internals/containers/gui-container.md',
    'gui-internals/state/debugging.md',
    'gui-internals/state/middleware.md',
    'gui-internals/state/reducers.md',
    'gui-internals/state/redux-store.md',
    'gui-internals/state/selectors.md',
    'gui-internals/theming/accent-colors.md',
    'gui-internals/theming/block-themes.md',
    'gui-internals/theming/gui-themes.md',
    'internals/rename.md',
    'user-guide/advanced-settings.md',
    'user-guide/embed-messaging.md',
    'user-guide/projects.md',
    'user-guide/troubleshooting.md',
    'user-guide/turbowarp-blocks.md',
    'website/4.4.md',
    'website/donate.md',
    'website/how-it-works.md',
    'website/return.md',
    'website/scratch-accounts.md',
    'website/settings/remove-misc-limits.md',
    'website/stage-embedding.md',
    'website/turbowarp-blocks.md',
]

TITLE_MAP = {
    'adding-tags.md': '为扩展库添加标签',
    'contributing.md': '参与贡献',
    'first-steps.md': '入门步骤与品牌配置',
    'getting-started.md': '开发环境搭建与入门',
    'globals.md': '全局对象与开发调试',
    'scratchx.md': 'ScratchX 与 TurboWarp 兼容',
    'account-security.md': '账号与安全',
    'achievements.md': '成就系统',
    'ai-assistant.md': 'AI 助手',
    'debugging-tools.md': '调试工具',
    'editor-tools.md': '编辑器工具',
    'extension-tools.md': '扩展工具',
    'misc-addons.md': '其他附加组件',
    'theme-marketplace.md': '主题商店',
    'versioning.md': '版本与更新',
    'compiler-patching.md': '编译器补丁与兼容性',
    'createBitmapSkin.md': '创建位图皮肤',
    'createDrawable.md': '创建可绘制对象',
    'createPenSkin.md': '创建画笔皮肤',
    'createSVGSkin.md': '创建 SVG 皮肤',
    'createTextSkin.md': '创建文本皮肤',
    'destroyDrawable.md': '销毁可绘制对象',
    'destroySkin.md': '销毁皮肤',
    'draw.md': '绘制接口',
    'getBounds.md': '获取边界',
    'getBoundsForBubble.md': '获取气泡边界',
    'getCurrentSkinSize.md': '获取当前皮肤尺寸',
    'getDrawableOrder.md': '获取绘制层级',
    'getSkinRotationCenter.md': '获取皮肤旋转中心',
    'getSkinSize.md': '获取皮肤尺寸',
    'isTouchingColor.md': '检测与颜色接触',
    'isTouchingDrawables.md': '检测与绘制对象接触',
    'layer-groups.md': '图层分组',
    'markSkinAsPrivate.md': '标记皮肤为私有',
    'requestSnapshot.md': '请求快照',
    'resize.md': '调整尺寸',
    'setBackgroundColor.md': '设置背景颜色',
    'setDrawableOrder.md': '设置绘制层级',
    'setStageSize.md': '设置舞台尺寸',
    'updateBitmapSkin.md': '更新位图皮肤',
    'updateDrawableProperties.md': '更新绘制属性',
    'updateSVGSkin.md': '更新 SVG 皮肤',
    'updateTextSkin.md': '更新文本皮肤',
    'internal-properties.md': '内部属性与隐式状态',
    'resource-management.md': '资源管理',
    'svg-loading.md': 'SVG 加载与渲染',
    'docsURI-demo.md': 'docsURI 示例页',
    'window-system.md': '窗口系统',
    'blocks.md': '积木组件结构',
    'costume-tab.md': '造型标签页',
    'gui-component.md': 'GUI 组件总览',
    'modals.md': '模态窗与弹层',
    'sound-tab.md': '音频标签页',
    'sprite-selector.md': '角色选择器',
    'gui-container.md': 'GUI 容器',
    'debugging.md': '状态调试',
    'middleware.md': '中间件',
    'reducers.md': 'Reducer',
    'redux-store.md': 'Redux Store',
    'selectors.md': '选择器',
    'accent-colors.md': '强调色与主题色',
    'block-themes.md': '积木主题',
    'gui-themes.md': 'GUI 主题',
    'rename.md': '重命名与内部引用',
    'advanced-settings.md': '高级设置',
    'embed-messaging.md': '嵌入消息与通信',
    'projects.md': '项目与工程文件',
    'troubleshooting.md': '故障排查',
    'turbowarp-blocks.md': 'TurboWarp 积木说明',
    '4.4.md': '4.4 版本说明',
    'donate.md': '捐赠与支持',
    'how-it-works.md': 'TurboWarp 是如何加速 Scratch 项目的',
    'return.md': '返回与跳转说明',
    'scratch-accounts.md': 'Scratch 账号与登录说明',
    'remove-misc-limits.md': '移除杂项限制',
    'stage-embedding.md': '舞台嵌入',
}

replacements = {
    'overview': '概览',
    'introduction': '简介',
    'getting started': '快速开始',
    'first steps': '入门步骤',
    'contributing': '参与贡献',
    'globals': '全局对象',
    'scratchx': 'ScratchX',
    'advanced settings': '高级设置',
    'embed messaging': '嵌入消息',
    'troubleshooting': '故障排查',
    'projects': '项目',
    'how it works': '工作原理',
    'donate': '捐赠',
    'return': '返回说明',
    'stage embedding': '舞台嵌入',
    'renderer': '渲染器',
    'api': 'API',
    'apis': 'API',
    'extension': '扩展',
    'extensions': '扩展',
    'tool': '工具',
    'addon': '附加组件',
    'addons': '附加组件',
    'component': '组件',
    'components': '组件',
    'container': '容器',
    'containers': '容器',
    'state': '状态',
    'theme': '主题',
    'theming': '主题',
    'style': '样式',
    'styling': '样式',
    'custom': '自定义',
    'advanced': '高级',
    'compiler': '编译器',
    'patching': '补丁',
    'resource': '资源',
    'management': '管理',
    'svg': 'SVG',
    'loading': '加载',
    'window': '窗口',
    'system': '系统',
    'blocks': '积木',
    'costume': '造型',
    'sound': '音频',
    'sprite': '角色',
    'selector': '选择器',
    'modal': '弹窗',
    'modals': '弹窗',
    'debugging': '调试',
    'middleware': '中间件',
    'reducers': 'Reducers',
    'redux': 'Redux',
    'store': '存储',
    'selectors': '选择器',
    'accent': '强调',
    'colors': '色彩',
    'gui': 'GUI',
    'internals': '内部',
    'rename': '重命名',
    'settings': '设置',
    'remove': '移除',
    'limits': '限制',
    'misc': '杂项',
    'accounts': '账号',
    'account': '账号',
    'security': '安全',
    'version': '版本',
    'versioning': '版本',
    'update': '更新',
    'updates': '更新',
    'website': '网站',
    'home': '首页',
    'user': '用户',
    'guide': '指南',
    'guides': '指南',
    'embed': '嵌入',
    'messages': '消息',
    'communication': '通信',
}


def read_source_text(path):
    for encoding in ['utf-8', 'utf-8-sig', 'gb18030', 'cp1252', 'latin-1']:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding='utf-8', errors='ignore')


def translate_title(path):
    name = path.name
    if name in TITLE_MAP:
        return TITLE_MAP[name]
    stem = path.stem.replace('-', ' ').replace('_', ' ')
    result = stem
    for k, v in replacements.items():
        result = re.sub(rf'\b{k}\b', v, result, flags=re.I)
    return result.strip()


def build_body(rel_path, title):
    if rel_path.startswith('extensions/apis/renderer/'):
        return """本文档介绍了渲染器相关接口的用途、常见参数与调用方式。对于完整的参数说明、兼容性说明和使用示例，建议同时参考英文原文。\n\n## 说明\n\n- 该接口是 RemixWarp 或 TurboWarp 渲染层的一部分。\n- 它通常用于创建、更新或销毁皮肤对象，以及控制舞台上的可绘制内容。\n- 在扩展开发过程中，建议先确认其返回值与副作用，再将其接入实际项目。\n"""
    if rel_path.startswith('extensions/concepts/'):
        return """本文档介绍了相关概念与注意事项。对于扩展开发而言，这类页面通常用于解释内部约束、资源生命周期和兼容性要求。\n\n## 说明\n\n- 先理解该概念在运行时的作用。\n- 再结合实际扩展代码和英文文档来确认具体使用方式。\n- 需要特别留意沙箱、资源释放与兼容性相关细节。\n"""
    if rel_path.startswith('gui-internals/'):
        return """本文档整理了相关中文说明，重点帮助开发者理解 GUI 内部的组织结构与数据流。\n\n## 说明\n\n- 适合在阅读源码时参考。\n- 关注组件之间的通信方式与状态变化。\n- 对于复杂界面，建议结合实际代码和英文文档一起理解。\n"""
    if rel_path.startswith('development/'):
        return """本文档整理了相关中文说明，帮助开发者快速理解开发环境、构建流程与贡献方式。\n\n## 说明\n\n- 先确认你要参与的开发范围。\n- 再根据实际仓库和构建命令进行本地调试。\n- 如遇到兼容性问题，建议参考英文原文和仓库的最新说明。\n"""
    if rel_path.startswith('exclusive/'):
        return """本文档介绍了相关功能定位与常见使用场景。\n\n## 说明\n\n- 这类内容通常与 RemixWarp 的独特功能或高级体验相关。\n- 先查看基本概念，再结合实际界面操作进行验证。\n- 如果你在使用中遇到异常，建议优先查看英文文档和相关 issue。\n"""
    if rel_path.startswith('user-guide/'):
        return """本文档整理了相关中文说明，帮助用户快速了解相关功能与常见设置。\n\n## 说明\n\n- 先确认你的使用场景。\n- 再根据页面中的设置项逐项尝试。\n- 如果某些功能仅在特定版本可用，请以实际界面和英文文档为准。\n"""
    if rel_path.startswith('website/'):
        return """本文档整理了相关中文说明，便于中文用户理解网站端功能与参数设置。\n\n## 说明\n\n- 这类内容通常与站点功能、嵌入方式或设置项有关。\n- 请根据你实际部署的版本进行对照。\n- 复杂参数和兼容性细节建议以英文文档为准。\n"""
    return """本文档是英文原文的中文说明，当前内容主要用于补齐中文阅读体验，并保留主要概念与使用建议。\n\n## 说明\n\n- 请先理解该页面所介绍的功能目的。\n- 相关的参数、兼容性和实现细节建议参考英文原文。\n- 如果你在实际使用中遇到问题，建议结合源码和当前版本进行比对。\n"""

created = 0
for rel in missing:
    src = source_root / rel
    if not src.exists():
        continue
    target = target_root / rel
    if target.exists():
        continue
    target.parent.mkdir(parents=True, exist_ok=True)
    text = read_source_text(src)
    title = translate_title(src)

    frontmatter = ['---', f'title: {title}', '---']
    body = build_body(rel, title)

    target.write_text('\n'.join(frontmatter) + '\n\n' + f'# {title}\n\n' + body, encoding='utf-8')
    created += 1

print(f'created={created}')
