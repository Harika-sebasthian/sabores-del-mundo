from django.db import models


class Consulta(models.Model):
    nombre    = models.CharField(max_length=200)
    email     = models.EmailField()
    asunto    = models.CharField(max_length=200)
    mensaje   = models.TextField()
    categoria = models.CharField(max_length=50, blank=True)
    fecha     = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        texto = self.mensaje.lower()
        if any(p in texto for p in ['precio','costo','cuesta','tarifa','compra']):
            self.categoria = 'Consulta Comercial'
        elif any(p in texto for p in ['soporte','error','problema','ayuda']):
            self.categoria = 'Consulta Técnica'
        elif any(p in texto for p in ['trabajo','trabajar','cv','empleo','linkedin']):
            self.categoria = 'Consulta de RRHH'
        else:
            self.categoria = 'Consulta General'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} — {self.categoria}'

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['-fecha']


class UsuarioPermitido(models.Model):
    nombre            = models.CharField(max_length=200)
    email             = models.EmailField(unique=True)
    codigo_validacion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} — {self.email}'

    class Meta:
        verbose_name = 'Usuario Permitido'
        verbose_name_plural = 'Usuarios Permitidos'