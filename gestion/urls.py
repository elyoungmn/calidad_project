from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.registrar_lote, name='registrar_lote'),
    path('lotes/', views.ver_lotes, name='ver_lotes'),
    path('lotes/<int:lote_id>/', views.detalle_lote, name='detalle_lote'),
    path('lotes/<int:lote_id>/descargar/<str:tipo_archivo>/', views.descargar_archivo, name='descargar_archivo'),
    path('lotes/<int:lote_id>/descargar_zip/', views.descargar_zip, name='descargar_zip'),
    path('registro/', views.registro_usuario, name='registro'),

    # Autenticación con vistas genéricas
    path('accounts/login/', auth_views.LoginView.as_view(template_name='gestion/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
