/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'RemixWarp Documentation',
  tagline: 'A comprehensive guide to RemixWarp - the advanced Scratch modification platform',
  url: 'https://docs.warp.mistium.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'favicon.ico',
  organizationName: 'RemixWarp',
  projectName: 'docs',
  trailingSlash: false,
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'zh'],
    localeConfigs: {
      en: {
        label: 'English',
      },
      zh: {
        label: '中文',
      },
    },
  },
  themeConfig: {
    navbar: {
      title: 'RemixWarp Documentation',
      logo: {
        alt: 'RemixWarp Logo',
        src: '/static/desktop.png',
      },
      items: [
        {
          to: '/getting-started/',
          label: 'Getting Started',
          position: 'left'
        },
        {
          to: '/development/',
          label: 'Development',
          position: 'left'
        },
        {
          to: '/gui-internals/',
          label: 'GUI Internals',
          position: 'left'
        },
        {
          to: '/packager/',
          label: 'Packager',
          position: 'left'
        },
        {
          to: '/api-reference/',
          label: 'API Reference',
          position: 'left'
        },
        {
          type: 'localeDropdown',
          position: 'right',
        },
        {
          href: 'https://editor.RemixWarp.org/',
          label: 'RemixWarp',
          position: 'right'
        },
        {
          href: 'https://github.com/RemixWarp',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    algolia: {
      // This is all supposed to be public
      appId: 'HORQ9E5CCA',
      apiKey: 'c3873ce4208edb896a31bb3e7c2cbdad',
      indexName: 'RemixWarp',
    },
    colorMode: {
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
          editUrl: 'https://github.com/RemixWarp/docs/edit/master/',
          breadcrumbs: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
