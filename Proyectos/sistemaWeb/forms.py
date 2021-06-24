from django import forms
from django.forms import ModelForm
from .models import PublicacionArte




class publicacionForm(ModelForm):

    class Meta:
        model = PublicacionArte
        fields= ['Nombre','apellido','correo','nombreObra','descObra','imagenPublicacion','categoria']