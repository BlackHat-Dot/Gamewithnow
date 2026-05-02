from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

waiting = None
lock = asyncio.Lock()

@app.websocket("/ws")
async def ws(ws: WebSocket):
    await ws.accept()

    global waiting

    async with lock:
        if waiting is None:
            waiting = ws
            await ws.send_text("WAIT")
            return
        else:
            opponent = waiting
            waiting = None

    # both players ready
    try:
        await ws.send_text("SEND")
        await opponent.send_text("SEND")

        n1 = int(await ws.receive_text())
        n2 = int(await opponent.receive_text())

        total = n1 + n2
        result = "EVEN" if total % 2 == 0 else "ODD"

        await ws.send_text(result)
        await opponent.send_text(result)

    except:
        pass

    finally:
        await ws.close()
        await opponent.close()