from django.urls import path
from .views import procesar_publicacion,detalle_pintura


urlpatterns =[

    path('pinturas',procesar_publicacion,name="procesar_publicacion"),
    path('pinturas/<id>',detalle_pintura,name="detalle_pintura")
]