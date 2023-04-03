from django.shortcuts import render
from django.http import HttpResponse
from tercera_pre_entrega.models import Notas, Usuario
from tercera_pre_entrega.forms import NotasForm
from django.views.generic import ListView

def mostrar_notas(request):
    
    notas = Notas.objects.all()
    total_notas = len(notas)
    context = {
        "notas": notas, 
        "total_notas":total_notas,
        "form": NotasForm(),
    }
    return render(request, "tercera_pre_entrega/notas.html", context)


def alta_notas(request):
    f = NotasForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Notas(alumno = f.data["alumno"], materia = f.data["materia"], fecha_parcial = f.data["fecha_parcial"], nota_parcial = f.data["nota_parcial"]).save()
        context["form"] = NotasForm()

    context["notas"] = Notas.objects.all()
    context["total_notas"] = len(Notas.objects.all())

    return render(request, "tercera_pre_entrega/notas-create.html", context)