from django.urls import path
from .import views

app_name = 'pefil'

urlpatterns = [
  path('', views.Criar.as_view(), name="criar"),
  path('atualizar/', views.Atualizar.as_view(), name="atualizar"),
  path('login/', views.Login.as_view(), name="criar"),
  path('logout', views.Logout.as_view(), name="logout"),

]