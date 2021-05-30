from django.test import TestCase
from channels.testing import HttpCommunicator

from .consumers import ChatConsumer


class MyTests(TestCase):

    async def test_my_consumer(self):
        communicator = HttpCommunicator(ChatConsumer.as_asgi(), path='/test/',
                                        method="GET")

        await communicator.send_input({
            'type': 'chat_message',
            'message': 'test'
        })
        value = await communicator.receive_output()
        print(value)
        self.assertEqual(value.get('text'),
                         '{"message": "test", "date": "2021-04-07"}')
