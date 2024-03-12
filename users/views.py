from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"

    def form_valid(self, form):
        # Save the user and authenticate
        response = super().form_valid(form)
        username = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        # Log in the user
        login(self.request, user)
        return response

class Login(generic.FormView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        # Authenticate user
        email = form.cleaned_data.get('username')  # Assuming email is used as username
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        
        if user is not None:
            # Log in the user
            login(self.request, user)
            return redirect('home')
        else:
            # Handle invalid login credentials
            return super().form_invalid(form)

class Logout(View):
    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request)
        # Redirect to the login page
        return redirect('login')

# def signup(request):
#     return render(request, 'signup.html')