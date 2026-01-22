from unittest.mock import AsyncMock, MagicMock

import pytest

from kata_users_python.domain.users.errors import (
    EmailAlreadyExistsError,
    EmailDomainAlreadyExistsError,
)
from kata_users_python.domain.users.use_cases import CreateUserUseCase
from kata_users_python.domain.users.use_cases.create_user_use_case import (
    AddressInput,
    CreateUserInput,
)
from tests.factories.models import UserMother


@pytest.fixture
def user_input() -> CreateUserInput:
    return CreateUserInput(
        email="user@test.com",
        name="Pepito",
        password="iker2026",
        address=AddressInput(address="street 123", city="ny", zip="1234567"),
    )


@pytest.mark.asyncio
class TestCreateUserUseCase:
    async def test_valid_case(
        self, mock_user_repository: MagicMock, user_input: CreateUserInput
    ):
        use_case = CreateUserUseCase(user_repository=mock_user_repository)

        mock_user_repository.get_by_email_domain = AsyncMock(return_value=[])
        mock_user_repository.get_by_email = AsyncMock(return_value=None)

        await use_case(input_data=user_input)

        mock_user_repository.create.assert_called_once()

    async def test_email_already_exists(
        self,
        mock_user_repository: MagicMock,
        user_input: CreateUserInput,
        user_mother: UserMother,
    ):
        use_case = CreateUserUseCase(user_repository=mock_user_repository)
        user = user_mother.build(email=user_input.email)

        mock_user_repository.get_by_email = AsyncMock(return_value=user)
        mock_user_repository.get_by_email_domain = AsyncMock(return_value=[])

        with pytest.raises(EmailAlreadyExistsError):
            await use_case(input_data=user_input)

        mock_user_repository.get_by_email_domain.assert_not_called()
        mock_user_repository.create.assert_not_called()

    async def test_domain_already_exists(
        self,
        mock_user_repository: MagicMock,
        user_input: CreateUserInput,
        user_mother: UserMother,
    ):
        use_case = CreateUserUseCase(user_repository=mock_user_repository)
        user = user_mother.build(email="user2@test.com")

        mock_user_repository.get_by_email = AsyncMock(return_value=None)
        mock_user_repository.get_by_email_domain = AsyncMock(return_value=[user])

        with pytest.raises(EmailDomainAlreadyExistsError):
            await use_case(input_data=user_input)

        mock_user_repository.create.assert_not_called()
