import asyncio
import time

from util import delay


async def main():
    t1 = time.perf_counter()
    sleep_1 = asyncio.create_task(delay(3, '1'))
    sleep_2 = asyncio.create_task(delay(3, '2'))
    sleep_3 = asyncio.create_task(delay(3, '3'))

    t2 = time.perf_counter()
    print(type(sleep_1))
    print(type(sleep_2))
    print(type(sleep_3))
    result_1 = await sleep_1
    t3 = time.perf_counter()
    result_2 = await sleep_2
    t4 = time.perf_counter()
    result_3 = await sleep_2
    t5 = time.perf_counter()
    print(result_1, result_2, result_3)
    print(t2-t1, t3-t1, t4-t1, t5-t1)

asyncio.run(main())
