from dataclasses import dataclass
from pathlib import Path


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
