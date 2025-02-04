from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='blog'),
    path('<int:blog_id>/', views.single_blog, name='single_blog'),
]
