from .models import Post
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView
from .api_views import PostListAPI, PostDetailAPI

urlpatterns = [
    # path('', home_view, name='home'),
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('api/posts/', PostListAPI.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', PostDetailAPI.as_view(), name='api_post_detail'),
]
