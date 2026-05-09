# Duyet Fonts

A collection of custom typefaces and editorial-style fonts.

## Fonts Included

### 1. Duyet Serif
A high-contrast editorial serif based on [Instrument Serif](https://github.com/Instrument/instrument-serif). Optimized for data-heavy projects, high-impact headings, and a Zen aesthetic.

## Live Demo
Check out the fonts in action: [https://duyet.github.io/fonts/](https://duyet.github.io/fonts/)

## Installation

```bash
npm install @duyet/fonts
```

## Usage

Import the specific font CSS in your project:

```javascript
import '@duyet/fonts/fonts/duyet-serif/index.css';
```

Then use it in your CSS:

```css
body {
  font-family: 'Duyet Serif', serif;
}
```

## Development

The project uses `fontmake` to build fonts from source.

```bash
# Install dependencies
uv pip install -r requirements.txt

# Build all fonts
make build

# Build a specific font
make duyet-serif
```

## Structure
- `sources/<font-name>/`: Font source files (e.g., `.glyphs`).
- `fonts/<font-name>/`: Compiled `.ttf` and `.woff2` files.

## License
Licensed under the [SIL Open Font License 1.1](OFL.txt).
