from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Author
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'login.html')

def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.Error(request, 'Invalid username/password')
            return redirect('login_view')
    return render(request, 'login_view.html')

def register_view(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        if (password == c_password):
            if len(password) >= 8:
                if User.objects.filter(username= username).exists():
                    messages.Error(request, "Username already exists")
                    return redirect('register_view')
                else:
                    user = User.objects.create_user(username = username, password = c_password)
                    Author.objects.create(user=user)
                    return redirect('login_view')
            else:
                messages.Error(request, "Password must be atleast 8 char long")
                return redirect('register_view')
        else:
            messages.Error(request, "Password do not match")
            return redirect('register_view')
    return render(request, 'register.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')