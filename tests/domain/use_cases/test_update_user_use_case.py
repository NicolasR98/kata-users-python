from unittest.mock import MagicMock

import pytest

from kata_users_python.domain.users.errors import UserNotFoundError
from kata_users_python.domain.users.use_cases import UpdateUserUseCase
from kata_users_python.domain.users.use_cases.update_user_use_case import (
    AddressInput,
    UpdateUserInput,
)
from tests.factories.models import UserMother


@pytest.fixture
def user_input() -> UpdateUserInput:
    return UpdateUserInput(
        address=AddressInput(address="street 123", city="ny", zip="1234567"),
        name="Pepito updated",
        password="2026iker",
    )


@pytest.mark.asyncio
class TestUpdateUserUseCase:
    async def test_valid_case(
        self,
        mock_user_repository: MagicMock,
        user_mother: UserMother,
        user_input: UpdateUserInput,
    ):
        user = user_mother.build()
        use_case = UpdateUserUseCase(user_repository=mock_user_repository)

        mock_user_repository.get_by_id.return_value = user

        await use_case(user_id=user.id, input_data=user_input)

        mock_user_repository.update.assert_called_once()

    async def test_user_not_found(
        self,
        mock_user_repository: MagicMock,
        user_mother: UserMother,
        user_input: UpdateUserInput,
    ):
        user = user_mother.build()
        use_case = UpdateUserUseCase(user_repository=mock_user_repository)

        mock_user_repository.get_by_id.return_value = None

        with pytest.raises(UserNotFoundError):
            await use_case(user_id=user.id, input_data=user_input)

    async def test_invalid_input_data(
        self,
        mock_user_repository: MagicMock,
        user_mother: UserMother,
    ):
        invalid_user_input = {}
        user = user_mother.build()
        use_case = UpdateUserUseCase(user_repository=mock_user_repository)

        mock_user_repository.get_by_id.return_value = user

        with pytest.raises(TypeError):
            await use_case(user_id=user.id, input_data=invalid_user_input)
