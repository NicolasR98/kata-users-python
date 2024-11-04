from polyfactory.pytest_plugin import register_fixture

from tests.factories.models import UserMother

user_mother = register_fixture(UserMother)
