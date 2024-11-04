import pytest
from pydantic import ValidationError

from kata_users_python.domain.common.vos.id import Id
from kata_users_python.domain.users.entities import User
from tests.conftest import UserMother


class TestUser:
    def test_valid_arguments(self, user_mother: UserMother):
        assert user_mother.build()

    def test_different_entities_and_ids(self, user_mother: UserMother):
        user_1, user_2 = user_mother.batch(2)

        assert user_1.equals(user_2) is False

    def test_different_entities_and_same_ids(self, user_mother: UserMother):
        user_1, user_2 = user_mother.batch(2, id=Id())

        assert user_1.equals(user_2)

    def test_same_entities_and_different_ids(self, user_mother: UserMother):
        user_1 = user_mother.build()
        user_2 = User(**user_1.model_dump(exclude=("id")), id=Id())

        assert user_1.equals(user_2) is False

    def test_same_entities_and_same_ids(self, user_mother: UserMother):
        user_1, user_2 = user_mother.batch(2, id=Id())

        assert user_1.equals(user_2)

    def test_no_args(self):
        with pytest.raises(ValidationError) as errors:
            User()

        for expected_error in ["name", "password", "email", "address"]:
            assert expected_error in str(errors.value)
