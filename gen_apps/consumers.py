import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        change_variable = data['change_variable']
        change_variable1 = data['change_variable1']
        # change_variable2 = data['change_variable2']
        # change_variable3 = data['change_variable3']
        
        username = data['username']
        room = data['room']
        

        await self.save_message(username, room, change_variable,change_variable1)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'change_variable': change_variable,
                'change_variable1': change_variable1,
                # 'change_variable2': change_variable2,
                # 'change_variable3': change_variable3,

                'username': username
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        change_variable = event['change_variable']
        change_variable1 = event['change_variable1']
        # change_variable2 = event['change_variable2']
        # change_variable3 = event['change_variable3']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'username': username,
            'change_variable': change_variable,
            'change_variable1': change_variable1
            # 'change_variable2': change_variable2,
            # 'change_variable3': change_variable3

        }))

    @sync_to_async
    def save_message(self, username, room, change_variable,change_variable1):
        
        # Message.objects.create(username=username, room=room, change_variable=change_variable,change_variable1=change_variable1,change_variable2=change_variable2,change_variable3=change_variable3)
        if Message.objects.filter(room =room).exists:
            room = Message(room=room)
            t= Message.objects.get(room=room)
            t.username = username
            t.change_variable = change_variable
            t.change_variable1 = change_variable1
            t.save()

        
            # t=Message.objects.filter(change_variable=change_variable,change_variable1=change_variable1 ).exists()
            # Message.objects.update(change_variable=change_variable,change_variable1=change_variable1)
            # print("update")
            

           
        else:
            Message.objects.create(username=username, room=room, change_variable=change_variable,change_variable1=change_variable1)
    

    


        
        
    
    
    


        
       
        
