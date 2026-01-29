"""Модуль консольного менеджера."""

from rich import get_console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn


class ConsoleManager:
    """
    Класс консольного менеджера.

    Attributes:
        _console: Экземпляр для работы с консолью.
        _silent (bool): Флаг, указывающий на то, что вывод в консоль отключен.
    """

    def __init__(self, silent: bool) -> None:
        """
        Конструктор класса.

        Args:
            silent (bool): Флаг, указывающий на то, что вывод в консоль отключен.
        """
        self._console = get_console()
        self._silent: bool = silent

    @property
    def progress(self) -> Progress:
        """
        Метод получения экземпляра прогресс-бара.

        Returns:
            (Progress): Экземпляр прогресс-бара.

        Examples:
            >>> import time
            >>>
            >>> console_manager: ConsoleManager = ConsoleManager(False)
            >>>
            >>> with console_manager.progress as progress:
            ...     task = progress.add_task("[cyan]Сортировка...", total=100, current_file="")
            ...     for i, file in enumerate([..., ..., ...]):
            ...         progress.update(task, advance=1, current_file=f"[yellow]{file.name}[/yellow]")
            ...         # Эмуляция долгой операции
            ...         time.sleep(0.1)
            ...         progress.update(task, description=f"[cyan]Сортировка... ({i}/{100})")
        """
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TextColumn("[dim]{task.fields[current_file]}"),
            console=self._console,
            transient=False,
            refresh_per_second=10,
        )

    def show_welcome(self, path: str | None = None) -> None:
        """
        Метод вывода приветственного сообщения.

        Args:
            path (str | None): Путь к папке, в которой происходит сортировка.

        Examples:
            >>> class Sorter:
            ...     def __init__(self) -> None:
            ...         self._console_manager: ConsoleManager = ConsoleManager(False)
            ...         self._console_manager.show_welcome()
        """
        self._print(
            Panel.fit(
                "[bold green]📁  DH|FileSorter[/bold green] \n\n"
                "Утилита для сортировки файлов по типам в папке."
                + ("\n\nПуть: [bold cyan]" + path + "[/bold cyan]" if path else ""),
                border_style="green",
            )
        )

    def print_log(self, message: str) -> None:
        """
        Вывод сообщения-лога в консоль.

        Args:
            message (str): Сообщение для вывода.

        Examples:
            >>> console_manager: ConsoleManager = ConsoleManager(False)
            >>> console_manager.print_log("Файл успешно перемещен.")
        """
        self._print(f"[yellow]→ {message}[/yellow]")

    def print_error(self, message: str) -> None:
        """
        вывод сообщения об ошибке в консоль.

        Args:
            message (str): Сообщение об ошибке.

        Examples:
            >>> console_manager: ConsoleManager = ConsoleManager(False)
            >>> console_manager.print_error("Ошибка при перемещении файла.")
        """
        self._print(f"[red]✗ {message}[/red]")

    def print_success(self, message: str) -> None:
        """
        Вывод сообщения об успешном выполнении операции в консоль.

        Args:
            message (str): Сообщение об успешном выполнении операции.

        Examples:
            >>> console_manager: ConsoleManager = ConsoleManager(False)
            >>> console_manager.print_success("Сортировка успешно завершена.")
        """
        self._print(f"[green]✓ {message}[/green]")

    def _print(self, message: str | Panel) -> None:
        """
        Метод вывода сообщения в консоль с проверкой на отключенный режим.

        Args:
            message (str | Panel): Сообщение для вывода.
        """
        if self._silent:
            return

        self._console.print(message)
