from warp10 import app
from sanic import response

# Pipes
from .counter import Counter
from .chat import Chat

app.static("/", "example/public")

@app.route("/")
async def index(req):
    return response.html(open("example/public/index.html").read())


app.run("0.0.0.0", 443, dev=True)
