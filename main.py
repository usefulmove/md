from rich.markdown import Markdown
from rich.console import Console
import sys

console = Console()

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
        console.print(f"[red]error[/]: [dim]{filename}[/] not found")
        sys.exit(1)

    # display as rendered markdown in console pager
    with console.pager(styles=True):
        console.print(Markdown(contents))

if __name__ == "__main__":
    main()
