from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.repositories import UserRepository


class ListUsersUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self) -> list[User]:
        return await self.user_repository.get_list()
