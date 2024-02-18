import asyncio


async def fn():
    print("one")
    await asyncio.sleep(1)
    await ook()
    await ook()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)


async def ook():
    val: str = input("enter: ")
    print(val)


asyncio.run(fn())
