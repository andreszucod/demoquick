from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label=('Escriba la contraseña'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Ingrese su Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label=('Repita la contraseña'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder' : 'Repita la Contraseña'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'email',
        )
        label = {
            'email' : 'Email',
        }
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese Correo Electronico'}),
        }

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'La contraseña deben ser igual')
            

class LoginUserForm(forms.Form):
    email = forms.CharField(
        label=('Ingrese su email'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Ingrese Email'
            }
        )
    )

    password = forms.CharField(
        label=('Escriba su contraseña'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Ingrese Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginUserForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            # Corta el proceso de validacion si los datos no son correctos
            raise forms.ValidationError('Loa Datos de Login no son Correctos')
        return self.cleaned_data