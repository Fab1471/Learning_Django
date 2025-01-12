from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'loja/home.html')

def lancamentos(request):
    return render(request, 'loja/lancamentos.html')

def masculino(request):
    return render(request, 'loja/masculino.html')

def feminino(request):
    return render(request, 'loja/feminino.html')
