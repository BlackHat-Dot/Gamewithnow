import asyncio
import websockets

async def handler(ws):
    print("Client connected")

    server_num = input("Enter your number: ")
    await ws.send(server_num)          # send first

    client_num = await ws.recv()       # receive second

    total = int(server_num) + int(client_num)

    if total % 2 == 0:
        await ws.send("EVEN")
    else:
        await ws.send("ODD")

    await asyncio.sleep(1)  # prevent instant close

async def main():
    async with websockets.serve(handler, "0.0.0.0", 5000):
        print("Server running...")
        await asyncio.Future()  # keep alive

asyncio.run(main())