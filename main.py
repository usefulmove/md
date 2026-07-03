from md_theme import md_theme
from rich.markdown import Markdown
from rich.console import Console
import sys

console = Console(theme=md_theme)

def main():
    # check for file argument
    if len(sys.argv) < 2:
        console.print("[red]error[/]: no file argument")
        sys.exit(1)
    filename = sys.argv[1]

    # read file contents
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        console.print(f"[red]error[/]: [#6272a4]{filename}[/] not found")
        sys.exit(1)

    # display as rendered markdown in console pager
    with console.pager(styles=True):
        console.print(Markdown(contents))

if __name__ == "__main__":
    main()
