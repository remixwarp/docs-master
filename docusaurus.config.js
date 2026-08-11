/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'RemixWarp Documentation',
  tagline: 'A comprehensive guide to RemixWarp - the advanced Scratch modification platform',
  url: 'https://rw-do-cs.pages.dev',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  favicon: 'favicon.ico',
  organizationName: 'RemixWarp',
  projectName: 'docs',
  trailingSlash: false,
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },
  clientModules: [
    require.resolve('./src/clientModules/spotlight-key.js'),
    require.resolve('./src/clientModules/sidebar-toggle.js'),
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'zh-CN', 'zh-TW'],
    localeConfigs: {
      en: {
        label: 'English',
      },
      'zh-CN': {
        label: '简体中文',
      },
      'zh-TW': {
        label: '繁體中文',
      },
    },
  },
  themeConfig: {
    navbar: {
      title: 'RemixWarp Documentation',
      logo: {
        alt: 'RemixWarp Logo',
        src: 'favicon.ico',
      },
      items: [
        {
          type: 'dropdown',
          label: 'Use RemixWarp',
          position: 'left',
          items: [
            {to: '/getting-started/introduction', label: 'Getting Started'},
            {to: '/editor/interface', label: 'Using the Editor'},
            {to: '/blocks/overview', label: 'Blocks Reference'},
            {to: '/extensions/overview', label: 'Extensions'},
            {to: '/advanced/cloud-variables', label: 'Advanced Features'}
          ]
        },
        {
          type: 'dropdown',
          label: 'Build & Extend',
          position: 'left',
          items: [
            {to: '/building-extensions/introduction', label: 'Building Extensions'},
            {to: '/packager/overview', label: 'Packager'},
            {to: '/api-reference/overview', label: 'API Reference'}
          ]
        },
        {
          type: 'dropdown',
          label: 'Contribute',
          position: 'left',
          items: [
            {to: '/contributing/overview', label: 'Contributing'},
            {to: '/development/home', label: 'Development'},
            {to: '/internals/overview', label: 'Architecture & Internals'},
            {to: '/gui-internals/home', label: 'GUI Internals'}
          ]
        },
        {
          type: 'dropdown',
          label: 'More',
          position: 'left',
          items: [
            {to: '/exclusive/overview', label: 'RemixWarp Exclusive'},
            {to: '/user-guide/overview', label: 'User Guide'},
            {to: '/website/how-it-works', label: 'Website Features'}
          ]
        },
        {
          href: 'https://remixwarp.pages.dev/',
          label: 'RemixWarp',
          position: 'right'
        },
        {
          href: 'https://github.com/RemixWarp',
          label: 'GitHub',
          position: 'right',
        },
        {
          type: 'localeDropdown',
          position: 'right',
        },
      ],
    },
    algolia: {
      container: '#docsearch',
      appId: '90B9X0B5K5',
      indexName: 'RemixWarp Documentation Crawler',
      apiKey: '2e6593daef4974ad3d144ebd2fdf488f'
    },
    colorMode: {
      // The editor syncs the docs to its own theme, so no in-page toggle.
      disableSwitch: true,
      respectPrefersColorScheme: true,
    },
    prism: {
      theme: require('./code-themes/light'),
      darkTheme: require('./code-themes/dark'),
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/',
          editUrl: 'https://github.com/RemixWarp/docs/edit/main/',
          breadcrumbs: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
