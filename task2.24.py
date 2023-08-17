import asyncio
from util import delay, async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 2
    for i in range(2000000):
        counter = counter + 1
    return counter


@async_timed()
async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(delay(1, '1'))
    print(await task_one)
    await delay(1, '2')
    await task_two

asyncio.run(main(), debug=True)
