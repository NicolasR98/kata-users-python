from unittest.mock import NonCallableMagicMock

from kata_users_python.composition_root import CompositionRoot
from kata_users_python.domain.users.repositories import UserRepository
from kata_users_python.presentation.users_presenter import UsersPresenter
from kata_users_python.presentation.users_view import UsersView


class TestCompositionRoot:
    def test_initialization(self):
        mock_user_view = NonCallableMagicMock(spec=UsersView)
        composition_root = CompositionRoot()
        presenter = composition_root.provide_presenter(view=mock_user_view)

        assert isinstance(composition_root.user_repository, UserRepository)
        assert isinstance(presenter, UsersPresenter)
