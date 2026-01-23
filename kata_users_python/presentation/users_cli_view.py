from kata_users_python.composition_root import CompositionRoot, UsersView
from kata_users_python.domain.users.entities import User


class UserCLIView(UsersView):
    def __init__(self) -> None:
        self.presenter = CompositionRoot.provide_presenter(view=self)

    def init(self) -> None:
        self.presenter.init_screen()

    def show_hello_message(self) -> None:
        print("Hello world!")

    def show_error(self, message: str, error_type: str | None = None) -> None:
        print("Error!")

    def start_loading(self) -> None:
        print("Loading...")

    def stop_loading(self) -> None:
        print("Stop loading")

    def show_main_options(self) -> None:
        print("Main options!!!")

    def list_users(self, users: list[User]) -> None:
        print("Listing users...")
