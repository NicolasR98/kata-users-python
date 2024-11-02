from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    address: str
    city: str
    zip: str

    model_config = ConfigDict(frozen=True)
