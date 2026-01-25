from abc import ABC, abstractmethod

from kata_users_python.domain.users.entities import User


class UsersView(ABC):
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
    def list_users(self, users: list[User]) -> None:
        pass

    # @abstractmethod
    def create_user(self, user: User) -> None:
        pass
