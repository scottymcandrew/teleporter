from django.urls import path
from public import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about_us, name='about_us'),
    path('service_stats/', views.service_stats, name='service_stats'),
]
