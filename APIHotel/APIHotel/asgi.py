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
from APIHotel.apps.websocket.consumers import Consumer
import APIHotel.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APIHotel.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            APIHotel.routing.websocket_urlpatterns = [
              url("websocket/"), Consumer
            ]
        )
    ),
})

# application = get_asgi_application()
