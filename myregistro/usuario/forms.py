from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Persona
from django.forms import ModelForm

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields =['cc','nombres','apellidos','foto','user']
        #help_text ={k:""for k in fields}

# class RegistroForm(UserCreationForm):
    
#     correo=forms.EmailField()
#     clave1=forms.CharField(label='contraseña',widget=forms.PasswordInput)
#     clave2=forms.CharField(label='contraseña',widget=forms.PasswordInput)

#     class Meta:
#         model =User
#         fields = ['correo','clave1','clave2']
#         help_text = {k:""for k in fields}

# class UserRegisterForm(ModelForm):
#     email = forms.EmailField()
#     #nombre=forms.Textarea()
#     password1=forms.CharField(label='contraseña',widget=forms.PasswordInput)
#     password2=forms.CharField(label='confirmar',widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username','email', 'password1', 'password2']
#         help_texts={k:"" for k in fields}