import asyncio

from kata_users_python.composition_root import CompositionRoot


async def main() -> None:
    composition_root = CompositionRoot()
    presenter = composition_root.provide_presenter()

    await presenter.start()


if __name__ == "__main__":
    asyncio.run(main())
