from abc import ABC, abstractmethod

from kata_users_python.domain.users.entities import User
from kata_users_python.domain.users.use_cases.create_user_use_case import (
    CreateUserInput,
)
from kata_users_python.domain.users.use_cases.update_user_use_case import (
    UpdateUserInput,
)


class UsersView(ABC):
    @abstractmethod
    def show_message(self, message: str) -> None:
        pass

    @abstractmethod
    def show_hello_message(self) -> None:
        pass

    @abstractmethod
    def show_exit_message(self) -> None:
        pass

    @abstractmethod
    def show_error(self, message: str, error_type: str | None = None) -> None:
        pass

    @abstractmethod
    def start_loading(self) -> None:
        pass

    @abstractmethod
    def stop_loading(self) -> None:
        pass

    @abstractmethod
    def show_main_options(self) -> None:
        pass

    # User actions
    @abstractmethod
    def render_users(self, users: list[User]) -> None:
        pass

    @abstractmethod
    def render_user(self, user: User) -> None:
        pass

    @abstractmethod
    def ask_create_user_input(self) -> CreateUserInput:
        pass

    @abstractmethod
    def ask_update_user_input(self) -> UpdateUserInput:
        pass

    @abstractmethod
    def ask_input(self) -> str:
        pass
