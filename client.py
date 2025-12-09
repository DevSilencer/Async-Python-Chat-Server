import asyncio
import aioconsole

async def client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8880)

    async def read_message():
        while True:
            data = await reader.read(1024)
            if not data:
                break
            print(data.decode())

    async def send_message():
        while True:
            msg = await aioconsole.ainput('')
            writer.write(msg.encode())
            await writer.drain()

    try:
        await asyncio.gather(read_message(), send_message())
    except asyncio.CancelledError:
        print('You Left The Chat')
    finally:
        writer.close()

asyncio.run(client())







