from sanic import Sanic, response, Websocket
from .pipeline import Pipeline
from .client import Client
from websockets.connection import CLOSED


app = Sanic("warp10")
pipeline = Pipeline(app)

app.static("/", "public")

@app.route("/")
async def index(req):
    return response.html(open("public/index.html").read())

@app.websocket("/ssr")
async def ssr(req, ws: Websocket):
    client = Client(ws, pipeline)
    try:
        await pipeline.connect(client)
        print("Finished startup")
        while client.alive:
            msg = await ws.recv()
            if not msg:
                print("Message not found")
                #break
            await pipeline.on_message(client, msg)
    except Exception as e:
        print("[DEBUG]", e)
    finally:
        print("Closed websocket")

