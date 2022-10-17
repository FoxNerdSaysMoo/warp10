from .pipeline import Pipe, Pipeline


class Element(Pipe):
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline
        if not hasattr(self.__class__, "packet"):
            raise Exception("Element must have packet attribute!")
        self.packet = self.__class__.packet
        self.tag = self.packet.tag
        self.fmt = self.packet.value
        if not hasattr(self.__class__, "default_val"):
            raise Exception("You didn't look at the example/docs. You must provide a default value!")
        self.value = self.__class__.default_val

    async def on_connect(self, client):
        await client.send(self.packet(self.value))

    async def set(self, newval):
        self.value = newval  # TODO: Make a smart diff
        await self.broadcast(self.pipeline.clients, self.packet(self.value))

