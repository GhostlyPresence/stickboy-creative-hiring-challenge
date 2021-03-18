from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    tasks = Task.objects.all()
    return render(request,'taskApp/list-task.html',{'tasks':tasks})

@login_required(login_url='login')
def your_tasks(request):
    schedule = Schedule.objects.filter(employee=request.user)
    return render(request,'taskApp/your_tasks.html',{'schedule' : schedule})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user  = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    context = {'form' : form}
    return render(request, 'taskApp/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password incorrect')
    return render(request, 'taskApp/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')