from pydantic import BaseModel

from kata_users_python.domain.common.vos import Id
from kata_users_python.domain.users.vos import Address, Email, Name, Password


class User(BaseModel):
    id: Id
    name: Name
    password: Password
    email: Email
    address: Address
