from django.shortcuts import render, redirect
from .models import Register
from .forms import ResForm
from django.contrib import messages



# Create your views here.
def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        from django.contrib import auth
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        form = ResForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, 'Student created successfully.')
           return redirect("register")
    else:
        form = ResForm
    return render(request,"register.html",{'form': form})

