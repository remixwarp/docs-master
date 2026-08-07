const fs = require('fs');
const path = require('path');

const DOCS_DIR = 'E:/RemixWarp/docs-master/docs';
const I18N_DIR = 'E:/RemixWarp/docs-master/i18n/zh/docusaurus-plugin-content-docs/current';
const BILUP_I18N = 'E:/RemixWarp/bilup-docs-temp/i18n/zh-CN/docusaurus-plugin-content-docs/current';

// 品牌词替换表
const BRAND_REPLACEMENTS = [
  [/Bilup 文档/g, 'RemixWarp 文档'],
  [/Bilup 编辑器/g, 'RemixWarp 编辑器'],
  [/Bilup 打包器/g, 'RemixWarp 打包器'],
  [/Bilup 社区/g, 'RemixWarp 社区'],
  [/Bilup 网站/g, 'RemixWarp 网站'],
  [/Bilup/g, 'RemixWarp'],
  [/editor\.bilup\.org/g, 'remixwarp.pages.dev'],
  [/packager\.bilup\.org/g, 'packager.warp.mistium.com'],
  [/github\.com\/Bilup/g, 'github.com/RemixWarp'],
  [/bilup\.org/g, 'remixwarp.pages.dev'],
];

// Bilup 路径前缀 -> 我们路径前缀 的映射
const PATH_MAPPING = [
  [/\/building-extensions\//g, '/extensions/'],
  [/\/building-extensions\/apis\//g, '/extensions/apis/'],
  [/\/advanced\//g, '/website/'],
  [/\/blocks\//g, '/user-guide/'],
  [/\/editor\//g, '/user-guide/'],
  [/\/contributing\//g, '/development/'],
  [/\/internals\//g, '/gui-internals/'],
];

function collectFiles(dir, map) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) collectFiles(full, map);
    else if (e.name.endsWith('.md')) map.set(e.name, full);
  }
  return map;
}

const bilupMap = collectFiles(BILUP_I18N, new Map());

function applyBrand(s) {
  for (const [re, rep] of BRAND_REPLACEMENTS) s = s.replace(re, rep);
  return s;
}

// 替换内部链接路径（只处理 markdown 链接和 <iframe src> 中的站点内路径）
function mapInternalLinks(s) {
  for (const [re, rep] of PATH_MAPPING) s = s.replace(re, rep);
  return s;
}

let matched = 0;
let notFound = 0;
const notFoundList = [];

function walk(docsDir, i18nDir) {
  const entries = fs.readdirSync(docsDir, { withFileTypes: true });
  for (const e of entries) {
    const fullDocs = path.join(docsDir, e.name);
    const fullI18n = path.join(i18nDir, e.name);
    if (e.isDirectory()) {
      if (!fs.existsSync(fullI18n)) fs.mkdirSync(fullI18n, { recursive: true });
      walk(fullDocs, fullI18n);
    } else if (e.name.endsWith('.md') || e.name.endsWith('.mdx')) {
      const bilupSrc = bilupMap.get(e.name);
      if (bilupSrc) {
        let content = fs.readFileSync(bilupSrc, 'utf8');
        content = applyBrand(content);
        content = mapInternalLinks(content);
        fs.writeFileSync(fullI18n, content, 'utf8');
        matched++;
      } else {
        notFound++;
        notFoundList.push(path.relative(DOCS_DIR, fullDocs));
      }
    }
  }
}

walk(DOCS_DIR, I18N_DIR);

console.log('Matched files: ' + matched);
console.log('Not found in Bilup: ' + notFound);
console.log('--- Not found files ---');
notFoundList.forEach((f) => console.log(f));
