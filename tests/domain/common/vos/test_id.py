import uuid

import pytest

from kata_users_python.domain.common.vos.id import Id


class TestId:
    @pytest.fixture
    def raw_id(self):
        return uuid.uuid4()

    def test_valid_arguments(self, raw_id):
        assert Id(raw_id)

    def test_no_arguments(self):
        assert Id()

    def test_equality_same(self, raw_id):
        assert Id(raw_id) == Id(raw_id)

    def test_equality_different(self):
        assert Id() != Id()
