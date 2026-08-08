---
title: Stage Embedding
sidebar_position: 3
slug: /website/stage-embedding
---

# Stage Embedding

In addition to the standard iframe [embedding method](/website/embedding), RemixWarp also supports embedding projects through a dedicated **stage-only player** — `fullscreen.html`. This method loads the project directly into a clean, full-stage view without any editor UI, making it ideal for showcasing finished projects.

## How It Works

The stage player loads an external `.sb3` project file via the `project_url` query parameter:

```
https://remixwarp.pages.dev/fullscreen.html?project_url=YOUR_SB3_URL
```

The project file (`.sb3`) must be hosted at a publicly accessible URL and support [CORS](/website/cors) so the player can fetch it.

## Basic Usage

```html
<iframe
  src="https://remixwarp.pages.dev/fullscreen.html?project_url=https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3"
  width="960"
  height="720"
  frameborder="0"
  scrolling="no"
  allowfullscreen
></iframe>
```

The `project_url` can point to any publicly hosted `.sb3` file, including files uploaded to your own server, a CDN, or cloud storage.

## Comparison: Stage Mode vs. iframe Embed

| Feature | Standard iframe Embed | Stage Mode (`fullscreen.html`) |
|---------|----------------------|-------------------------------|
| Project source | Scratch / RemixWarp project ID | Any hosted `.sb3` file URL |
| Requires shared project | Yes | No |
| Editor UI | None | None |
| Fullscreen background | Controlled by parameter | Controlled by the stage |
| CORS required | No | Yes (for the SB3 URL) |
| Self-hosting projects | Use Packager | Host the `.sb3` directly |
| Best for | Quick sharing of public projects | Custom portfolios, game sites, offline-ready demos |

## URL Parameters

The stage player supports the following query parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `project_url` | **Required.** The URL of the `.sb3` file to load. | `?project_url=https://example.com/project.sb3` |
| `autoplay` | Automatically starts the project when loaded. | `?project_url=...&autoplay` |
| `turbo` | Enables turbo mode for maximum performance. | `?project_url=...&turbo` |
| `fps` | Sets a custom frame rate (e.g. `60`). | `?project_url=...&fps=60` |
| `hqpen` | Enables high-quality pen rendering. | `?project_url=...&hqpen` |
| `interpolate` | Enables motion interpolation for smoother animation. | `?project_url=...&interpolate` |
| `username` | Sets the username used by blocks. | `?project_url=...&username=Player` |

### Full Example with Multiple Parameters

```
https://remixwarp.pages.dev/fullscreen.html?project_url=https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3&autoplay&turbo&fps=60
```

## Hosting Your SB3 Files

To use stage embedding, you need to host your `.sb3` file somewhere accessible. Here are common options:

### Option 1: Cloud Storage with CORS

Upload your `.sb3` to a service that supports CORS headers, such as Cloudflare R2, AWS S3 (with CORS configured), or GitHub Pages.

**Example (Cloudflare R2 with custom domain):**
```
https://rw-vep.pages.dev/BV1Cu5m6kENy.sb3
```

### Option 2: Self-Hosted

Place the `.sb3` on the same server as the embedding page (same-origin), which avoids CORS issues entirely.

```
https://yoursite.com/projects/my-game.sb3
```

### Option 3: Export from the 02Engine Packager

Use the [02Engine Packager](https://packager.02engine.org/) to export a packaged HTML file. You can then extract the `.sb3` or host the packaged HTML directly. See [Packager Embedding](/packager/embedding) for details.

## Security Considerations

- **CORS**: The `.sb3` file host must return appropriate `Access-Control-Allow-Origin` headers for cross-origin requests. Otherwise, the player cannot fetch the file.
- **Content Security Policy**: If embedding the stage player in an iframe, configure your CSP to allow `frame-src https://remixwarp.pages.dev`.
- **Sandbox**: Use the `sandbox` iframe attribute for defense in depth:

```html
<iframe
  src="https://remixwarp.pages.dev/fullscreen.html?project_url=..."
  sandbox="allow-scripts allow-same-origin allow-fullscreen"
  allowfullscreen
></iframe>
```

## Responsive Embedding

Wrap the stage player in a responsive container that maintains the stage aspect ratio:

```html
<div style="position: relative; padding-bottom: 75%; height: 0;">
  <iframe
    src="https://remixwarp.pages.dev/fullscreen.html?project_url=https://example.com/project.sb3"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    frameborder="0"
    allowfullscreen
  ></iframe>
</div>
```

The `75%` padding creates a 4:3 aspect ratio to match the default Scratch stage. Adjust to `56.25%` for 16:9 widescreen if your project uses a custom stage size.

## Troubleshooting

### Project doesn't load
- Verify the `project_url` is a direct link to the `.sb3` file (not a download page).
- Check that the file hosting supports CORS. Test with a CORS-enabled host like a same-origin URL.
- Open the browser console for CORS or network errors.

### White screen / blank stage
- Ensure the `.sb3` file is a valid Scratch 3.0 project file.
- Try downloading the URL directly in the browser to confirm it resolves.
- Check for Content Security Policy errors in the browser console.

## See Also

- [Standard Embedding](/website/embedding) — Embed projects by Scratch or RemixWarp project ID
- [02Engine Packager](https://packager.02engine.org/) — Package projects as standalone HTML files
- [Packager Embedding](/packager/embedding) — Embed packaged project files
- [CORS Guide](/website/cors) — Understanding CORS for project hosting
- [URL Parameters](/website/url-parameters) — All available URL parameters
