from warp10 import app
from .counter import Counter

app.run("0.0.0.0", 443, dev=True)
