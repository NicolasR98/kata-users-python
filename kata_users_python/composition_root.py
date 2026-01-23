from kata_users_python.common import Singleton
from kata_users_python.data import MemoryUserRepository
from kata_users_python.domain.users.use_cases import (
    CreateUserUseCase,
    DeleteUserByEmailUseCase,
    ListUsersUseCase,
    UpdateUserUseCase,
)
from kata_users_python.presentation.users_presenter import UsersPresenter
from kata_users_python.presentation.users_view import UsersView


class CompositionRoot(metaclass=Singleton):
    def __init__(self) -> None:
        self.user_repository = MemoryUserRepository()

    def provide_presenter(self, view: UsersView) -> UsersPresenter:
        return UsersPresenter(
            view=view,
            list_users_use_case=ListUsersUseCase(user_repository=self.user_repository),
            create_user_use_case=CreateUserUseCase(
                user_repository=self.user_repository
            ),
            update_user_use_case=UpdateUserUseCase(
                user_repository=self.user_repository
            ),
            delete_user_by_email_use_case=DeleteUserByEmailUseCase(
                user_repository=self.user_repository
            ),
        )
