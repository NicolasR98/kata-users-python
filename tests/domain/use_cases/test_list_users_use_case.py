from unittest.mock import MagicMock

import pytest

from kata_users_python.domain.users.use_cases import ListUsersUseCase


@pytest.mark.asyncio
class TestListUsersUseCase:
    async def test_valid_case(self, mock_user_repository: MagicMock):
        use_case = ListUsersUseCase(user_repository=mock_user_repository)

        await use_case()

        mock_user_repository.get_list.assert_called_once()
