from django.urls import path
# from . import views
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Logueo.as_view(), name='login'),
    path('registro/', PaginaRegistro.as_view(), name='registro'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', ListaPendientes.as_view(), name='tareas'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='detalle-tarea'),
    path('tarea/crear/', CrearTarea.as_view(), name='crear-tarea'),
    path('tarea/editar/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
    path('tarea/eliminar/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea'),

]

