from typing import Annotated

from pydantic import AfterValidator, ConfigDict, EmailStr, RootModel


class Email(RootModel):
    root: Annotated[EmailStr, AfterValidator(lambda x: x.lower())]

    model_config = ConfigDict(frozen=True)
