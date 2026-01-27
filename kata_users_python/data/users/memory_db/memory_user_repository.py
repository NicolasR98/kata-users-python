from pydantic import validate_call

from kata_users_python.domain.common.vos import Id
from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.repositories import UserRepository
from kata_users_python.domain.users.vos import Email


class MemoryUserRepository(UserRepository):
    def __init__(self, data: dict[Id, User] | None = None) -> None:
        self._data: dict[Id, User] = data or {}

    async def get_list(self) -> list[User]:
        return list(self._data.values())

    @validate_call
    async def get_by_id(self, user_id: Id) -> User | None:
        return self._data.get(user_id, None)

    @validate_call
    async def get_by_email(self, email: Email) -> User | None:
        return next((user for user in self._data.values() if user.email == email), None)

    @validate_call
    async def get_by_email_domain(self, email: Email) -> list[User]:
        def _get_domain(email: Email) -> str:
            return email.root.split("@")[1].split(".")[0]

        domain = _get_domain(email)
        users_list = await self.get_list()

        return [user for user in users_list if _get_domain(user.email) == domain]

    @validate_call
    async def create(self, user: User) -> None:
        self._data[user.id] = user

    @validate_call
    async def update(self, user: User) -> None:
        if user.id in self._data:
            self._data[user.id] = user

    @validate_call
    async def delete(self, user_id: Id) -> None:
        if user_id in self._data:
            del self._data[user_id]
