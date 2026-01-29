import shutil
from pathlib import Path
from typing import Any, Generator

from .consts import FILE_TYPE_EXTENSIONS_MAPPING, FileTypes


class PathModel:
    def __init__(self, path: Path) -> None:
        self._path: Path = path
        self._check_exists()

    @property
    def files_count(self) -> int:
        file_count: int = 0

        for item in self._path.iterdir():
            if item.is_file():
                file_count += 1

        return file_count

    @property
    def files(self) -> Generator[Path, Any, None]:
        for item in self._path.iterdir():
            if item.is_file():
                yield item

    def _check_exists(self) -> None:
        if not self._path.exists():
            raise FileNotFoundError(f"Папка {self._path} не найдена")

        if not self._path.is_dir():
            raise NotADirectoryError(f"{self._path} не является папкой")


class FileModel:
    def __init__(self, path: Path, source: Path) -> None:
        self._path: Path = path
        self._source: Path = source

    @property
    def file_type(self) -> str:
        file_type: str = self._path.suffix.lower().lstrip(".")

        for type_name, extensions in FILE_TYPE_EXTENSIONS_MAPPING.items():
            if file_type in extensions:
                return type_name

        return FileTypes.OTHER

    @property
    def folder_type_name(self) -> str:
        return self.file_type.title()

    @property
    def folder(self) -> Path:
        path: Path = Path(self._source / self.folder_type_name)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def move(self) -> None:
        shutil.move(str(self._path), str(self.folder))
