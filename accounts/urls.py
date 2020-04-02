from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    # Using Django's in-built authentication URL patterns:
    # https://github.com/django/django/blob/stable/2.2.x/django/contrib/auth/urls.py
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    # path('all_features_chart/', views.all_features_chart, name='all_features_chart'),
    path('my_features_chart/', views.my_features_chart, name='my_features_chart'),
]
