from kata_users_python.composition_root import CompositionRoot
from kata_users_python.domain.users.repositories import UserRepository
from kata_users_python.presentation.users.users_cli_view import UserCLIView
from kata_users_python.presentation.users.users_presenter import UsersPresenter


class TestCompositionRoot:
    def test_initialization(self):
        composition_root = CompositionRoot()
        presenter = composition_root.provide_presenter()

        assert isinstance(composition_root.user_repository, UserRepository)
        assert isinstance(composition_root.view, UserCLIView)
        assert isinstance(presenter, UsersPresenter)
