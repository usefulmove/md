# markdown

A simple terminal markdown viewer. It renders markdown files in your console pager with syntax-highlighted code blocks, styled headings, lists, tables, links, and more.

## Features

- **Pager output** — rendered markdown opens in your system pager (e.g. `less`) with full color support
- **Syntax highlighting** — code blocks are highlighted with a custom Pygments style
- **Zero config** — just pass a markdown file and go

## Installation

```
pipx git+https://github.com/usefulmove/md.git
```

This installs the `md` command globally and isolated from other Python packages.

## Usage

```
md <file>
```

For example:

```
md README.md
```

If no file argument is provided, or the file doesn't exist, an error is shown:

```
md
# error: no file argument

md missing.md
# error: missing.md not found
```

## License

[MIT](LICENSE)
