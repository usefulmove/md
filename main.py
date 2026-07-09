from md_theme import md_theme
from rich.markdown import Markdown
from rich.console import Console
import sys

console = Console(theme=md_theme)


def main() -> None:
    # check for file argument
    if len(sys.argv) < 2:
        console.print("[#f15f49]error[/]: no file argument")
        console.print("usage: [#6272a4]mp [#0080ff]<file.md>[/][/]")
        sys.exit(1)
    arg = sys.argv[1]

    # handle help flags
    if arg in ["--help", "-h"]:
        console.print("[#0080ff]md[/]. [#6272a4 bold]a simple markdown viewer[/].")
        console.print("usage: [#6272a4]mp [#0080ff]<file.md>[/][/]")
        console.print("usage: [#6272a4]mp --python [#0080ff]<file.py>[/][/]")
        sys.exit(0)

    # handle code flags
    filename = arg
    code_flag = ""
    if arg.startswith("--"):  # if code flag is present
        code_flag = arg[2:]
        if len(sys.argv) < 3:
            console.print("[#f15f49]error[/]: no file argument after code flag")
            console.print("usage: [#6272a4]mp --python [#0080ff]<file.py>[/][/]")
            sys.exit(1)
        filename = sys.argv[2]

    # read file contents
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        console.print(f"[#f15f49]error[/]: file [#6272a4 bold]{filename}[/] not found")
        sys.exit(1)

    # display as rendered markdown in console pager
    def code_block(code: str, lang: str) -> None:
        return f"# {filename}\n```{lang}\n{code}\n\n```"

    with console.pager(styles=True):
        console.print(
            Markdown(
                contents if not code_flag else code_block(contents, code_flag),
                code_theme="md",
            )
        )


if __name__ == "__main__":
    main()
