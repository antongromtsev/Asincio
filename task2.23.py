import asyncio
from util import async_timed
from util import delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 2
    for i in range(100000000):
        counter = counter + 1
    return counter


async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(delay(1, '1'))
    print(await task_one)
    await task_two


asyncio.run(main(), debug=True)
