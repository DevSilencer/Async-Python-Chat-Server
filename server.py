import asyncio
import time
import uuid

conn_id = {}
lock = asyncio.Lock()

def generate_id():
    timestamp = int(time.time() * 1000)
    uid = uuid.uuid4().int
    return (timestamp >> 32) | (uid & 0xffff)

def find_online_uid(writer, dic, uid):
    for k,v in dic.items():
        writer.write('Online Users In Chat Room: ')
        if k and k != uid:
            writer.write(f'{k} '.encode('utf-8'))
    writer.write('\n'.encode('utf-8'))

async def handle_client(reader, writer):
    client_id = generate_id()
    addr = writer.get_extra_info('peername')

    async with lock:
        conn_id[client_id] = {"writer": writer, "target_id": None}
        find_online_uid(writer, conn_id, client_id)


    print(f'Client {client_id} connected from {addr}')

    writer.write(f'Your id is {client_id}\n'.encode('utf-8'))
    await writer.drain()

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            msg = data.decode('utf-8').strip()
            print(f"Client {client_id} sent: {msg}")

            if ':' in msg:
                target_id_str, message = msg.split(':', 1)
                try:
                    target_id = int(target_id_str)
                except ValueError:
                    writer.write(b"Invalid target ID\n")
                    await writer.drain()
                    continue

                async with lock:
                    conn_id[client_id]["target_id"] = target_id_str

            else:
                async with lock:
                    target_id_str = conn_id[client_id]["target_id"]
                if not target_id_str:
                    writer.write(b"Invalid format. Use target_id:message\n")
                    await writer.drain()
                    continue
                message = msg.strip()
                target_id = int(target_id_str)

            async with lock:
                target_info = conn_id.get(target_id)

            if not target_info or target_info["writer"].is_closing():
                writer.write(f"Client {target_id} not found\n".encode('utf-8'))
                await writer.drain()
                continue

            target_writer = target_info["writer"]
            target_writer.write(f"From {client_id}: {message}\n".encode('utf-8'))
            await target_writer.drain()

    except asyncio.CancelledError:
        print(f"Client {client_id} task cancelled")
    finally:
        async with lock:
            if client_id in conn_id:
                del conn_id[client_id]

        writer.close()
        await writer.wait_closed()
        print(f"Client {client_id} disconnected")

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 8880)
    print("Server running on 0.0.0.0:8880")
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nServer stopped by user")