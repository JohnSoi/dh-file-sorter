"""Модуль логики сортировки файлов."""
import time
from pathlib import Path

from rich.progress import Progress, SpinnerColumn, TextColumn
from typer import Typer, Argument, Option

from .console import ConsoleManager
from .models import PathModel, FileModel

# Экземпляр консольной утилиты
console_app: Typer = Typer(help="Консольная утилита для сортировки файлов по типам в папки")


class Sorter:
    def __init__(self, source: Path, silent: bool) -> None:
        self._source: Path = source
        self._silent: bool = silent
        self._console_manager: ConsoleManager = ConsoleManager(silent)

        try:
            self._path_model: PathModel = PathModel(self._source)
        except (FileNotFoundError, NotADirectoryError) as exc:
            self._console_manager.print_error(exc)
            raise SystemError()

        self._print_start_message()

    def _print_start_message(self) -> None:
        self._console_manager.show_welcome(str(self._source))
        self._console_manager.print_log(f"Всего файлов: {self._path_model.files_count}")

    def sort(self) -> None:
        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                TextColumn("[dim]{task.fields[current_file]}"),
                console=self._console_manager.console,
                transient=False,  # Прогресс-бар исчезнет после завершения
                refresh_per_second=10
        ) as progress:
            task = progress.add_task(
                "[cyan]Сортировка...",
                total=self._path_model.files_count,
                current_file=""
            )

            for i, file in enumerate(self._path_model.files):
                progress.update(
                    task,
                    advance=1,
                    current_file=f"[yellow]{file.name}[/yellow]"
                )

                self._move_file_in_type_folder(file)
                time.sleep(0.1)

                progress.update(
                    task,
                    description=f"[cyan]Сортировка... ({i}/{self._path_model.files_count})"
                )

        self._console_manager.print_success("Все файлы отсортированы")

    def _move_file_in_type_folder(self, file: Path) -> None:
        model: FileModel = FileModel(file, self._source)
        model.move()


@console_app.command()
def sorter(
    source: Path = Argument(..., help="Путь к папке с исходными файлами"),
    silent: bool = Option(False, "--silent", help="Не выводить логи")
) -> None:
    """Функция сортировки файлов по типам в папке.

    Args:
        source (Path): Путь к папке с исходными файлами.
        silent (bool): Не выводить логи.
    """
    try:
        Sorter(source, silent).sort()
    except SystemError:
        return

