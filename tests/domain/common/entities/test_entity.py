from kata_users_python.domain.common.entities import Entity
from kata_users_python.domain.common.vos import Id


class SubClass(Entity):
    value: str = "hello world"


class TestEntityClass:
    def test_valid_arguments(self):
        assert Entity(id=Id())

    def test_no_arguments(self):
        assert Entity()

    def test_subclass(self):
        result = SubClass()

        assert isinstance(result, Entity)
        assert result.id


class TestEquals:
    def test_same_id(self):
        mock_id = Id()

        entity_1 = SubClass(id=mock_id, value="hello")
        entity_2 = SubClass(id=mock_id, value="world")

        assert entity_1.equals(entity_2)

    def test_different_id(self):
        entity_1 = SubClass()
        entity_2 = SubClass()

        assert not entity_1.equals(entity_2)

    def test_self(self):
        entity_1 = SubClass()
        assert entity_1.equals(entity_1)

    def test_different_class(self):
        class Foo: ...

        entity_1 = SubClass()
        entity_2 = Foo()

        assert not entity_1.equals(entity_2)

    def test_none(self):
        entity_1 = SubClass()

        assert not entity_1.equals(None)
        assert not entity_1.equals()
