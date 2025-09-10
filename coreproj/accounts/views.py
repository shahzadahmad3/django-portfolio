from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)   # Log the user in after signup
        messages.success(self.request, "Account created successfully. Please log in.")
        return super().form_valid(form)

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("post_list")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = reverse_lazy("login")


    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "accounts/profile.html"
    context_object_name = "profile_user"

    def get_object(self):
        return self.request.user


class ProfilePictureUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ["avatar"]   # only allow avatar updates
    template_name = "accounts/profile_picture_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

