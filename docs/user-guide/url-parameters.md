---
title: URL Parameters
sidebar_position: 10
---

# URL Parameters

RemixWarp supports URL parameters that let you load projects and adjust runtime and compiler behavior. These are useful for embedding, automation, and sharing reproducible setups.

## Basic Usage

### URL Parameter Syntax
Add parameters using standard query string format:
```
https://editor.RemixWarp.org/${projectId}`
```

### Multiple Parameters
Combine multiple parameters with `&`:
```
https://editor.RemixWarp.org/${projectId}`
```

## Project Loading

### Load by ID
Load a Scratch project by its ID:
```
https://editor.RemixWarp.org/${projectId}`
```

### Load from URL
Load a project from a direct URL:
```
https://editor.RemixWarp.org/${projectId}`
```

### Auto-start (embed only)
Automatically start the project in embeds:
```
https://editor.RemixWarp.org/${projectId}`?autoplay
```

### Username
Set the username used by cloud variables and blocks:
```
https://editor.RemixWarp.org/${projectId}`?username=alice
```

## Performance

### Turbo Mode
Enable high-speed execution:
```
https://editor.RemixWarp.org/${projectId}`
```

### Frame Rate
Set custom frame rate:
```
https://editor.RemixWarp.org/${projectId}`     # 60 FPS
https://editor.RemixWarp.org/${projectId}`    # 120 FPS
https://editor.RemixWarp.org/${projectId}`     # 30 FPS (default)
```

### High Quality Pen
Enable anti-aliased pen rendering:
```
https://editor.RemixWarp.org/${projectId}`
```

### Interpolation
Enable frame interpolation for smoother motion:
```
https://editor.RemixWarp.org/${projectId}`
```

### Remove Misc Limits
Disable certain runtime limits:
```
https://editor.RemixWarp.org/${projectId}`
```

## Display

### Custom Stage Size
Set custom stage dimensions:
```
https://editor.RemixWarp.org/${projectId}`
https://editor.RemixWarp.org/${projectId}`
```

### Fullscreen Background (player-only)
Control fullscreen background color:
```
https://editor.RemixWarp.org/${projectId}`
```

### Offscreen Fencing
Disable offscreen fencing:
```
https://editor.RemixWarp.org/${projectId}`
```

### Clone Limit
Set maximum clones:
```
https://editor.RemixWarp.org/${projectId}`
```

## Extensions

### Load Extensions
Load custom extensions by URL (unsandboxed recommended):
```
https://editor.RemixWarp.org/${projectId}`
https://editor.RemixWarp.org/${projectId}`
```

### Addons (embed only)
Enable specific addons in embeds:
```
https://editor.RemixWarp.org/${projectId}`/embed?addons=pause,gamepad
```

## Embedding

### Autoplay and Addons
Embed-specific options:
```
https://editor.RemixWarp.org/${projectId}`/embed?autoplay
https://editor.RemixWarp.org/${projectId}`/embed?addons=pause,gamepad
```

## Development

### Disable Compiler
Turn off the compiler (for debugging):
```
https://editor.RemixWarp.org/${projectId}`
```

### Project URL
Load project data from a direct URL:
```
https://editor.RemixWarp.org/${projectId}`
```

### Cloud Host (embed/player)
Override cloud server:
```
https://editor.RemixWarp.org/${projectId}`
```

## Reference

## Complete Parameter Reference

### Performance
| Parameter | Values | Description |
|-----------|--------|-------------|
| `turbo` | boolean | Enable turbo mode |
| `fps` | number | Set frame rate |
| `hqpen` | boolean | High quality pen |
| `interpolate` | boolean | Enable interpolation |
| `limitless` | boolean | Disable misc limits |
| `stuck` | boolean | Enable warp timer (player-only) |

### Display
| Parameter | Values | Description |
|-----------|--------|-------------|
| `size` | WIDTHxHEIGHT | Custom stage size |
| `fullscreen-background` | CSS color | Fullscreen background color |
| `offscreen` | boolean | Disable offscreen fencing |

### Project
| Parameter | Values | Description |
|-----------|--------|-------------|
| `username` | string | Username |
| `project_url` | URL | Load from URL |

### Extensions
| Parameter | Values | Description |
|-----------|--------|-------------|
| `extension` | URL | Load extension by URL |

### Development
| Parameter | Values | Description |
|-----------|--------|-------------|
| `nocompile` | boolean | Disable compiler |
| `cloud_host` | wss://... | Custom cloud host |

## URL Parameter Examples

### Gaming Setup
Optimized for games:
```
https://editor.RemixWarp.org/${projectId}`?turbo&fps=60&interpolate
```

### Educational Embedding
Clean embed for education:
```
https://editor.RemixWarp.org/${projectId}`/embed?autoplay&size=800x600
```

### Development Testing
Development environment:
```
https://editor.RemixWarp.org/${projectId}`&fps=120&hqpen
```

### High Performance
Maximum performance:
```
https://editor.RemixWarp.org/${projectId}`&fps=120&hqpen
```

### Accessible Mode
Use OS/browser accessibility features. Theme is controlled in the UI, not via URL.

## URL Encoding

### Special Characters
Encode special characters in URLs:
```
Space: %20
#: %23
&: %26
=: %3D
```

### Example with Encoding
```
https://editor.RemixWarp.org/${projectId}`&hqpen
```

## JavaScript URL Manipulation

### Reading Parameters
```javascript
const urlParams = new URLSearchParams(window.location.search);
const turboMode = urlParams.has('turbo');
const fps = urlParams.get('fps') || '30';
```

### Setting Parameters
```javascript
const url = new URL(window.location);
url.searchParams.set('fps', '60');
url.searchParams.set('turbo', '');
window.history.pushState({}, '', url);
```

### Building URLs Programmatically
```javascript
function buildRemixWarpURL(projectId, options = {}) {
  const url = new URL(`https://editor.RemixWarp.org/${projectId}`);
  
  Object.entries(options).forEach(([key, value]) => {
    if (value === true) {
      url.searchParams.set(key, '');
    } else if (value !== false && value !== null) {
      url.searchParams.set(key, value);
    }
  });
  
  return url.toString();
}

// Usage
const gameURL = buildRemixWarpURL('123456789', {
  turbo: true,
  fps: 60,
  interpolate: true
});
```

## Best Practices

### URL Length
- Keep URLs reasonable length (under 2000 characters)
- Use essential parameters only
- Consider using short parameter names

### User Experience
- Provide sensible defaults
- Use autoplay sparingly
- Test URLs thoroughly

### Performance
- Combine compatible performance parameters
- Test performance impact of parameter combinations
- Monitor for conflicts between parameters

URL parameters provide powerful customization capabilities for RemixWarp. Use them to create tailored experiences for different users and use cases!
