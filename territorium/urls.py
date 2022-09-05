from unicodedata import name
from django.urls import path

from . import views     #dentro del mismo paquete importar vistas

app_name = "territorium"

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('loginForm/', views.loginForm, name="loginForm"),
    
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    
    
    
    
    
    path('aprendices/', views.aprendices, name="aprendices"),
    path('crear_aprendices/', views.aprendicesFormulario, name="crear_aprendiz"),
    path('guardar_aprendices/', views.aprendicesGuardar, name="guardar_aprendiz"),
    path('eliminar_aprendices/<int:id>',views.aprendicesEliminar, name="eliminar_aprendiz"),
    path('editar_aprendices/<int:id>', views.aprendizFormularioEditar, name="aprendizFormularioEditar"),
    path('actualizar_aprendices/', views.actualizarAprendiz, name="actualizarAprendiz"),
    path('aprendicesBuscar/', views.aprendicesBuscar, name = "aprendicesBuscar"),


    path('monitorias/', views.monitorias, name="monitorias"),
    path('crear_monitorias/', views.monitoriasFormulario, name="crear_monitoria"),
    path('guardar_monitorias/', views.monitoriasGuardar, name="guardar_monitoria"),
    path('eliminar_monitorias/<int:id>',views.monitoriasEliminar, name="eliminar_monitoria"),


    path('actividades/', views.actividades, name="actividades"),
    path('crear_actividades/', views.actividadesFormulario, name="crear_actividad"),
    path('guardar_actividades/', views.actividadesGuardar, name="guardar_actividad"),
    path('eliminar_actividades/<int:id>',views.actividadesEliminar, name="eliminar_actividad"),






    
]