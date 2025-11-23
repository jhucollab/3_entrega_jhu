from django.db import models
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.db import models

class CV(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    def __str__(self):
        return f"CV de {self.usuario.username}"
from django.contrib.auth.models import User
from django.db import models

class CV(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(default="")
    experiencia_laboral = models.TextField(default="")
    estudios_realizados = models.TextField(default="")
# Create your models here.
