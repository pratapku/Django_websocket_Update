import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import gen_apps.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatty.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            gen_apps.routing.websocket_urlpatterns
        )
    )
})