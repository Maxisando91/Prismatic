from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('bonjovi',views.bonjovi, name='bonjovi'),
    path('registro',views.registro, name='registro'),
]