from kata_users_python.domain.users.entities.user import User
from kata_users_python.domain.users.vos.address import Address


class TestUser:
    def test_valid_arguments(self):
        user = User(
            address=Address(address="addr", city="city", zip="123"),
            email="mail@mail.com",
            name="name",
            password="ABC12345678@",
        )

        assert user
