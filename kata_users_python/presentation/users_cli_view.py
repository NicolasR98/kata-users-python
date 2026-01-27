from kata_users_python.composition_root import UsersView
from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.use_cases.create_user_use_case import (
    CreateAddressInput,
    CreateUserInput,
)
from kata_users_python.domain.users.use_cases.update_user_use_case import (
    UpdateAddressInput,
    UpdateUserInput,
)


class UserCLIView(UsersView):
    def show_message(self, message: str) -> None:
        print(message)

    def show_error(self, message: str, error_type: str | None = None) -> None:
        print("[Error] -", message)

    def start_loading(self) -> None:
        print("Loading... \n")

    def stop_loading(self) -> None:
        print("Stop loading\n")

    def show_main_options(self) -> str:
        print("\nOptions:")
        print("1 - Read all users")
        print("2 - Read user by email")
        print("3 - Create user")
        print("4 - Update user")
        print("5 - Delete user")
        print("0 - Exit")

        return input("> ")

    def render_users(self, users: list[User]) -> None:
        for _, user in enumerate(users):
            self.render_user(user)

    def render_user(self, user: User) -> None:
        print(
            "----\n"
            f"Name    : {user.name.root}\n"
            f"Email   : {user.email.root}\n"
            "Address :\n"
            f"  Street: {user.address.address}\n"
            f"  City  : {user.address.city}\n"
            f"  ZIP   : {user.address.zip}"
            "\n"
        )

    def ask_input(self, key: str) -> str:
        return input(f"{key}: ")

    def ask_create_user_input(self) -> CreateUserInput:
        name = input("Name: ")
        email = input("Email: ")
        password = input("Password: ")
        address = input("Address: ")
        city = input("City: ")
        zip = input("ZIP code: ")

        address = CreateAddressInput(address=address, city=city, zip=zip)

        return CreateUserInput(
            address=address,
            email=email,
            name=name,
            password=password,
        )

    def ask_update_user_input(self) -> UpdateUserInput:
        name = input("Name: ") or None
        password = input("Password: ") or None
        address = input("Address: ") or None
        city = input("City: ") or None
        zip = input("ZIP code: ") or None

        address = UpdateAddressInput(address=address, city=city, zip=zip)

        return UpdateUserInput(
            address=address,
            name=name,
            password=password,
        )
