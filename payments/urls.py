from django.urls import path

from .views import create_checkout_session, webhook
from django.views.decorators.csrf import csrf_exempt
  
urlpatterns = [
    path("checkout/", csrf_exempt(create_checkout_session)),
    path("webhook/", webhook, name="webhook"),
]
