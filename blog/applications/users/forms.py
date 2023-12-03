from django import forms

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

