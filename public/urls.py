from django.urls import path
from public import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about_us, name='about_us'),
    path('service_stats/', views.service_stats, name='service_stats'),
    path('all_features_chart/', views.all_features_chart, name='all_features_chart'),
    path('all_bugs_chart/', views.all_bugs_chart, name='all_bugs_chart'),
    path('resolved_bugs_chart/', views.resolved_bugs_chart, name='resolved_bugs_chart'),
]
