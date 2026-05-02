import asyncio
import websockets

async def play():
    uri = "wss://your-app.onrender.com/ws"
    async with websockets.connect(uri) as ws:
        while True:
            msg = await ws.recv()
            if msg == "SEND":
                num = input("Enter number: ")
                await ws.send(num)
            else:
                print("Result:", msg)
                break

asyncio.run(play())