from kata_users_python.domain.users.errors import UserNotFoundError
from kata_users_python.domain.users.use_cases import (
    CreateUserUseCase,
    DeleteUserByEmailUseCase,
    GetUserByEmailUseCase,
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
        get_user_by_email_use_case: GetUserByEmailUseCase,
    ) -> None:
        self.view = view
        self.list_users_use_case = list_users_use_case
        self.create_user_use_case = create_user_use_case
        self.update_user_use_case = update_user_use_case
        self.delete_user_by_email_use_case = delete_user_by_email_use_case
        self.get_user_by_email_use_case = get_user_by_email_use_case

    async def start(self) -> None:
        while True:
            option = self.view.show_main_options()

            if option == "1":
                await self.handle_display_users()

            elif option == "2":
                await self.handle_display_user()

            elif option == "3":
                await self.handle_create_user()

            elif option == "4":
                await self.handle_update_user()

            elif option == "5":
                await self.handle_delete_user()

            elif option == "0":
                self.view.show_exit_message()
                return

            else:
                self.view.show_error("Invalid option")

    async def handle_display_users(self) -> None:
        try:
            self.view.start_loading()
            users = await self.list_users_use_case()
            self.view.render_users(users=users)

        except Exception as error:
            self.view.show_error(message=str(error))

        finally:
            self.view.stop_loading()

    async def handle_display_user(self) -> None:
        try:
            email = self.view.ask_input("Email")

            self.view.start_loading()

            user = await self.get_user_by_email_use_case(email=email)

            self.view.render_user(user=user)

        except UserNotFoundError:
            self.view.show_error(message="User not found")

        except Exception as error:
            self.view.show_error(message=str(error))

        finally:
            self.view.stop_loading()

    async def handle_create_user(self) -> None:
        try:
            input_data = self.view.ask_create_user_input()

            self.view.start_loading()

            user = await self.create_user_use_case(input_data=input_data)

            self.view.stop_loading()

            self.view.render_user(user=user)

        except UserNotFoundError:
            self.view.show_error(message="User not found")

        except Exception as error:
            self.view.show_error(message=str(error))

    async def handle_update_user(self) -> None:
        try:
            user_email = self.view.ask_input("Email")

            self.view.start_loading()

            existing_user = await self.get_user_by_email_use_case(email=user_email)

            self.view.stop_loading()

            input_data = self.view.ask_update_user_input()

            self.view.start_loading()

            user = await self.update_user_use_case(
                user_id=existing_user.id, input_data=input_data
            )

            self.view.stop_loading()

            self.view.render_user(user=user)

        except UserNotFoundError:
            self.view.show_error(message="User not found")

        except Exception as error:
            self.view.show_error(message=str(error))

    async def handle_delete_user(self) -> None:
        try:
            user_email = self.view.ask_input("Email")

            self.view.start_loading()

            await self.delete_user_by_email_use_case(email=user_email)

            self.view.stop_loading()

            self.view.show_message(f"User {user_email} successfully deleted")

        except UserNotFoundError:
            self.view.show_error(message="User not found")

        except Exception as error:
            self.view.show_error(message=str(error))
