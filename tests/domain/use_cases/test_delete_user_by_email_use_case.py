from unittest.mock import MagicMock

import pytest

from kata_users_python.domain.users.errors import UserNotFoundError
from kata_users_python.domain.users.use_cases import DeleteUserByEmailUseCase
from tests.factories.models import UserMother


@pytest.mark.asyncio
class TestDeleteUserByEmailUseCase:
    async def test_valid_case(
        self, mock_user_repository: MagicMock, user_mother: UserMother
    ):
        user = user_mother.build()
        use_case = DeleteUserByEmailUseCase(user_repository=mock_user_repository)
        mock_user_repository.get_by_email.return_value = user

        await use_case(email=user.email.root)

        mock_user_repository.delete.assert_called_with(user_id=user.id)

    async def test_user_not_found(self, mock_user_repository: MagicMock):
        use_case = DeleteUserByEmailUseCase(user_repository=mock_user_repository)
        mock_user_repository.get_by_email.return_value = None

        with pytest.raises(UserNotFoundError):
            await use_case(email="email@test.com")

        mock_user_repository.delete.assert_not_called()
