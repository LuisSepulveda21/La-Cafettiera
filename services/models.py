from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="contenido")
    image = models.ImageField(verbose_name="imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    # metadatos
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.title
