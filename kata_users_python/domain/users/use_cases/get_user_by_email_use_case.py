from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.errors import UserNotFoundError
from kata_users_python.domain.users.repositories import UserRepository


class GetUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, email: str) -> User:
        user = await self.user_repository.get_by_email(email=email)

        if user is None:
            raise UserNotFoundError

        return user
