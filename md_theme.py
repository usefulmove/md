"""
a Rich Theme + Pygments Style
"""

from rich.theme import Theme
from rich.style import Style

# ── md color constants ──────────────────────────────────────────

MD_FG          = "#f8f8f2"   # foreground / document text
MD_BG          = "#121420"   # background
MD_COMMENT     = "#6272a4"   # comments, dim text
MD_BLUE        = "#00a0ff"   # links, enumerations, names
MD_GREEN       = "#50fa7b"   # code, functions, decorators
MD_ORANGE      = "#ef9d6e"   # strong/bold, code blocks
MD_PINK        = "#ff79c6"   # link text, keywords, tags
MD_PURPLE      = "#bd93f9"   # headings, constants
MD_RED         = "#ff5555"   # errors, deletions
MD_YELLOW      = "#faf699"   # emphasis/italic, block quotes, strings
MD_GREEN_CYAN  = "#6eefc0"   # literal numbers

# ── Rich Theme for Markdown text styling ────────────────────────────
#
# maps glow/glamour md JSON keys → Rich markdown.* style names:
#
#   document.color           → markdown.paragraph, markdown.text
#   heading.color/bold       → markdown.h1-h6
#   emph.color/italic        → markdown.em
#   strong.color/bold        → markdown.strong
#   code.color               → markdown.code
#   code_block               → markdown.code_block (cosmetic; real highlighting via Pygments)
#   block_quote.color/italic → markdown.block_quote
#   item.color               → markdown.item
#   item.block_prefix "• "   → markdown.item.bullet
#   enumeration.color        → markdown.item.number
#   hr.color                 → markdown.hr
#   link.color/underline     → markdown.link_url
#   link_text.color          → markdown.link
#   strikethrough            → markdown.s
#   table                    → markdown.table.border, markdown.table.header

md_theme = Theme({
    # ── Document / paragraphs ──
    "markdown.paragraph":       Style(color=MD_FG),
    "markdown.text":            Style(color=MD_FG),

    # ── Headings (all share purple + bold) ──
    "markdown.h1":              Style(color=MD_PURPLE, bold=True),
    "markdown.h2":              Style(color=MD_PURPLE, bold=True),
    "markdown.h3":              Style(color=MD_PURPLE, bold=True),
    "markdown.h4":              Style(color=MD_PURPLE, bold=True),
    "markdown.h5":              Style(color=MD_PURPLE, bold=True),
    "markdown.h6":              Style(color=MD_PURPLE, bold=True),
    "markdown.h1.border":       Style(color=MD_PURPLE),

    # ── Inline styles ──
    "markdown.em":              Style(color=MD_YELLOW, italic=True),   # *italic*
    "markdown.strong":          Style(color=MD_ORANGE, bold=True),     # **bold**
    "markdown.code":            Style(color=MD_GREEN),                 # `inline code`
    "markdown.code_block":      Style(color=MD_ORANGE),                # code blocks
    "markdown.s":               Style(strike=True),                    # ~~strikethrough~~

    # ── Block quote ──
    "markdown.block_quote":     Style(color=MD_YELLOW, italic=True),

    # ── Lists ──
    "markdown.item":            Style(color=MD_FG),
    "markdown.item.bullet":     Style(color=MD_FG, bold=True),
    "markdown.item.number":     Style(color=MD_BLUE),

    # ── Links ──
    "markdown.link":            Style(color=MD_PINK),                   # link text
    "markdown.link_url":        Style(color=MD_BLUE, underline=False),   # link URL

    # ── Horizontal rule ──
    "markdown.hr":              Style(color=MD_COMMENT),

    # ── Tables ──
    "markdown.table.border":    Style(color=MD_COMMENT),
    "markdown.table.header":    Style(color=MD_BLUE, bold=True),
})


# ── Custom Pygments Style for code blocks ────────────────────────────

from pygments.style import Style as PygmentsStyle
from pygments.token import (
    Keyword, Name, Comment, String, Error, Punctuation,
    Number, Operator, Generic, Token, Whitespace, Literal,
)


class MDStyle(PygmentsStyle):
    """Pygments style."""

    default_style = ""

    styles = {
        # ── Base text ──
        Token:              f"bold {MD_FG}",
        Whitespace:         MD_FG,
        Comment:            f"italic {MD_COMMENT}",
        Comment.Preproc:    MD_PINK,

        # ── Keywords ──
        Keyword:            MD_PINK,
        Keyword.Constant:   MD_PINK,
        Keyword.Declaration: MD_PINK,
        Keyword.Namespace:  MD_PINK,
        Keyword.Type:       MD_BLUE,
        Keyword.Reserved:   MD_PINK,

        # ── Operators / Punctuation ──
        Operator:           MD_PINK,
        Operator.Word:      MD_PINK,
        Punctuation:        MD_FG,

        # ── Names ──
        Name:               MD_BLUE,
        Name.Builtin:       MD_BLUE,
        Name.Function:      MD_GREEN,
        Name.Class:         MD_BLUE,
        Name.Constant:      MD_PURPLE,
        Name.Decorator:     MD_GREEN,
        Name.Attribute:     MD_GREEN,
        Name.Tag:           MD_PINK,
        Name.Other:         MD_FG,

        # ── Literals ──
        Literal:                "",
        Literal.Number:         MD_GREEN_CYAN,
        Literal.String:         MD_YELLOW,
        Literal.String.Escape:  MD_PINK,
        Literal.Number.Integer: MD_GREEN_CYAN,
        Literal.Number.Float:   MD_GREEN_CYAN,

        # ── Generic ──
        Generic.Deleted:    MD_RED,
        Generic.Inserted:   MD_GREEN,
        Generic.Heading:    f"bold {MD_PURPLE}",
        Generic.Subheading: MD_PURPLE,
        Generic.Error:      MD_RED,
        Generic.Emph:       f"italic {MD_YELLOW}",
        Generic.Strong:     f"bold {MD_ORANGE}",

        # ── Error ──
        Error:              f"bold {MD_RED}",
    }

    background_color = MD_BG


# ── Register the custom Pygments style so Rich can find it by name ──

from pygments.styles import _STYLE_NAME_TO_MODULE_MAP

_STYLE_NAME_TO_MODULE_MAP["md"] = ("md_theme", "MDStyle")


# ── Usage ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console
    from rich.markdown import Markdown

    sample = """
# md theme demo

## Headings
### Heading 3
#### Heading 4

This is a **bold** and *italic* paragraph with `inline code`.

> This is a block quote.
> It spans multiple lines.

- Bullet item one
- Bullet item two
- Bullet item three

1. Numbered item one
2. Numbered item two
3. Numbered item three

Here is a [link](https://example.com) and some ~~strikethrough~~ text.

```python
import os

def hello(name: str) -> None:
    # Say hello to someone
    print(f"Hello, {name}!")

hello("md")
```

---

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
"""

    console = Console(theme=md_theme)
    md = Markdown(sample, code_theme="md")
    console.print(md)
