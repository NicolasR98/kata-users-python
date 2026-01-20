from abc import ABC, abstractmethod

from kata_users_python.domain.common.vos import Id
from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.vos import Email


class UserRepository(ABC):
    @abstractmethod
    async def get_list(self) -> list[User]:
        pass

    @abstractmethod
    async def get_by_email(self, email: Email) -> User | None:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: Id) -> User | None:
        pass

    @abstractmethod
    async def get_by_email_domain(self, email: Email) -> list[User]:
        pass

    @abstractmethod
    async def create(self, user: User) -> None:
        pass

    @abstractmethod
    async def update(self, user: User) -> None:
        pass

    @abstractmethod
    async def delete(self, user_id: Id) -> None:
        pass
