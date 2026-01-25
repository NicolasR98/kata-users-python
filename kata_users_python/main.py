import asyncio

from kata_users_python.presentation.users_cli_view import UserCLIView


async def main() -> None:
    view = UserCLIView()
    await view.init()


if __name__ == "__main__":
    asyncio.run(main())
