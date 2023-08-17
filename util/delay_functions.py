import asyncio
from util.async_timed import async_timed


@async_timed()
async def delay(delay_second: int, name: str) -> int:
    print(f'{name}: засыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'{name}: сон в течение {delay_second} c закончился')
    return delay_second
