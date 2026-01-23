from kata_users_python.common import Singleton
from kata_users_python.data import MemoryUserRepository
from kata_users_python.domain.users.use_cases import (
    CreateUserUseCase,
    DeleteUserByEmailUseCase,
    ListUsersUseCase,
    UpdateUserUseCase,
)


class CompositionRoot(metaclass=Singleton):
    def __init__(self) -> None:
        self.user_repository = MemoryUserRepository()

    def provide_list_users_use_case(self) -> ListUsersUseCase:
        return ListUsersUseCase(user_repository=self.user_repository)

    def provide_create_user_use_case(self) -> CreateUserUseCase:
        return CreateUserUseCase(user_repository=self.user_repository)

    def provide_update_user_use_case(self) -> UpdateUserUseCase:
        return UpdateUserUseCase(user_repository=self.user_repository)

    def provide_delete_user_by_email_use_case(self) -> DeleteUserByEmailUseCase:
        return DeleteUserByEmailUseCase(user_repository=self.user_repository)
