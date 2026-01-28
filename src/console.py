from rich import get_console
from rich.panel import Panel

console = get_console()

def show_welcome():
    console.print(Panel.fit(
        "[bold cyan]📁 DH|FileSorter[/bold cyan]\n"
        "Утилита для сортировки файлов по типам",
        border_style="cyan"
    ))


def print_error(message):
    console.print(f"[red]✗ {message}[/red]")