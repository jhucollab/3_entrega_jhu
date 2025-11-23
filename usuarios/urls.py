from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    registro, login_usuario, CrearCV, VerCV,
    EditarCV, BorrarCV, PagSecreta, logout
)

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("login/", login_usuario, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path("cv/crear/", CrearCV.as_view(), name="crear_cv"),
    path("cv/", VerCV.as_view(), name="ver_cv"),
    path("cv/editar/<int:pk>/", EditarCV.as_view(), name="editar_cv"),
    path("cv/borrar/<int:pk>/", BorrarCV.as_view(), name="borrar_cv"),
    path("secreta/", PagSecreta.as_view(), name="pag_secreta"),
]





