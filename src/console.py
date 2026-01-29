from rich import get_console
from rich.panel import Panel


class ConsoleManager:
    def __init__(self, silent: bool) -> None:
        self._console = get_console()
        self._silent: bool = silent

    @property
    def console(self):
        return self._console

    def show_welcome(self, path: str | None = None) -> None:
        self._print(Panel.fit(
            "[bold green]📁  DH|FileSorter[/bold green] \n\n"
            "Утилита для сортировки файлов по типам в папке." + ("\n\nПуть: [bold cyan]" + path + "[/bold cyan]" if path else ""),
            border_style="green"
        ))

    def print_log(self, message: str) -> None:
        self._print(f"[yellow]→ {message}[/yellow]")

    def print_error(self, message: str) -> None:
        self._print(f"[red]✗ {message}[/red]")

    def print_success(self, message: str) -> None:
        self._print(f"[green]✓ {message}[/green]")

    def _print(self, message: str | Panel) -> None:
        if self._silent:
            return

        self._console.print(message)
