from django.urls import path
from .views import procesar_publicacion,detalle_pintura
from .viewslogin import login


urlpatterns =[

    path('pinturas',procesar_publicacion,name="procesar_publicacion"),
    path('pinturas/<id>',detalle_pintura,name="detalle_pintura"),
    path('login',login,name="login"),
]