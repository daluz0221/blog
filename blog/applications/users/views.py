from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    CreateView
)
from django.views.generic.edit import FormView

from .forms import UserRegisterForm
from .models import User
# Create your views here.


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            genero=form.cleaned_data['genero'],
        )

        return super(UserRegisterView, self).form_valid(form)
    
class PanelView(TemplateView):
    template_name = "users/panel.html"