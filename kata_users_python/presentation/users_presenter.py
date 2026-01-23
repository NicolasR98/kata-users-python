from kata_users_python.domain.users.use_cases import (
    CreateUserUseCase,
    DeleteUserByEmailUseCase,
    ListUsersUseCase,
    UpdateUserUseCase,
)
from kata_users_python.presentation.users_view import UsersView


class UsersPresenter:
    def __init__(
        self,
        view: UsersView,
        list_users_use_case: ListUsersUseCase,
        create_user_use_case: CreateUserUseCase,
        update_user_use_case: UpdateUserUseCase,
        delete_user_by_email_use_case: DeleteUserByEmailUseCase,
    ) -> None:
        self.view = view
        self.list_users_use_case = list_users_use_case
        self.create_user_use_case = create_user_use_case
        self.update_user_use_case = update_user_use_case
        self.delete_user_by_email_use_case = delete_user_by_email_use_case

    def init_screen(self) -> None:
        self.view.show_hello_message()
        self.view.show_main_options()

    async def list_users(self) -> None:
        try:
            self.view.start_loading()
            users = await self.list_users_use_case()
            self.view.list_users(users=users)

        except Exception as error:
            self.view.show_error(message=str(error))

        finally:
            self.view.stop_loading()
