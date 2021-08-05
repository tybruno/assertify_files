from dataclasses import (
    dataclass,
    field,
)
from pathlib import Path
from typing import (
    Callable,
)

from assertify_files.assertify_path import (
    AssertifyPathFileExists,
    AssertifyPathFileExtension,
    AssertifyPathFileNotExists,
)


@dataclass
class StrToPath:
    def __call__(self, string: str) -> Path:
        if isinstance(string, str):
            path = Path(string)
            return path
        elif isinstance(string, Path):
            return string

        raise TypeError(
            f"{string} is of type {type(string)} not {type(str())}"
        )


@dataclass
class AssertifyFileExtension(AssertifyPathFileExtension):
    convert_to_path: Callable = field(default=StrToPath(), init=False)

    def __call__(self, file: str) -> bool:
        path = self.convert_to_path(file)
        return super().__call__(path=path)


@dataclass
class AssertifyFileExists(AssertifyPathFileExists):
    convert_to_path: Callable = field(default=StrToPath(), init=False)

    def __call__(self, file: str) -> bool:
        path = self.convert_to_path(file)
        return super().__call__(path=path)


@dataclass
class AssertifyFileExists(AssertifyPathFileNotExists):
    convert_to_path: Callable = field(default=StrToPath(), init=False)

    def __call__(self, file: str) -> bool:
        path = self.convert_to_path(file)
        return super().__call__(path=path)
