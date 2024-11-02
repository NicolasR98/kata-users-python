from pydantic import ConfigDict, Field, RootModel


class Password(RootModel):
    root: str = Field(min_length=8, pattern=r"/^(?=.*[A-Za-z])(?=.*\d).{8,}$/")

    model_config = ConfigDict(frozen=True)
