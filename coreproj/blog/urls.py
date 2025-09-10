from .models import Post
from django.urls import path, include
from .views import home_view, PostListView, PostDetailView, PostCreateView

urlpatterns = [
    # path('', home_view, name='home'),
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
]
