from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request, "core/Home.html")                      

def Contacto(request):
    return render(request, "core/Contacto.html")
    
def Mas(request):
    return render(request, "core/Mas.html")

def Nosotros(request):
    return render(request, "core/Nosotros.html")

    