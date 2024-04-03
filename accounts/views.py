from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth import authenticate
from django.contrib.messages import error

from django.views.generic import CreateView

from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

def loginView(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username = username, password = password)
    print("loginView was called")

    if user:
        pass
    else:
        print("Invalid username or password")
        error(request, "Invalid username or password")
        return render(request, "registration/login.html")

# def signUp(request):
#     return render(request, "registration/signup.html")