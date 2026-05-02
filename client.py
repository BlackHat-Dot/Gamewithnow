import asyncio
import websockets

async def play():
    uri = "ws://0.tcp.ngrok.io:XXXXX"   # ngrok endpoint

    async with websockets.connect(uri) as ws:
        server_num = await ws.recv()    # first receive

        num = input("Enter number: ")
        await ws.send(num)              # then send

        result = await ws.recv()        # final result
        print("Result:", result)

asyncio.run(play())
asyncio.run(play())
asyncio.run(play())
hfhdfhjmgjg
