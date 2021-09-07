from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def home(request):
    return render(request, 'user/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('dashboard-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You're logged in as {username} ")
#                 return redirect("dashboard-login")
#             else:
#                 messages.error(request,"Invalid username or password")
#         else:
#             messages.error(request, "Invalid username or password")
#     form = AuthenticationForm()
#     return render(request=request, template_name='user/login.html',context={"login_form":form})
