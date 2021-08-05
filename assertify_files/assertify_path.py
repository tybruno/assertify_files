from dataclasses import (
    dataclass,
    field,
)
from pathlib import Path
from string import Template
from typing import (
    Iterable,
    Optional,
    Type,
    Union,
)

from assertifiers.container import AssertifyIn
from assertifiers.logic import (
    AssertifyFalse,
    AssertifyTrue,
)

from assertify_files.base import AbstractAssertiyFile


@dataclass
class AssertifyPathFileExtension(AbstractAssertiyFile):
    valid_extensions: Iterable
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(
        default=Template(
            "'$path' does not have a valid file extension $valid_extensions"
        )
    )

    def __call__(self, path: Path) -> bool:

        asserity_in = AssertifyIn(
            raises=self.raises,
            msg=self.msg.substitute(
                path=path, valid_extensions=self.valid_extensions
            ),
        )
        return asserity_in(member=path.suffix, container=self.valid_extensions)


@dataclass
class AssertifyPathFileExists(AbstractAssertiyFile):
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=FileNotFoundError)
    msg: Optional[Union[None, str, Template]] = field(
        default=Template("'$path' is not a file")
    )

    def __call__(self, path: Path) -> bool:
        assertify_true = AssertifyTrue(
            raises=self.raises, msg=self.msg.substitute(path=path)
        )
        return assertify_true(expr=path.is_file())


@dataclass
class AssertifyPathFileNotExists(AbstractAssertiyFile):
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=FileExistsError)
    msg: Optional[Union[None, str, Template]] = field(
        default=Template("'$path' exists")
    )

    def __call__(self, path: Path) -> bool:
        assertify_false = AssertifyFalse(
            raises=self.raises, msg=self.msg.substitute(path=Path)
        )
        return assertify_false(expr=path.is_file())
