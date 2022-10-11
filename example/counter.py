from warp10 import Pipe, Packet, Pipeline, load_packet_from_toml

ButtonCounter = load_packet_from_toml("example/packets.toml", "buttoncounter")

VisitCounter = load_packet_from_toml("example/packets.toml", "visitcounter")

class Counter(Pipe):

    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.clients = pipeline.clients
        self.counter = 0
        self.visits = 0

    async def on_connect(self, client):
        self.visits += 1
        await client.send(ButtonCounter(self.counter))
        await self.broadcast(self.clients, VisitCounter(self.visits))

    async def on_message(self, client, msg):
        if msg != "inc_counter":
            return
        self.counter += 1
        await client.send(ButtonCounter(self.counter))
        await self.broadcast(self.clients, ButtonCounter(self.counter))

    def __repr__(self):
        return f"<Counter counter={self.counter} visits={self.visits}>"

Pipeline.pipes.append(Counter)
