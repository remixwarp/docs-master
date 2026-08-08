const fs = require('fs');
const path = require('path');

const ROOT = 'E:/RemixWarp/docs-master';

// 替换规则
const REPLACEMENTS = [
  [/editor\.bilup\.org/g, 'remixwarp.pages.dev'],
  [/packager\.bilup\.org/g, 'packager.02engine.org'],
  [/docs\.bilup\.org/g, 'rw-do-cs.pages.dev'],
  [/bilup\.org/g, 'remixwarp.pages.dev'],
  [/github\.com\/Bilup\/docs\/edit\/main\//g, 'github.com/RemixWarp/docs/edit/master/'],
  [/github\.com\/Bilup/g, 'github.com/RemixWarp'],
  [/Bilup Documentation/g, 'RemixWarp Documentation'],
  [/Bilup Logo/g, 'RemixWarp Logo'],
  [/Bilup 编辑器/g, 'RemixWarp 编辑器'],
  [/Bilup 打包器/g, '02Engine Packager'],
  [/RemixWarp 打包器/g, '02Engine Packager'],
  [/RemixWarp打包器/g, '02Engine Packager'],
  [/Bilup 社区/g, 'RemixWarp 社区'],
  [/Bilup/g, 'RemixWarp'],
  [/90B9X0B5K5/g, 'HORQ9E5CCA'],
  [/Bilup Documentation Crawler/g, 'RemixWarp'],
  [/2e6593daef4974ad3d144ebd2fdf488f/g, 'c3873ce4208edb896a31bb3e7c2cbdad'],
];

function walk(dir, callback) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (e.name === 'node_modules' || e.name === '.docusaurus' || e.name === 'build' || e.name === 'bilup-docs-temp') continue;
      walk(full, callback);
    } else {
      callback(full);
    }
  }
}

let changed = 0;
let scanned = 0;
const exts = new Set(['.md', '.mdx', '.json', '.js', '.jsx', '.ts', '.tsx', '.css', '.html', '.txt', '.yml', '.yaml']);

function processFile(file) {
  const ext = path.extname(file).toLowerCase();
  if (!exts.has(ext)) return;
  scanned++;
  let content = fs.readFileSync(file, 'utf8');
  let original = content;
  for (const [re, rep] of REPLACEMENTS) {
    content = content.replace(re, rep);
  }
  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    changed++;
  }
}

const targets = [
  path.join(ROOT, 'docs'),
  path.join(ROOT, 'i18n', 'zh'),
  path.join(ROOT, 'src'),
];

for (const t of targets) {
  if (fs.existsSync(t)) walk(t, processFile);
}

for (const f of ['docusaurus.config.js', 'sidebars.js', 'README.md', 'CONTRIBUTING.md']) {
  const p = path.join(ROOT, f);
  if (fs.existsSync(p)) processFile(p);
}

console.log('Scanned files: ' + scanned);
console.log('Changed files: ' + changed);