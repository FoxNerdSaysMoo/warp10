from warp10 import Element, Pipeline, CustomPacket
from .utils import random_name


class Chat(Element):
    packet = CustomPacket.from_toml("example/packets.toml", "chat")
    default_val = ["Start of chat."]

    async def saturate(self, client):
        """For (future) SSR."""
        return "Welcome to the chat."

    async def on_message(self, client, msg):
        if not msg.startswith("chat:"):
            return
        message = client.ctx["chatname"] + ": " + msg[5:]
        await self.send_message(message)

    async def send_message(self, message):
        if len(self.value) > 100:
            self.value = self.value[:-1]
        await self.set(self.value + [message])

    async def on_connect(self, client):
        await super().on_connect(client)  # Sends current chat
        client.ctx["chatname"] = random_name()
        await self.send_message(client.ctx["chatname"] + " has joined.")

Pipeline.pipes.append(Chat)

