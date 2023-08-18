import asyncio
import socket
import signal
import logging
import os
import time

from typing import Set
from asyncio import AbstractEventLoop

from util import delay


def cancel_tasks(x, y):
    print('Получен сигнал SIGINT!')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Снимается {len(tasks)} задач.')
    [task.cancel() for task in tasks]


async def echo(connection: socket,
               loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b'boon':
                raise Exception("Неожиданная ошибка сети")
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {address}")
        await asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    signal.signal(signal.SIGINT, cancel_tasks)
    await listen_for_connection(server_socket, asyncio.get_event_loop())
    # while True:
    #     print(f'Run.. {os.getpid()}')
    #     time.sleep(5)
    #     os.kill(os.getpid(), signal.SIGINT)

asyncio.run(main())
