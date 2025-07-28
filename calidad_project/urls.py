# calidad_project/urls.py
from django.contrib import admin
from django.urls import path
from gestion import views  # Importando las vistas desde la app 'gestion'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registrar_lote, name='registrar_lote'),
    path('lotes/', views.ver_lotes, name='ver_lotes'),
    path('lotes/<int:lote_id>/', views.detalle_lote, name='detalle_lote'),
    path('lotes/<int:lote_id>/descargar/<str:tipo_archivo>/', views.descargar_archivo, name='descargar_archivo'),
    path('lotes/<int:lote_id>/descargar_zip/', views.descargar_zip, name='descargar_zip'),
    path('registro/', views.registro_usuario, name='registro'),
]
