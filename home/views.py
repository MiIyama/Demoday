from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request, 'index.html')

def mostrar_cadastro(request):
    return render(request, 'cadastro.html')

def mostrar_cadastrook(request):
    return render(request, 'cadastrook.html')