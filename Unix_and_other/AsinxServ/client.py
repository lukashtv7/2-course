#!/bin/bash

import asyncio


HOST = 'localhost'
PORT = 9095


async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    message = 'Hello, world'

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    writer.close()
    print (data)
    await writer.wait_closed()

asyncio.run(tcp_echo_client(HOST, PORT))

#loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
task = loop.create_task(tcp_echo_client(HOST, PORT))
loop.run_until_complete(task)
