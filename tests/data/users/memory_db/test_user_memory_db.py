import pytest

from kata_users_python.data import MemoryUserRepository
from kata_users_python.domain.common.vos import Id
from kata_users_python.domain.users.entities.user import User
from kata_users_python.domain.users.vos import Email
from tests.factories.models import UserMother


class TestMemoryUserRepository:
    @pytest.fixture
    def empty_repository(self) -> MemoryUserRepository:
        return MemoryUserRepository({})

    @pytest.fixture
    def populated_repository(
        self, user_mother: UserMother
    ) -> tuple[MemoryUserRepository, list[User]]:
        users = user_mother.batch(3)
        data = {user.id: user for user in users}

        return MemoryUserRepository(data), users

    def test_init_with_empty_data(self):
        repository = MemoryUserRepository({})

        assert repository._data == {}

    def test_init_with_none_data(self):
        repository = MemoryUserRepository(None)

        assert repository._data == {}

    def test_init_with_data(self, user_mother: UserMother):
        users = user_mother.batch(2)
        data = {user.id: user for user in users}
        repository = MemoryUserRepository(data)

        assert repository._data == data

    @pytest.mark.asyncio
    async def test_get_list_empty_repository(
        self, empty_repository: MemoryUserRepository
    ):
        result = await empty_repository.get_list()

        assert result == []

    @pytest.mark.asyncio
    async def test_get_list_populated_repository(
        self, populated_repository: tuple[MemoryUserRepository, list[User]]
    ):
        repository, users = populated_repository
        result = await repository.get_list()

        assert len(result) == 3
        assert all(user in result for user in users)

    @pytest.mark.asyncio
    async def test_get_by_id_existing_user(
        self, populated_repository: tuple[MemoryUserRepository, list[User]]
    ):
        repository, users = populated_repository
        user = users[0]
        result = await repository.get_by_id(user.id)

        assert result == user

    @pytest.mark.asyncio
    async def test_get_by_id_nonexistent_user(
        self, empty_repository: MemoryUserRepository
    ):
        result = await empty_repository.get_by_id(Id())

        assert result is None

    @pytest.mark.asyncio
    async def test_get_by_email_existing_user(
        self, populated_repository: tuple[MemoryUserRepository, list[User]]
    ):
        repository, users = populated_repository
        user = users[0]
        result = await repository.get_by_email(user.email)

        assert result == user

    @pytest.mark.asyncio
    async def test_get_by_email_nonexistent_user(
        self, empty_repository: MemoryUserRepository
    ):
        result = await empty_repository.get_by_email(Email("nonexistent@example.com"))

        assert result is None

    @pytest.mark.asyncio
    async def test_get_by_email_domain_matching_users(self, user_mother: UserMother):
        user1 = user_mother.build(email=Email("alice@company.com"))
        user2 = user_mother.build(email=Email("bob@company.org"))
        user3 = user_mother.build(email=Email("charlie@different.com"))

        data = {user.id: user for user in [user1, user2, user3]}
        repository = MemoryUserRepository(data)

        result = await repository.get_by_email_domain(Email("test@company.net"))

        assert len(result) == 2
        assert user1 in result
        assert user2 in result
        assert user3 not in result

    @pytest.mark.asyncio
    async def test_get_by_email_domain_no_matches(
        self, populated_repository: tuple[MemoryUserRepository, list[User]]
    ):
        repository, _ = populated_repository
        result = await repository.get_by_email_domain(Email("test@nonexistent.com"))

        assert result == []

    @pytest.mark.asyncio
    async def test_create_new_user(
        self, empty_repository: MemoryUserRepository, user_mother: UserMother
    ):
        user = user_mother.build()

        await empty_repository.create(user)

        assert empty_repository._data[user.id] == user

    @pytest.mark.asyncio
    async def test_create_overwrites_existing_user(self, user_mother: UserMother):
        user1 = user_mother.build()
        user2 = user_mother.build(id=user1.id)
        repository = MemoryUserRepository({user1.id: user1})

        await repository.create(user2)

        assert repository._data[user1.id] == user2

    @pytest.mark.asyncio
    async def test_update_existing_user(
        self,
        populated_repository: tuple[MemoryUserRepository, list[User]],
        user_mother: UserMother,
    ):
        repository, users = populated_repository
        existing_user = users[0]
        updated_user = user_mother.build(id=existing_user.id)

        await repository.update(updated_user)

        assert repository._data[existing_user.id] == updated_user

    @pytest.mark.asyncio
    async def test_update_nonexistent_user(
        self, empty_repository: MemoryUserRepository, user_mother: UserMother
    ):
        user = user_mother.build()
        await empty_repository.update(user)

        assert user.id not in empty_repository._data

    @pytest.mark.asyncio
    async def test_delete_existing_user(
        self, populated_repository: tuple[MemoryUserRepository, list[User]]
    ):
        repository, users = populated_repository
        user_to_delete = users[0]

        await repository.delete(user_to_delete.id)

        assert user_to_delete.id not in repository._data
        assert len(repository._data) == 2

    @pytest.mark.asyncio
    async def test_delete_nonexistent_user(
        self, populated_repository: tuple[MemoryUserRepository, list[User]]
    ):
        repository, users = populated_repository
        original_count = len(repository._data)

        await repository.delete(Id())

        assert len(repository._data) == original_count
