
from django.urls import path

from .views import UserRegisterView, PanelView, LoginView, LogoutView, UpdatePasswordView

app_name = "users_app"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('panel/', PanelView.as_view(), name='user-panel'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('update-password/', UpdatePasswordView.as_view(), name='user-update-password'),
]
