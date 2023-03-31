from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('perfil/', views.perfil, name="perfil"),
    path('add_materia_aluno/', views.add_materia_aluno, name="add_materia_aluno"),
    path('delete_all_materia_aluno/', views.delete_all_materias_aluno, name="delete_all_materia_aluno"),

]