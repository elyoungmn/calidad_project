from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def registrar_lote(request):
    # Lógica de la vista para registrar un lote
    return render(request, 'gestion/registrar_lote.html')

def ver_lotes(request):
    # Lógica para ver los lotes
    return render(request, 'gestion/ver_lotes.html')

def detalle_lote(request, lote_id):
    # Lógica para ver detalles de un lote
    return render(request, 'gestion/detalle_lote.html')

def descargar_archivo(request, lote_id, tipo_archivo):
    # Lógica para descargar un archivo
    pass

def descargar_zip(request, lote_id):
    # Lógica para descargar un archivo zip
    pass

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ver_lotes')
    else:
        form = UserCreationForm()
    return render(request, 'gestion/registro.html', {'form': form})
