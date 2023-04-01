from django.shortcuts import render
from django.http import HttpResponse

def mostrar_mi_template(request):
    return render (request, "tercera_pre_entrega/index.html")
