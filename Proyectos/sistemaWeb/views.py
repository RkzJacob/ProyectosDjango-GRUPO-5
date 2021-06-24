from sistemaWeb.forms import publicacionForm
from django.shortcuts import redirect,render
from .models import PublicacionArte,Categoria

# Create your views here.
def index(request):
    
    Cat =Categoria.objects.all()
    #cargo datos de categoria en la pagina principal
    datos ={
        'Cat' : Cat,
        'form':publicacionForm
    }
    if request.method == 'POST':
        formulariod= publicacionForm(request.POST,request.FILES)

        if formulariod.is_valid:
            formulariod.save()
            datos['mensaje']= 'datos guardados correctamente'
        else:
            datos['mensaje']= 'datos no guardados'
    return render(request,'sistemaWeb/index2.html',datos)


def register(request):
    return render(request,'sistemaWeb/register.html')

def login(request):
    return render(request,'sistemaWeb/login.html')

def pinturas(request):
    PubliArte =PublicacionArte.objects.all()
    #cargo los datos de publicaciones de artes con todos sus datos en los artistas 
    datos ={
        'PubliArte' : PubliArte
    }
    return render(request,'sistemaWeb/Pinturas.html',datos)

def artistas(request):
    PubliArte =PublicacionArte.objects.all()
    #cargo los datos de publicaciones de artes con todos sus datos en los artistas 
    datos ={
        'PubliArte' : PubliArte
    }

    return render(request,'sistemaWeb/artistas.html',datos)

def CondicionesServicio(request):
    return render(request,'sistemaWeb/CondicionesServicio.html')

def form_publi(request):


    datos={
        'form': publicacionForm
    }


    return render(request,'sistemaWeb/form.html',datos)

def modificarPintura(request,id):

    pinturaPersona=PublicacionArte.objects.get(Nombre=id)

    dic={
        'form':publicacionForm(instance=pinturaPersona)
    }

    if request.method == 'POST':
        formulario=publicacionForm(data=request.POST,instance=pinturaPersona,files=request.FILES)

        if formulario.is_valid:
            formulario.save()
            dic['mensaje']="datos modificados exitosamente"
        else:
            dic['mensaje']="datos no modificados"

    return render(request,'sistemaWeb/modificar.html',dic)

def eliminarPintura(request,id):
    publicacion=PublicacionArte.objects.get(Nombre=id)

    publicacion.delete()

    return redirect(to="listaPublicaciones")
    
def listaPublicaciones(request):
    PubliArte =PublicacionArte.objects.all()
    #cargo los datos de publicaciones de artes con todos sus datos en los artistas 
    datos ={
        'PubliArte' : PubliArte
    }
    return render(request,'sistemaWeb/lista.html',datos)