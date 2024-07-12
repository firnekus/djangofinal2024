from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Perfil

# *********************************************************************************************************#
#                                                                                                          #
# INSTRUCCIONES PARA EL ALUMNO, PUEDES SEGUIR EL VIDEO TUTORIAL, COMPLETAR EL CODIGO E INCORPORAR EL TUYO: #
#                                                                                                          #
# https://drive.google.com/drive/folders/1ObwMnpKmCXVbq3SMwJKlSRE0PCn0buk8?usp=drive_link                  #
#                                                                                                          #
# *********************************************************************************************************#

# PARA LA PAGINA MANTENEDOR DE PRODUCTOS:
# Crea ProductoForm como una clase que hereda de ModelForm
# asocialo con el modelo Producto
# muestra todos los campos
# crea 2 widgets para:
#   - la descripción del producto como TextArea
#   - el botón de cargar imagen como FileInput y 
#     escóndelo para reemplazarlo por otro acorde 
#     con tu diseño gráfico
# renombra las siguientes etiquetas para que ocupen menos
# espacio en la página: 'Nombre', 'Subscriptor(%)' y 'Oferta(%)'
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'subscriptor': 'Subscriptor(%)',
            'oferta': 'Oferta(%)'
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'imagen': forms.FileInput(attrs={'style': 'display:none;'})
        }

# El formulario de bodega está listo, no necesitas modificarlo
class BodegaForm(Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label ="", widget=forms.Select(attrs={'class': 'form-control'}))
    producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label='', widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class':"form-control"}))
    class Meta:
        fields = '__all__'

# El formulario de ingreso está listo, no necesitas modificarlo
class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': 'Ingresa tu usuario'}), label="Cuenta")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder': 'Ingresa tu contraseña'}), label="Contraseña")
    
    class Meta:
        fields = ['username', 'password']

# PARA LA PAGINA DE REGISTRO DE NUEVO CLIENTE:
# Crea RegistroUsuarioForm como una clase que hereda de UserCreationForm
# asocialo con el modelo User
# muestra los campos: 
#    'username', 'first_name', 'last_name', 'email', 'password1' y 'password2'
# renombra la etiqueta del campo 'email' por 'E-mail'
class RegistroUsuarioForm(UserCreationForm):
   class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'email': 'E-mail'
        }




# PARA LA PAGINA DE REGISTRO DE NUEVO CLIENTE Y MIS DATOS:
# Crear RegistroPerfilForm como una clase que hereda de ModelForm
# asocialo con el modelo Perfil
# muestra los campos: 'rut', 'direccion', 'subscrito', 'imagen'
# excluye el campo 'tipo_usuario', pues sólo los administradores asignan el tipo
# crea los widgets para:
#   - direccion como Textarea,
#   - imagen como FileInput()
class RegistroPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'direccion', 'subscrito', 'imagen']
        exclude = ['tipo_usuario']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
        }

# PARA LA PAGINA MIS DATOS Y MANTENEDOR DE USUARIOS:
# Crear UsuarioForm como una clase que hereda de ModelForm
# asocialo con el modelo User
# muestra todos los campos: 'username', 'first_name', 'last_name' e 'email'
# renombra la etiqueta del campo 'email' por 'E-mail'
class UsuarioForm(ModelForm):
   class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

# PARA LA PAGINA MANTENEDOR DE USUARIOS:
# Crear PerfilForm como una clase que hereda de ModelForm
# asocialo con el modelo Perfil
# muestra todos los campos: 
#    'tipo_usuario', 'rut', 'direccion', 'subscrito'e 'imagen'
# crea los widgets para:
#   - direccion como Textarea,
#   - imagen como FileInput()
class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['tipo_usuario', 'rut', 'direccion', 'subscrito', 'imagen']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'})
        }