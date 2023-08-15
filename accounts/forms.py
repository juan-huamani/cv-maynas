from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users
from django.contrib.auth.password_validation import  CommonPasswordValidator


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('email', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password1'].validators = [self.custom_password_validator]

    # def custom_password_validator(self, password):
    #     errors = []
    #     if len(password) < 8:
    #         errors.append("La contraseña es demasiado corta. Debe contener al menos 8 caracteres.")
    #     if CommonPasswordValidator().validate(password):
    #         errors.append("La contraseña es demasiado común.")

    #     if errors:
    #         raise forms.ValidationError(errors)

    #     return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not ('@' in email and '.' in email):
            raise forms.ValidationError('El correo electrónico debe contener "@" y ".".')
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico')
    