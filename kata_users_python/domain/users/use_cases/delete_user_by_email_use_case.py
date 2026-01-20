from kata_users_python.domain.users.errors import UserNotFoundError
from kata_users_python.domain.users.repositories import UserRepository


class DeleteUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, email: str) -> None:
        user = await self.user_repository.get_by_email(email=email)

        if user is None:
            raise UserNotFoundError

        await self.user_repository.delete(user_id=user.id)
