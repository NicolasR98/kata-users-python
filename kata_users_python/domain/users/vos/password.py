import re

from pydantic import ConfigDict, Field, RootModel

PASSWORD_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")


class Password(RootModel):
    root: str = Field(min_length=8, pattern=PASSWORD_REGEX)

    model_config = ConfigDict(regex_engine="python-re", frozen=True)
