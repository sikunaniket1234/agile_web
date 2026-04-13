from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'), # New Path
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]