from kata_users_python.domain.common.entities import Entity
from kata_users_python.domain.users.vos import Address, Email, Name, Password


class User(Entity):
    name: Name
    password: Password
    email: Email
    address: Address
