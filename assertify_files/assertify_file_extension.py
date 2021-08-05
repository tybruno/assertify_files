from dataclasses import (
    dataclass,
    field,
)
from pathlib import Path
from string import Template
from typing import (
    Callable,
    Iterable,
    Optional,
    Type,
    Union,
)

from assertifiers.container import AssertifyIn

from assertify_files.base import AssertiyFile
from assertify_files.str_to_path import StrToPath


@dataclass
class AssertifyFileExtension(AssertiyFile):
    valid_extensions: Iterable
    convert_to_path: Callable = field(default=StrToPath(), init=False)
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(
        default=Template(
            "'$file' does not have a valid file extension $valid_extensions"
        )
    )

    def __call__(self, file: Union[str, Path]) -> bool:
        path = self.convert_to_path(file)

        asserity_in = AssertifyIn(
            raises=self.raises,
            msg=self.msg.substitute(
                file=file, valid_extensions=self.valid_extensions
            ),
        )
        return asserity_in(member=path.suffix, container=self.valid_extensions)
