from unittest.mock import MagicMock

import pytest
from polyfactory.pytest_plugin import register_fixture

from kata_users_python.domain.users.repositories import UserRepository
from tests.factories.models import UserMother

user_mother = register_fixture(UserMother)


@pytest.fixture
def mock_user_repository() -> MagicMock:
    return MagicMock(spec=UserRepository)
