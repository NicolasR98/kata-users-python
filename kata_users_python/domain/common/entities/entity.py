from typing import TypeVar

from pydantic import BaseModel, Field

from kata_users_python.domain.common.vos import Id

T = TypeVar("T", bound="Entity")


class Entity(BaseModel):
    id: Id = Field(default_factory=lambda: Id())

    def equals(self, obj: T | None = None) -> bool:
        if obj is None:
            return False
        if self is obj:
            return True
        if not isinstance(obj, Entity):
            return False
        return self.id == obj.id
