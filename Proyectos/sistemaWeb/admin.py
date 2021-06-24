from django.contrib import admin
from .models import Categoria, PublicacionArte

# Register your models here.
#permite administrar los modelos completos


admin.site.register(Categoria)
admin.site.register(PublicacionArte)
