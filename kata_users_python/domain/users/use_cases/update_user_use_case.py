from dataclasses import asdict, dataclass

from kata_users_python.domain.common.vos import Id
from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.errors import UserNotFoundError
from kata_users_python.domain.users.repositories import UserRepository


@dataclass(frozen=True)
class AddressInput:
    address: str
    city: str
    zip: str


@dataclass(frozen=True)
class UpdateUserInput:
    address: AddressInput
    name: str
    password: str


class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, user_id: Id, input_data: UpdateUserInput):
        existing_user = await self.user_repository.get_by_id(user_id=user_id)

        if existing_user is None:
            raise UserNotFoundError

        user = User.model_validate(**existing_user.model_dump(), **asdict(input_data))

        await self.user_repository.update(user=user)

        return user
