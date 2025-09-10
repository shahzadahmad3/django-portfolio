from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, ProfileView, ProfilePictureUpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("profile/edit-picture/", ProfilePictureUpdateView.as_view(), name="profile_picture_edit"),
]