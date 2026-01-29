# pylint: disable=too-few-public-methods
"""Модуль логики сортировки файлов."""

import time
from pathlib import Path

from typer import Argument, Option, Typer

from .console import ConsoleManager
from .models import FileModel, PathModel

# Экземпляр консольной утилиты
console_app: Typer = Typer(help="Консольная утилита для сортировки файлов по типам в папки")


class Sorter:
    """
    Класс сортировки файлов по типам в папке.

    Attributes:
        _source (Path): Путь к папке с исходными файлами.
        _silent (bool): Не выводить логи.
        _console_manager (ConsoleManager): Менеджер консоли.
    """

    def __init__(self, source: Path, silent: bool) -> None:
        """
        Конструктор класса.

        Args:
            source (Path): Путь к папке с исходными файлами.
            silent (bool): Не выводить логи.
        """
        self._source: Path = source
        self._silent: bool = silent
        self._console_manager: ConsoleManager = ConsoleManager(silent)

        try:
            self._path_model: PathModel = PathModel(self._source)
        except (FileNotFoundError, NotADirectoryError) as exc:
            self._console_manager.print_error(str(exc))
            raise SystemError() from exc

        self._print_start_message()

    def sort(self) -> None:
        """
        Сортировка файлов по типам в папке.

        Examples:
            >>> sorter_1: Sorter = Sorter(Path("C:/Users/username/Desktop"), False)
            >>> sorter_1.sort() # Сортировка файлов без вывода логов
            >>> sorter_2: Sorter = Sorter(Path("C:/Users/username/Desktop"), True)
            >>> sorter_2.sort() # Сортировка файлов с выводом логов
        """
        with self._console_manager.progress as progress:
            task = progress.add_task("[cyan]Сортировка...", total=self._path_model.files_count, current_file="")

            for i, file in enumerate(self._path_model.files):
                progress.update(task, advance=1, current_file=f"[yellow]{file.name}[/yellow]")

                self._move_file_in_type_folder(file)
                time.sleep(0.1)

                progress.update(task, description=f"[cyan]Сортировка... ({i}/{self._path_model.files_count})")

        self._console_manager.print_success("Все файлы отсортированы")

    def _print_start_message(self) -> None:
        """Вывод сообщения о начале сортировки."""
        self._console_manager.show_welcome(str(self._source))
        self._console_manager.print_log(f"Всего файлов: {self._path_model.files_count}")

    def _move_file_in_type_folder(self, file: Path) -> None:
        """Перемещение файла в папку с типом."""
        model: FileModel = FileModel(file, self._source)
        model.move()


@console_app.command()
def sorter(
    source: Path = Argument(..., help="Путь к папке с исходными файлами"),
    silent: bool = Option(False, "--silent", help="Не выводить логи"),
) -> None:
    """Функция сортировки файлов по типам в папке.

    Args:
        source (Path): Путь к папке с исходными файлами.
        silent (bool): Не выводить логи.
    """
    try:
        Sorter(source, silent).sort()
    except SystemError:
        pass
