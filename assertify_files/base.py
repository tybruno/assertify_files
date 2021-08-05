from abc import (
    ABC,
    abstractmethod,
)
from enum import Enum
from pathlib import Path
from string import Template
from typing import (
    Optional,
    Type,
    Union,
)


class FileExtensions(Enum):
    TEXT = {".txt"}
    EXCEL = {".xlsx", ".xlx"}
    CSV = {".csv"}


class AbstractAssertiyFile(ABC):
    def __init__(
        self,
        raises: Optional[Union[None, Type[Exception], Type[AssertionError]]],
        msg: Optional[Union[None, str, Template]],
    ):
        ...

    @abstractmethod
    def __call__(self, file: Union[str, Path]) -> bool:
        ...
