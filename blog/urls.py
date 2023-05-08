from django.urls import path

from . import views

# / Isso faz com que o app(pasta) seja reconhecido inteiramente como esse nome
app_name = 'blog'

urlpatterns = [
    path('post/<int:post_id>', views.post, name='post'),
    path('', views.blog, name='Blog'),
]
