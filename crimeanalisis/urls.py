from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('upload/', views.upload, name='upload'),
  path('resultados/', views.resultados, name='resultados'),
  path('historial/', views.historial, name='historial')
]
