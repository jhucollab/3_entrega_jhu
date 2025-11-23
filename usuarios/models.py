from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(default="")
    foto = models.ImageField(upload_to='fotos_cv/', blank=True, null=True)

    def __str__(self):
        return f"CV de {self.usuario.username}"
# Create your models here.
