import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(1)
result = asyncio.run(coroutine_add_one(1))
print(f'Результат функции равен {function_result},',
      'а его тип равен {type(function_result)}')
print(f'Результат сопрограммы равен {result},',
      'а его тип равен {type(coroutine_result)}')
