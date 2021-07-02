from django.shortcuts import render
from sistemaWeb.models import PublicacionArte
from .serializers import PublicacionSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
@api_view(['GET','POST'])

def procesar_publicacion(request):
    if request.method == 'GET' :#listar todos los vehiculos
        pinturas = PublicacionArte.objects.all() 
        serializer = PublicacionSerializer(pinturas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST': 
        data= JSONParser().parse(request)
        serializer = PublicacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_pintura(request,id):
    try:
        pintura= PublicacionArte.objects.get(Nombre=id)
    except PublicacionArte.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
    if request.method == 'GET':
        serializer= PublicacionSerializer(pintura)
        return Response(serializer.data)
    
    if request.method== 'PUT':
        data= JSONParser().parse(request)
        serializer = PublicacionSerializer(pintura,data=data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)

    if request.method == 'DELETE':
        pintura.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    


    


