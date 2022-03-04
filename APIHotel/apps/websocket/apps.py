from django.apps import AppConfig


class WebsocketConfig(AppConfig):
    name = 'apps.websocket'
    
    def ready(self):
        from .signals import alojamientos_signals
        from .signals import habitacion_signals
        from .signals import usuarios_signals
        
        
