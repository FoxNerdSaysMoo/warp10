from dataclasses import dataclass

from sanic.server.websockets.impl import WebsocketImplProtocol

from .pipeline import Pipeline


@dataclass
class Client:
    ws: WebsocketImplProtocol
    pipeline: Pipeline
    alive: bool = True

    async def shutdown(self):
        await self.ws.close()

    async def send(self, packet):
        try:
            await self.ws.send(str(packet))
        except:
            self.alive = False
