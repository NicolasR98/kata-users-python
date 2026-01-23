from kata_users_python.composition_root import CompositionRoot
from kata_users_python.domain.users.repositories import UserRepository
from kata_users_python.domain.users.use_cases import (
    CreateUserUseCase,
    DeleteUserByEmailUseCase,
    ListUsersUseCase,
    UpdateUserUseCase,
)


class TestCompositionRoot:
    def test_initialization(self):
        composition_root = CompositionRoot()

        assert isinstance(composition_root.user_repository, UserRepository)
        assert isinstance(
            composition_root.provide_create_user_use_case(), CreateUserUseCase
        )
        assert isinstance(
            composition_root.provide_list_users_use_case(), ListUsersUseCase
        )
        assert isinstance(
            composition_root.provide_update_user_use_case(), UpdateUserUseCase
        )
        assert isinstance(
            composition_root.provide_delete_user_by_email_use_case(),
            DeleteUserByEmailUseCase,
        )
