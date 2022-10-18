from sanic import Sanic, Websocket
from .pipeline import Pipeline
from .client import Client


app = Sanic("warp10")
pipeline = Pipeline(app)

@app.websocket("/ssr")
async def ssr(req, ws: Websocket):
    client = Client(ws, pipeline)
    client.ctx = {}
    try:
        await pipeline.connect(client)
        print("Finished startup")
        while client.alive:
            msg = await ws.recv()
            if not msg:
                print("Message not found")
            await pipeline.on_message(client, msg)
    except Exception as e:
        print("[DEBUG]", e)
    finally:
        await pipeline.on_disconnect(client)
        print("Closed websocket")

