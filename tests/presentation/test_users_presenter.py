from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

from kata_users_python.presentation.users.users_view import UsersView


@pytest.fixture
def view():
    v = MagicMock(spec=UsersView)
    v.show_main_options.return_value = "0"
    return v


@pytest.mark.asyncio
async def test_handle_display_users_renders_list(view):
    from kata_users_python.presentation.users.users_presenter import UsersPresenter

    users = [SimpleNamespace(id=1, email="a@b"), SimpleNamespace(id=2, email="c@d")]
    list_uc = AsyncMock(return_value=users)
    presenter = UsersPresenter(
        view=view,
        list_users_use_case=list_uc,
        create_user_use_case=AsyncMock(),
        update_user_use_case=AsyncMock(),
        delete_user_by_email_use_case=AsyncMock(),
        get_user_by_email_use_case=AsyncMock(),
    )

    await presenter.handle_display_users()

    view.render_users.assert_called_once_with(users=users)


@pytest.mark.asyncio
async def test_handle_display_user_renders_user(view):
    from kata_users_python.presentation.users.users_presenter import UsersPresenter

    email = "a@b"
    view.ask_input.return_value = email
    user = SimpleNamespace(id=1, email=email)
    get_uc = AsyncMock(return_value=user)
    presenter = UsersPresenter(
        view=view,
        list_users_use_case=AsyncMock(return_value=[]),
        create_user_use_case=AsyncMock(),
        update_user_use_case=AsyncMock(),
        delete_user_by_email_use_case=AsyncMock(),
        get_user_by_email_use_case=get_uc,
    )

    await presenter.handle_display_user()

    view.render_user.assert_called_once_with(user=user)


@pytest.mark.asyncio
async def test_handle_create_user_renders_created_user(view):
    from kata_users_python.presentation.users.users_presenter import UsersPresenter

    created = SimpleNamespace(id=10, email="new@user")
    view.ask_create_user_input.return_value = {}
    create_uc = AsyncMock(return_value=created)
    presenter = UsersPresenter(
        view=view,
        list_users_use_case=AsyncMock(return_value=[]),
        create_user_use_case=create_uc,
        update_user_use_case=AsyncMock(),
        delete_user_by_email_use_case=AsyncMock(),
        get_user_by_email_use_case=AsyncMock(),
    )

    await presenter.handle_create_user()

    view.render_user.assert_called_once_with(user=created)


@pytest.mark.asyncio
async def test_handle_update_user_renders_updated_user(view):
    from kata_users_python.presentation.users.users_presenter import UsersPresenter

    email = "exists@user"
    view.ask_input.return_value = email
    existing = SimpleNamespace(id=5, email=email)
    updated = SimpleNamespace(id=5, email=email)
    view.ask_update_user_input.return_value = {}
    get_uc = AsyncMock(return_value=existing)
    update_uc = AsyncMock(return_value=updated)
    presenter = UsersPresenter(
        view=view,
        list_users_use_case=AsyncMock(return_value=[]),
        create_user_use_case=AsyncMock(),
        update_user_use_case=update_uc,
        delete_user_by_email_use_case=AsyncMock(),
        get_user_by_email_use_case=get_uc,
    )

    await presenter.handle_update_user()

    view.render_user.assert_called_once_with(user=updated)


@pytest.mark.asyncio
async def test_handle_delete_user_shows_message(view):
    from kata_users_python.presentation.users.users_presenter import UsersPresenter

    email = "del@user"
    view.ask_input.return_value = email
    delete_uc = AsyncMock(return_value=None)
    presenter = UsersPresenter(
        view=view,
        list_users_use_case=AsyncMock(return_value=[]),
        create_user_use_case=AsyncMock(),
        update_user_use_case=AsyncMock(),
        delete_user_by_email_use_case=delete_uc,
        get_user_by_email_use_case=AsyncMock(),
    )

    await presenter.handle_delete_user()

    view.show_message.assert_called_with(f"User {email} successfully deleted")
