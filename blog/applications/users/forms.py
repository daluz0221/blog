from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )



    class Meta:
        model = User
        fields = ('username', 'email', 'nombre', 'apellido', 'genero')


    def clean_password1(self):
        password1 = self.cleaned_data['password1']

        if len(password1) < 5:
            self.add_error('password1', 'La contraseña debe tener mas de 5 caracteres')

        return password1
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('El nombre de usuario ya esta en uso')

        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()

        if email_taken:
            raise forms.ValidationError('El email ya esta en uso')

        return email


class Loginform(forms.Form):

    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'style': '{margin: 10px;}',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )


    def clean(self):
        cleaned_data = super(Loginform, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos ingresados no son correctos')
        
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )

    password3 = forms.CharField(
        label='Repetir Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña Nueva'
            }
        )
    )
    
    def clean_password3(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password3']:
            self.add_error('password2', 'Las contraseñas no son iguales')

        return self.cleaned_data['password3']