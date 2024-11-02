import uuid

from pydantic import ConfigDict, Field, RootModel


class Id(RootModel):
    root: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())

    model_config = ConfigDict(frozen=True)
