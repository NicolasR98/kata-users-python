import asyncio

from kata_users_python.composition_root import CompositionRoot
from kata_users_python.presentation.users_cli_view import UserCLIView


async def main() -> None:
    view = UserCLIView()
    composition_root = CompositionRoot()
    presenter = composition_root.provide_presenter(view=view)

    await presenter.start()


if __name__ == "__main__":
    asyncio.run(main())
