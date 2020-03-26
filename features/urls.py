from django.urls import path
from features import views

urlpatterns = [
    path('', views.all_features, name='all_features'),
    path('all_features/', views.all_features, name='all_features'),
    path('create_feature_report/', views.request_feature, name='request_feature'),
    path('detail/<int:id>/', views.feature_detail, name='feature_detail'),
    path('search/', views.feature_search, name='feature_search'),
    path('<pk>/edit/', views.FeatureEdit.as_view(), name='feature_edit'),
    path('<pk>/delete/', views.FeatureDelete.as_view(), name='feature_delete'),
]
