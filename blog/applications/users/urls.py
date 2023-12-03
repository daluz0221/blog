
from django.urls import path

from .views import UserRegisterView, PanelView

app_name = "users_app"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('panel/', PanelView.as_view(), name='user-panel'),
]
