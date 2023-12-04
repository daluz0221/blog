from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    TemplateView
)
from django.views.generic.edit import FormView

from utils.functions import code_generator

from .forms import UserRegisterForm, Loginform, UpdatePasswordForm
from .models import User
# Create your views here.


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        code = code_generator()
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            genero=form.cleaned_data['genero'],
            coderegister=code
        )



        return super(UserRegisterView, self).form_valid(form)
    
class PanelView(LoginRequiredMixin,TemplateView):
    template_name = "users/panel.html"
    login_url = reverse_lazy('users_app:user-login')


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = Loginform
    success_url = reverse_lazy('users_app:user-panel')


    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)

        return super(LoginView, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )
    
class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = "users/update_password.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-panel')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1'],
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)

        return super(UpdatePasswordView, self).form_valid(form)