from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('search/', views.post_search, name='post_search'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]