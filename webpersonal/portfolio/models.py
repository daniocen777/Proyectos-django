from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen")
    # fecha de creación
    # auto_now_add=True => se agregará automáticamente AL CREARSE
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )  # fecha y hora
    # fecha de modificación
    # auto_now=True => se agregará automáticamente CADA VEZ QUE SE MODIFICA
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

