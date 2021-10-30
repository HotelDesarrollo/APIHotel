from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from apps.mymid.authmid import UniversalAuthMiddlewareStack
from apps.websocket.consumers import Consumer

application = ProtocolTypeRouter({
    "websocket": UniversalAuthMiddlewareStack(
        URLRouter([
            path("ws/", Consumer),
        ]),
    ),
})
