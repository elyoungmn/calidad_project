from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoteForm, CustomUserCreationForm
from .models import Lote
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
import zipfile
import io

@login_required
def registrar_lote(request):
    if request.method == 'POST':
        form = LoteForm(request.POST, request.FILES)
        if form.is_valid():
            lote = form.save(commit=False)
            lote.usuario = request.user
            try:
                lote.save()
                messages.success(request, "Lote registrado correctamente.")
                return redirect('ver_lotes')
            except IntegrityError:
                form.add_error('id_lote', 'Ya existe un lote con este ID.')
    else:
        form = LoteForm()
    return render(request, 'gestion/registrar_lote.html', {'form': form})
@login_required
def ver_lotes(request):
    lotes = Lote.objects.filter(usuario__empresa=request.user.empresa)
    return render(request, 'gestion/listar_lotes.html', {'lotes': lotes})


@login_required
def detalle_lote(request, lote_id):
    lote = get_object_or_404(Lote, id=lote_id, usuario__empresa=request.user.empresa)
    return render(request, 'gestion/detalle_lote.html', {'lote': lote})

@login_required
def descargar_archivo(request, lote_id, tipo_archivo):
    lote = get_object_or_404(Lote, id=lote_id, empresa=request.user.empresa)
    archivo = getattr(lote, tipo_archivo)
    if archivo and archivo.name:
        return FileResponse(archivo.open('rb'), as_attachment=True)
    return HttpResponse('Archivo no disponible.', status=404)

@login_required
def descargar_zip(request, lote_id):
    lote = get_object_or_404(Lote, id=lote_id)
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        if lote.analisis_espectrometrico:
            zip_file.write(lote.analisis_espectrometrico.path, 'analisis_espectrometrico.pdf')
        if lote.tolerancia_geometrica:
            zip_file.write(lote.tolerancia_geometrica.path, 'tolerancia_geometrica.pdf')
        if lote.numero_partes:
            zip_file.writestr('numero_partes.txt', str(lote.numero_partes))
        if lote.prueba_dureza_tension:
            zip_file.write(lote.prueba_dureza_tension.path, 'prueba_dureza_tension.pdf')
        if lote.evidencia_fotografica:
            zip_file.write(lote.evidencia_fotografica.path, 'evidencia_fotografica.jpg')
        if lote.plano_original:
            zip_file.write(lote.plano_original.path, 'plano_original.pdf')

    zip_buffer.seek(0)
    filename = f"{lote.id_lote.zfill(5)}.zip"
    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ver_lotes')  # O la página a la que deseas redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'gestion/registro.html', {'form': form})