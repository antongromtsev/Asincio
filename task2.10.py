import asyncio

from util import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код!")


async def main():
    firts_delay = asyncio.create_task(delay(2, '1'))
    second_delay = asyncio.create_task(delay(2, '2'))
    await hello_every_second()
    await firts_delay
    await second_delay

asyncio.run(main())
