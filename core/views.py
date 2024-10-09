# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import UserLogin  # Import the UserLogin model
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# core/views.py
from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        # If the user is logged in, display a personalized welcome message
        context = {
            'username': request.user.username
        }
        return render(request, 'home.html', context)
    else:
        # If the user is not logged in, display the default homepage
        return render(request, 'home.html')


class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to a success page.
        return render(request, 'signup.html', {'form': form})

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')  # Render your login template

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Save the login information to the database
            user_login = UserLogin.objects.create(user=user, ip_address=request.META.get('REMOTE_ADDR'))
            user_login.save()
            
            return redirect('home')  # Redirect to a success page.
        return render(request, 'login.html', {'error': 'Invalid credentials'})

def home(request):
    return render(request, 'home.html')


@login_required
def logout_view(request):
    auth.logout(request)  # Logout the current user
    return redirect('home')  # Redirect to the login page