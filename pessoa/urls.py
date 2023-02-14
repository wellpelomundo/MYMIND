from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('s_avaliacao/', views.s_avaliacao, name='s_avaliacao'),
    path('s_anotacao/', views.s_anotacao, name='s_anotacao'),
    path('s_alerta/', views.s_alerta, name='s_alerta'),
    path('registro/', views.registro, name='registro'),
]
