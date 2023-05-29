from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'Auths/Signup.html'
    context = {'form':form}
    return render(request, template_name, context)

def Login_view(request):
    template_name = 'Auths/Login.html'
    context = {}
    if request.method == "POST":
        User = request.POST.get('user')
        Pass = request.POST.get('pass')

        user = authenticate(username = User, password = Pass)
        if user is not None:
            login(request, user)
            return redirect('details')
    return render(request, template_name, context)

def Logout_view(request):
    logout(request)
    return redirect('login')