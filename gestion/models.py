from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.username

class Lote(models.Model):
    usuario = models.ForeignKey('gestion.Usuario', on_delete=models.CASCADE)
    id_lote = models.CharField(max_length=10, unique=True)
    fecha_registro = models.DateTimeField(default=timezone.now)

    analisis_espectrometrico = models.FileField(upload_to='lotes/%Y/%m/%d/', blank=True, null=True)
    tolerancia_geometrica = models.FileField(upload_to='lotes/%Y/%m/%d/', blank=True, null=True)
    numero_partes = models.FileField(upload_to='lotes/%Y/%m/%d/', blank=True, null=True)
    prueba_dureza_tension = models.FileField(upload_to='lotes/%Y/%m/%d/', blank=True, null=True)
    evidencia_fotografica = models.FileField(upload_to='lotes/%Y/%m/%d/', blank=True, null=True)
    plano_original = models.FileField(upload_to='lotes/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f"Lote {self.id_lote}"
