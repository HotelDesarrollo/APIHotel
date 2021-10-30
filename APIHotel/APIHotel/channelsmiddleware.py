from django.urls import re_path
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from APIHotel.apps.websocket.consumers import Consumer

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"^front(end)/$", Consumer.AsyncChatConsumer.as_asgi()),
        ])
    ),
})
