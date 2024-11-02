from pydantic import ConfigDict, Field, RootModel


class Name(RootModel):
    root: str = Field(min_length=2)

    model_config = ConfigDict(frozen=True)
