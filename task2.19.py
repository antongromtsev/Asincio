import asyncio
from util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        await asyncio.sleep(0.00000000001)
        counter = counter + 1
        return counter


@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4, '1'))
    await delay_task
    await task_one
    await task_two


asyncio.run(main())
