from django.urls import path
from bugs import views


urlpatterns = [
    path('all_bugs/', views.all_bugs, name='all_bugs'),
    path('create_bug_report/', views.create_bug_report, name='create_bug_report'),
    path('detail/<int:id>/', views.bug_detail, name='bug_detail'),
    path('vote/', views.bug_vote, name='bug_vote'),
]
