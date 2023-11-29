import asyncio
import websockets

connected_clients = []

async def handle_connection(websocket, path):
   
    connected_clients.append(websocket)
    try:
        print("Novo cliente conectado!")
        while True:
            
            message = await websocket.recv()
            print("MENSAGEM RECEBIDA:")
            print(message)

            
            for client in connected_clients:
                await client.send(message)
    finally:
        
        connected_clients.remove(websocket)

async def main():
    print("INICIANDO SERVIDOR WEBSOCKET...\n")
    start_server = await websockets.serve(handle_connection, 'localhost', 8000)

    #
    await start_server.wait_closed()

if __name__ == "__main__":
    
    asyncio.run(main())
