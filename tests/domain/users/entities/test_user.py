import pytest
from pydantic import ValidationError

from kata_users_python.domain.common.vos.id import Id
from kata_users_python.domain.users.entities.user import User
from kata_users_python.domain.users.vos.address import Address


class TestUser:
    @pytest.fixture
    def user_data(self):
        return {
            "id": Id(),
            "address": {"address": "addr", "city": "city", "zip": "123"},
            "email": "mail@mail.com",
            "name": "name",
            "password": "Example123",
        }

    def test_valid_arguments(self):
        user = User(
            address=Address(address="addr", city="city", zip="123"),
            email="mail@mail.com",
            name="name",
            password="Example123",
        )

        assert user.password

    def test_equality_different_ids(self, user_data):
        user_1 = User(**user_data)
        user_2 = User(**user_data)

        assert user_1.equals(user_2)

    def test_equality_same_different_ids(self, user_data):
        user_1 = User(**{**user_data, "id": Id()})
        user_2 = User(**user_data)

        assert user_1.equals(user_2) is False

    def test_no_args(self, user_data):
        with pytest.raises(ValidationError) as errors:
            User()

        for expected_error in ["name", "password", "email", "address"]:
            assert expected_error in str(errors.value)
