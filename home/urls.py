
from django.urls import path

from . import views

# / Isso faz com que o app(pasta) seja reconhecido inteiramente como esse nome
app_name = 'home'

urlpatterns = [
    path('', views.home, name='Home'),
]
