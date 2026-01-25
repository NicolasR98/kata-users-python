from kata_users_python.composition_root import CompositionRoot, UsersView
from kata_users_python.domain.users.entities import User


class UserCLIView(UsersView):
    def __init__(self) -> None:
        self.composition_root = CompositionRoot()
        self.presenter = self.composition_root.provide_presenter(view=self)

    async def init(self) -> None:
        self.presenter.init_screen()
        await self.show_main_options()

    def show_hello_message(self) -> None:
        print("Hello world!")

    def show_exit_message(self) -> None:
        return print("Bye bye...")

    def show_error(self, message: str, error_type: str | None = None) -> None:
        print("Error!")

    def start_loading(self) -> None:
        print("Loading...")

    def stop_loading(self) -> None:
        print("Stop loading")

    async def show_main_options(self) -> None:
        while True:
            option = input("Select an option:")

            if option == "1":
                await self.presenter.list_users()
            if option == "0":
                break

        self.show_exit_message()

    def list_users(self, users: list[User]) -> None:
        for user in users:
            print(f"- {user.name.root}, {user.email.root}")
