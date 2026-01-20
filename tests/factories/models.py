from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory

from kata_users_python.domain.users.entities import User


class UserMother(ModelFactory[User]):
    __faker__ = Faker()

    @classmethod
    def password(cls) -> str:
        return cls.__faker__.password(
            length=12, special_chars=False, upper_case=True, lower_case=True
        )
