from .protocol import Packet


class Pipeline:
    pipes: list = []
    
    def __init__(self, app):
        self.app = app
        self.clients = []
        self._started = False

    def _start(self):
        if not self._started:
            self._pipes = [pipe(self) for pipe in Pipeline.pipes]
            self._started = True
            print("[DEBUG] Pipes:", self.pipes)

    async def _event(self, name: str, client, *args):
        self._start()
        for pipe in self._pipes:
            print(pipe)
            try:
                await getattr(pipe, name)(client, *args)
            except AttributeError as e:
                print(f"WARN: {pipe} does not have a {name} method. {e}")

    async def on_connect(self, client):
        await self._event("on_connect", client)

    async def on_message(self, client, msg):
        print(msg)
        try:
            await self._event("on_message", client, msg)
            print("SENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return True
        except Exception as e:
            print(e)
            return False

    async def connect(self, client):
        self._start()
        self.clients.append(client)
        await self.on_connect(client)

class Pipe:
    app = None
    
    def __init__(self, *args):
        ...

    async def on_connect(self, client) -> None:
        ...
        
    async def on_message(self, client, msg) -> None:
        ...

    async def broadcast(self, clients, packet):
        for client in clients:
            await client.send(packet)
