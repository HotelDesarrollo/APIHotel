from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls.conf import path
import APIHotel.routing
from .channelsmiddleware import TokenAuthMiddleware
from apps.websocket.consumers import FooConsumer

application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        "websocket": TokenAuthMiddleware(
            URLRouter([
                path("ws/", FooConsumer),
            ])
        )
    }
)
