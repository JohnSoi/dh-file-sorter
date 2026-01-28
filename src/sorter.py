"""Модуль логики сортировки файлов."""
from pathlib import Path

from typer import Typer, Argument, Option

from .console import show_welcome, print_error

# Экземпляр консольной утилиты
console_app: Typer = Typer(help="Консольная утилита для сортировки файлов по типам в папки")

@console_app.command()
def sorter(
    source: Path = Argument(..., help="Путь к папке с исходными файлами"),
    log_level: str = Option("INFO", "--log-level", help="Уровень логирования")
) -> None:
    """Функция сортировки файлов по типам в папке.

    Args:
        source (Path): Путь к папке с исходными файлами.
        log_level (str): Уровень логирования.
    """
    show_welcome()

    if not source.exists():
        print_error(f"Папка {source} не существует")
