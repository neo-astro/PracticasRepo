
from django.contrib import admin
from django.urls import path
from Crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('estudiante/', views.Estudiante,name='estudiante'),
    path('estudiante/eliminar/<str:id>/', views.deleteEstudiante),
    path('estudiante/update/<str:id>/', views.updateEstudiante),

    path('usuario/', views.usuario,name='usuario'),
    path('usuario/update/<str:N_Identificacion>/', views.updateUsuario,name='usuarioupdate'),
    path('usuario/eliminar/<str:N_Identificacion>/', views.deleteUser),
    path('provincia/<str:nombre_pais>/', views.ApiProvincia),
    path('ciudad/<str:nombre_provincia>/', views.ApiCiudad),
    path('asignarEstudiante/', views.asignarEstudiante)
]
