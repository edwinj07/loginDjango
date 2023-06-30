from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('inicio',views.inicio,name='inicio'),
    path('registro',views.registro,name='registro'),
    path('solucion',views.solucion,name='solucion'),
    path('cerrar',views.cerrar,name='cerrar'),
    path('home',views.home,name='home'),
    path('solucion/usuario',views.usuario,name='usuario'),
    path('solucion/perfil',views.perfil,name='perfil'),
    path('solucion/<int:cc>',views.editar_perfil,name='editar_perfil'),
    path('solucion/<int:cc>/eliminar_perfil',views.eliminar_perfil,name='eliminar_perfil'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)