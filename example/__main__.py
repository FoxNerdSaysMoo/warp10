from warp10 import app
from .counter import Counter
from .chat import Chat

app.run("0.0.0.0", 443, dev=True)
