from typing import ChainMap

from django.db import models


# Crear mi modelos

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True,verbose_name='idcategoria')
    nombreCategoria=models.CharField(max_length=40,verbose_name="nombre categoria")


    def __str__(self) :
        return self.nombreCategoria


#clase vehiculo

class PublicacionArte(models.Model):
    Nombre= models.CharField(primary_key=True,max_length=20,verbose_name='nombre')
    apellido =models.CharField(max_length=20,null=True,blank=True,verbose_name="apellido")
    correo= models.CharField(max_length=40,null=True,blank=True,verbose_name="correo")
    nombreObra=models.CharField(max_length=20,null=True,blank=True,verbose_name="NombreObra")
    descObra=models.TextField(max_length=400,null=True,blank=True,verbose_name="DescObra")
    imagenPublicacion=models.ImageField(upload_to="fotopublicaciones",null=True,blank=True,verbose_name="imagen")
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) :
        return self.Nombre
