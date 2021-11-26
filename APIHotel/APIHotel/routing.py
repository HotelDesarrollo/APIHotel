
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls.conf import path
from .channelsmiddleware import JWTChannelMiddleware
from apps.websocket.consumers import Consumer

application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        "websocket": JWTChannelMiddleware(
            URLRouter([
                path("ws/", Consumer.as_asgi()),
            ])
        )
    }
)
