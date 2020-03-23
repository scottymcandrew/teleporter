from django.urls import path
from features import views


urlpatterns = [
    path('all_features/', views.all_features, name='all_features'),
    path('create_feature_report/', views.create_feature_report, name='create_feature_report'),
    path('detail/<int:id>/', views.feature_detail, name='feature_detail'),
    path('vote/', views.feature_vote, name='feature_vote'),
    path('search/', views.feature_search, name='feature_search'),
    path('<pk>/edit/', views.FeatureEdit.as_view(), name='feature_edit'),
    path('<pk>/delete/', views.FeatureDelete.as_view(), name='feature_delete'),
]
