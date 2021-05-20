#!/bin/bash
import asyncio

HOST = 'localhost'
PORT = 9095


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    #print (data)
    res = bytes("mama, just killed  a man", 'utf-8')
    print (res)

    res = bytes(message+" nice message, nibba", 'utf-8')
    
    writer.write(res)
    await writer.drain()

    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, HOST, PORT, loop=loop)
server = loop.run_until_complete(coro)

# Обрабатываем запросы пока прграмма не будет завершена по Ctrl+C
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Закрываем сервер
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
