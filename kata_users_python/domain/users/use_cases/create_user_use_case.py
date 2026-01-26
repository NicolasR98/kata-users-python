from dataclasses import asdict, dataclass

from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.errors import (
    EmailAlreadyExistsError,
    EmailDomainAlreadyExistsError,
)
from kata_users_python.domain.users.repositories import UserRepository


@dataclass(frozen=True)
class CreateAddressInput:
    address: str
    city: str
    zip: str


@dataclass(frozen=True)
class CreateUserInput:
    address: CreateAddressInput
    email: str
    name: str
    password: str


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, input_data: CreateUserInput) -> User:
        user = User.model_validate(asdict(input_data))

        email_already_exists = await self.user_repository.get_by_email(email=user.email)

        if email_already_exists:
            raise EmailAlreadyExistsError

        email_domain_already_exists = await self.user_repository.get_by_email_domain(
            email=user.email
        )

        if email_domain_already_exists:
            raise EmailDomainAlreadyExistsError

        await self.user_repository.create(user)

        return user
