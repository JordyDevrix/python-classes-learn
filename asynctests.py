import asyncio
import time


async def fn():
    new_task = asyncio.create_task(ook())
    print('1')
    await asyncio.sleep(1)
    time.sleep(1)
    print('3')
    await asyncio.sleep(1)


async def ook():
    time.sleep(1)
    print('2')
    await asyncio.sleep(1)
    time.sleep(1)
    print('4')
    time.sleep(1)

asyncio.run(fn())
