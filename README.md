# md

A simple terminal Markdown viewer. It renders Markdown files in your console pager with syntax-highlighted code blocks, styled headings, lists, tables, links, and more.

## Features

- **Pager output** — rendered Markdown opens in your system pager (e.g. `less`) with full color support
- **Syntax highlighting** — code blocks are highlighted with a custom Pygments style
- **Zero config** — just pass a Markdown file and go

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
