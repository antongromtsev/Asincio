import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(3, '1'))
    try:
        result = await asyncio.wait_for(delay_task, timeout=4)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')
asyncio.run(main())
