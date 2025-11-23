from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
from django import forms
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['usuario', 'descripcion']  # reemplaza con tus campos reales
from django.shortcuts import render, redirect, get_object_or_404
from .models import CV
from .forms import CVForm
from django.contrib.auth.decorators import login_required

@login_required
def VerCV(request):
    try:
        cv = CV.objects.get(usuario=request.user)
    except CV.DoesNotExist:
        return redirect('crear_cv')  # Redirige a crear CV si no existe
    return render(request, 'usuarios/cv_detalle.html', {'cv': cv})
