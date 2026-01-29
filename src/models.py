"""Модуль вспомогательных моделей для работы с файлами и папками."""

import shutil
from pathlib import Path
from typing import Any, Generator

from .consts import FILE_TYPE_EXTENSIONS_MAPPING, FileTypes


class PathModel:
    """
    Модель для работы с папками.

    Attributes:
        _path(Path): Путь к папке.
    """

    def __init__(self, path: Path, skip_check: bool = False) -> None:
        """
        Инициализация модели.

        Args:
            path (Path): Путь к папке.
            skip_check (bool): Пропуск проверки существования папки.
        """
        self._path: Path = path

        if not skip_check:
            self._check_exists()

    @property
    def files_count(self) -> int:
        """
        Количество файлов в папке. Не учитывает вложенные папки.

        Returns:
            (int): Количество файлов.

        Examples:
            >>> PathModel(Path("test")).files_count # Количество файлов в папке "test"
        """
        file_count: int = 0

        for item in self._path.iterdir():
            if item.is_file():
                file_count += 1

        return file_count

    @property
    def files(self) -> Generator[Path, Any, None]:
        """
        Итератор по файлам в папке.

        Returns:
            (Path): Итератор по файлам.

        Examples:
            >>> for file in PathModel(Path("test")).files:
            ...     print(file) # Итерация по файлам в папке "test"
        """
        for item in self._path.iterdir():
            if item.is_file():
                yield item

    def create(self) -> None:
        """
        Создание папки. Если папка уже существует, то ничего не делает.

        Examples:
            >>> PathModel(Path("test")).create() # Создание папки "test"
        """
        self._path.mkdir(parents=True, exist_ok=True)

    def _check_exists(self) -> None:
        """Проверка существования папки."""
        if not self._path.exists():
            raise FileNotFoundError(f"Папка {self._path} не найдена")

        if not self._path.is_dir():
            raise NotADirectoryError(f"{self._path} не является папкой")


class FileModel:
    """
    Модель для работы с файлами.

    Attributes:
        _path(Path): Путь к файлу.
        _source(Path): Путь к папке, в которую нужно переместить файл.
    """

    def __init__(self, path: Path, source: Path) -> None:
        """
        Инициализация модели.

        Args:
            path (Path): Путь к файлу.
            source (Path): Путь к папке, в которую нужно переместить файл.
        """
        self._path: Path = path
        self._source: Path = source

    @property
    def file_type(self) -> str:
        """
        Тип файла. Определяется по расширению файла.

        Returns:
            (str): Тип файла для сортировки.

        Examples:
            >>> FileModel(Path("test.txt")).file_type # Тип файла "document" (FileTypes.DOCUMENT)
        """
        file_type: str = self._path.suffix.lower().lstrip(".")

        for type_name, extensions in FILE_TYPE_EXTENSIONS_MAPPING.items():
            if file_type in extensions:
                return type_name

        return FileTypes.OTHER

    @property
    def folder_type_name(self) -> str:
        """
        Название папки для сортировки. Делает тип файла (self.file_type) заглавным.

        Returns:
            str: Название папки для сортировки.

        Examples:
            >>> FileModel(Path("test.txt")).folder_type_name # Название папки "Document"
        """
        return self.file_type.title()

    @property
    def folder(self) -> Path:
        """
        Папка для сортировки. Создает папку, если ее нет.

        Returns:
            (Path): Папка для сортировки.

        Examples:
            >>> FileModel(Path("test.txt")).folder # Папка "Document"
        """
        path: Path = Path(self._source / self.folder_type_name)
        PathModel(path, True).create()
        return path

    def move(self) -> None:
        """
        Перемещение файла в папку.

        Examples:
            >>> FileModel(Path("test.txt")).move() # Перемещение файла "test.txt" в папку "Document"
        """
        shutil.move(str(self._path), str(self.folder))
