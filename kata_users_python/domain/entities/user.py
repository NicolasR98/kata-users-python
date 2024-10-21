from pydantic import BaseModel

from kata_users_python.domain.value_objects.address import Address
from kata_users_python.domain.value_objects.email import Email
from kata_users_python.domain.value_objects.id import Id
from kata_users_python.domain.value_objects.name import Name
from kata_users_python.domain.value_objects.password import Password


class User(BaseModel):
    id: Id
    name: Name
    password: Password
    email: Email
    address: Address
