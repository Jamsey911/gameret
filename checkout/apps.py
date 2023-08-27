from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """Import to pick up signals model"""
    name = 'checkout'

    def ready(self):
        import checkout.signals
