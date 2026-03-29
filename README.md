# Sunburst Plot

A simple Python app that generates an interactive **sunburst chart** visualizing a two-level product category hierarchy.

## What It Does

The app builds a sunburst plot showing a breakdown of gadget categories and their subcategories by value:

- **Electronics**
  - Phones (10)
  - Computers (20)
- **Radios**
  - HAM (5)
  - Citizens Band (15)

The chart is rendered interactively in a browser window, allowing you to hover over and click segments to explore the hierarchy.

## Technology

| Technology | Purpose |
|---|---|
| **Python** | Core language |
| **Pandas** | Data structuring via `DataFrame` |
| **Plotly Express** | Interactive sunburst chart generation and rendering |

## Requirements

```
plotly
pandas
```

Install dependencies with:

```bash
pip install plotly pandas
```

## Usage

```bash
python file.py
```

This will open an interactive sunburst chart in your default web browser.
