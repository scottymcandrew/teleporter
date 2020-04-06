from django.urls import path
from blog import views


urlpatterns = [
    path('', views.all_blog_posts, name='all_blog_posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.blog_post_detail, name='blog_post_detail'),
]
