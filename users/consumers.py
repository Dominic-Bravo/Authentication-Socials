# users/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'You are now connected to WebSockets!'
        }))
        
# users/consumers.py

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the connection
        await self.accept()
        
        # Add the user to a "group" (so we can broadcast to many people)
        await self.channel_layer.group_add("global_notifications", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("global_notifications", self.channel_name)

    # Receive message from WebSocket (from the user)
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        # Send message to the group
        await self.channel_layer.group_send(
            "global_notifications",
            {
                "type": "chat_message",
                "message": message
            }
        )

    # Handler for the 'chat_message' type sent above
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))