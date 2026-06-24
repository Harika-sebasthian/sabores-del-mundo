from django.db import models

class UsuarioPermitido(models.Model):
    nombre = models.CharField(max_length=200)
    email  = models.EmailField(unique=True)
    codigo_validacion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} — {self.email}'

    class Meta:
        verbose_name = 'Usuario Permitido'
        verbose_name_plural = 'Usuarios Permitidos'