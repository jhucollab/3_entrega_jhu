from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['descripcion', 'foto']
from django.shortcuts import render, redirect
from .models import CV
from django.contrib.auth.decorators import login_required

@login_required
def VerCV(request):
    try:
        cv = CV.objects.get(usuario=request.user)
    except CV.DoesNotExist:
        return redirect('crear_cv')
    return render(request, 'usuarios/cv_detalle.html', {'cv': cv})
