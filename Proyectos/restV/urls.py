from django.urls import path
from .views import procesar_publicacion


urlpatterns =[

    path('pinturas',procesar_publicacion,name="procesar_publicacion")
]