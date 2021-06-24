from django.urls import path
from django.urls.resolvers import URLPattern 
from .views import form_publi, index,register,login,artistas,pinturas,CondicionesServicio,modificarPintura,eliminarPintura,listaPublicaciones
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('artistas/',artistas,name='artistas'),
    path('Pinturas/',pinturas,name='pinturas'),
    path('CondicionesServicio/',CondicionesServicio,name='CondicionesServicio'),
    path('form',form_publi,name='form_publi'),
    path('editar/<id>',modificarPintura,name='modificarPintura'),
    path('eliminar/<id>',eliminarPintura,name='eliminarPintura'),
    path('lista',listaPublicaciones,name='listaPublicaciones')



]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)