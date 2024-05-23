from django import forms
from django.core.exceptions import ValidationError

class RegistroForm(forms.Form):
    nombre_apellido = forms.CharField(
        label="Nombre", 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Nombre y Apellido'})
    )
    email = forms.EmailField(
        label="Dirección de correo electrónico", 
        required=True
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Al menos 6 caracteres'})
    )
    confirm_password = forms.CharField(
        label="Confirma tu contraseña",
        required=True,
        widget=forms.PasswordInput()
    )

    def clean_nombre_apellido(self):
        nombre_apellido = self.cleaned_data.get("nombre_apellido")
        if not all(x.isalpha() or x.isspace() for x in nombre_apellido):
            raise ValidationError("El nombre solo puede estar compuesto por letras y espacios")
        return nombre_apellido

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise ValidationError("La contraseña debe tener al menos 6 caracteres")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data
