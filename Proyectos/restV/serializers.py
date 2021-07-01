from rest_framework import serializers 
from sistemaWeb.models import PublicacionArte


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionArte
        fields=['Nombre','apellido','correo','nombreObra','descObra','imagenPublicacion','categoria']
