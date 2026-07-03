"""
A Rich Theme + Pygments Style matching glow's Dracula theme exactly.

Colors sourced from glamour's dracula.json:
  https://github.com/charmbracelet/glamour/blob/main/styles/dracula.json

Dracula palette:
  Background    #282a36    Current Line
  Foreground    #f8f8f2    Foreground
  Comment       #6272a4    Comment
  Cyan          #8be9fd
  Green         #50fa7b
  Orange        #ffb86c
  Pink          #ff79c6
  Purple        #bd93f9
  Red           #ff5555
  Yellow        #f1fa8c
  Green-Cyan    #6eefc0    (literal numbers)
"""

from rich.theme import Theme
from rich.style import Style

# ── Dracula color constants ──────────────────────────────────────────

DRACULA_FG          = "#f8f8f2"   # foreground / document text
DRACULA_BG          = "#282a36"   # background
DRACULA_COMMENT     = "#6272a4"   # comments, dim text
DRACULA_CYAN        = "#8be9fd"   # links, enumerations, names
DRACULA_GREEN       = "#50fa7b"   # code, functions, decorators
DRACULA_ORANGE      = "#ffb86c"   # strong/bold, code blocks
DRACULA_PINK        = "#ff79c6"   # link text, keywords, tags
DRACULA_PURPLE      = "#bd93f9"   # headings, constants
DRACULA_RED         = "#ff5555"   # errors, deletions
DRACULA_YELLOW      = "#f1fa8c"   # emphasis/italic, block quotes, strings
DRACULA_GREEN_CYAN  = "#6eefc0"   # literal numbers

# ── Rich Theme for Markdown text styling ────────────────────────────
#
# Maps glow/glamour Dracula JSON keys → Rich markdown.* style names:
#
#   document.color          → markdown.paragraph, markdown.text
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
#   link_text.color           → markdown.link
#   strikethrough            → markdown.s
#   table                    → markdown.table.border, markdown.table.header

dracula_theme = Theme({
    # ── Document / paragraphs ──
    "markdown.paragraph":       Style(color=DRACULA_FG),
    "markdown.text":            Style(color=DRACULA_FG),

    # ── Headings (all share purple + bold) ──
    "markdown.h1":              Style(color=DRACULA_PURPLE, bold=True),
    "markdown.h2":              Style(color=DRACULA_PURPLE, bold=True),
    "markdown.h3":              Style(color=DRACULA_PURPLE, bold=True),
    "markdown.h4":              Style(color=DRACULA_PURPLE, bold=True),
    "markdown.h5":              Style(color=DRACULA_PURPLE, bold=True),
    "markdown.h6":              Style(color=DRACULA_PURPLE, bold=True),
    "markdown.h1.border":       Style(color=DRACULA_PURPLE),

    # ── Inline styles ──
    "markdown.em":              Style(color=DRACULA_YELLOW, italic=True),   # *italic*
    "markdown.strong":          Style(color=DRACULA_ORANGE, bold=True),      # **bold**
    "markdown.code":            Style(color=DRACULA_GREEN),                  # `inline code`
    "markdown.code_block":      Style(color=DRACULA_ORANGE),                  # code blocks
    "markdown.s":               Style(strike=True),                          # ~~strikethrough~~

    # ── Block quote ──
    "markdown.block_quote":     Style(color=DRACULA_YELLOW, italic=True),

    # ── Lists ──
    "markdown.item":            Style(color=DRACULA_FG),
    "markdown.item.bullet":     Style(color=DRACULA_FG, bold=True),
    "markdown.item.number":     Style(color=DRACULA_CYAN),

    # ── Links ──
    "markdown.link":            Style(color=DRACULA_PINK),                   # link text
    "markdown.link_url":        Style(color=DRACULA_CYAN, underline=True),   # link URL

    # ── Horizontal rule ──
    "markdown.hr":              Style(color=DRACULA_COMMENT),

    # ── Tables ──
    "markdown.table.border":    Style(color=DRACULA_COMMENT),
    "markdown.table.header":    Style(color=DRACULA_CYAN, bold=True),
})


# ── Custom Pygments Style for code blocks ────────────────────────────
#
# Glow's dracula.json includes a full chroma (Pygments) theme.
# Pygments doesn't ship a built-in "dracula" style, so we create one
# that matches the glamour chroma config exactly.

from pygments.style import Style as PygmentsStyle
from pygments.token import (
    Keyword, Name, Comment, String, Error, Punctuation,
    Number, Operator, Generic, Token, Whitespace, Literal,
)


class DraculaStyle(PygmentsStyle):
    """Pygments style matching glamour's dracula.json chroma config."""

    default_style = ""

    styles = {
        # ── Base text ──
        Token:              f"bold {DRACULA_FG}",
        Whitespace:         DRACULA_FG,
        Comment:            f"italic {DRACULA_COMMENT}",
        Comment.Preproc:    DRACULA_PINK,

        # ── Keywords ──
        Keyword:            DRACULA_PINK,
        Keyword.Constant:   DRACULA_PINK,
        Keyword.Declaration: DRACULA_PINK,
        Keyword.Namespace:  DRACULA_PINK,
        Keyword.Type:       DRACULA_CYAN,
        Keyword.Reserved:   DRACULA_PINK,

        # ── Operators / Punctuation ──
        Operator:           DRACULA_PINK,
        Operator.Word:      DRACULA_PINK,
        Punctuation:        DRACULA_FG,

        # ── Names ──
        Name:               DRACULA_CYAN,
        Name.Builtin:       DRACULA_CYAN,
        Name.Function:      DRACULA_GREEN,
        Name.Class:         DRACULA_CYAN,
        Name.Constant:      DRACULA_PURPLE,
        Name.Decorator:     DRACULA_GREEN,
        Name.Attribute:     DRACULA_GREEN,
        Name.Tag:           DRACULA_PINK,
        Name.Other:         DRACULA_FG,

        # ── Literals ──
        Literal:            "",
        Literal.Number:     DRACULA_GREEN_CYAN,
        Literal.String:     DRACULA_YELLOW,
        Literal.String.Escape: DRACULA_PINK,
        Literal.Number.Integer: DRACULA_GREEN_CYAN,
        Literal.Number.Float: DRACULA_GREEN_CYAN,

        # ── Generic ──
        Generic.Deleted:    DRACULA_RED,
        Generic.Inserted:   DRACULA_GREEN,
        Generic.Heading:    f"bold {DRACULA_PURPLE}",
        Generic.Subheading: DRACULA_PURPLE,
        Generic.Error:      DRACULA_RED,
        Generic.Emph:       f"italic {DRACULA_YELLOW}",
        Generic.Strong:     f"bold {DRACULA_ORANGE}",

        # ── Error ──
        Error:              f"bold {DRACULA_RED}",
    }

    background_color = DRACULA_BG


# ── Register the custom Pygments style so Rich can find it by name ──

from pygments.styles import STYLE_MAP

STYLE_MAP["dracula"] = DraculaStyle


# ── Usage ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console
    from rich.markdown import Markdown

    sample = """\
# Dracula Theme Demo

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

hello("Dracula")
```

---

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
"""

    console = Console(theme=dracula_theme)
    md = Markdown(sample, code_theme="dracula")
    console.print(md)