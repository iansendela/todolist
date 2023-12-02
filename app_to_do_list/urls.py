from django.urls import path
from app_to_do_list import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('editar/<uuid:id_tarefa>/', views.editar_tarefa, name='editar_tarefa'),
    path('delete/<uuid:id_tarefa>/', views.delete, name='delete'),
    path('concluida/<uuid:id_tarefa>/', views.concluida, name='concluida'),
    path('desmarcar_concluido<uuid:id_tarefa>/', views.desmarcar_concluida, name='desmacar_concluida'),
    ]