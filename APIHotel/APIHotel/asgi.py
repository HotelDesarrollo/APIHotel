"""
ASGI config for APIHotel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application
from apps.websocket.consumers import Consumer
from django.urls.conf import path
from .channelsmiddleware import JWTChannelMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APIHotel.settings')

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": JWTChannelMiddleware(
        URLRouter([
            path("ws/", Consumer.as_asgi()),
        ])
    )
})

# application = get_asgi_application()
