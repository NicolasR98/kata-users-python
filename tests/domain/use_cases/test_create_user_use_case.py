from unittest.mock import AsyncMock, MagicMock

import pytest

from kata_users_python.domain.users.use_cases import CreateUserUseCase
from kata_users_python.domain.users.use_cases.create_user_use_case import (
    AddressInput,
    CreateUserInput,
)


@pytest.mark.asyncio
class TestCreateUserUseCase:
    async def test_valid_case(self, mock_user_repository: MagicMock):
        use_case = CreateUserUseCase(user_repository=mock_user_repository)

        input_data = CreateUserInput(
            email="user@test.com",
            name="Pepito",
            password="iker2026",
            address=AddressInput(address="street 123", city="ny", zip="1234567"),
        )
        mock_user_repository.get_by_email_domain = AsyncMock(return_value=[])
        mock_user_repository.get_by_email = AsyncMock(return_value=None)

        await use_case(input_data=input_data)

        mock_user_repository.create.assert_called_once()
