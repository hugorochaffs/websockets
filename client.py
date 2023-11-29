import asyncio
import websockets

async def connect_to_server():
    async with websockets.connect('ws://localhost:8000') as websocket:
        while True:
            #
            message = input("DIGITE SUA MENSAGEM: ")

            await websocket.send(message)

            response = await websocket.recv()

            print("MENSAGEM RECEBIDA:", response)


async def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        await connect_to_server()
    finally:
        loop.close()

if __name__ == "__main__":
    asyncio.run(main())
