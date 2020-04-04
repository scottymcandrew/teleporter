from django.urls import path
from bugs import views

urlpatterns = [
    path('', views.all_bugs, name='all_bugs'),
    path('all_bugs/', views.all_bugs, name='all_bugs'),
    path('create_bug_report/', views.create_bug_report, name='create_bug_report'),
    path('detail/<int:id>/', views.bug_detail, name='bug_detail'),
    path('vote/', views.bug_vote, name='bug_vote'),
    path('search/', views.bug_search, name='bug_search'),
    path('<pk>/edit/', views.BugEdit.as_view(), name='bug_edit'),
    path('<pk>/delete/', views.BugDelete.as_view(), name='bug_delete'),
    path('update_bug_status/', views.update_bug_status, name='update_bug_status'),
]
