from django.urls import path
from bugs import views


urlpatterns = [
    path('create_bug_report/', views.create_bug_report, name='create_bug_report'),
]
