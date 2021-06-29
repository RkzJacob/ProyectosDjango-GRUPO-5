from django.shortcuts import render
from sistemaWeb.models import PublicacionArte
from .serializers import PublicacionSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['GET'])

def procesar_publicacion(request):
    if request.method == 'GET' :#listar todos los vehiculos
        pinturas = PublicacionArte.objects.all() 
        serializer = PublicacionSerializer(pinturas,many=True)
        return Response(serializer.data)


