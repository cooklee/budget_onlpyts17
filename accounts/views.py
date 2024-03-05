from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View


# Create your views here.


class CreateUserView(View):

    def get(self, request):
        return render(request, 'create_user.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['password2']
        if password != re_password:
            return render(request,'create_user.html', {'error':'hasła są różne'})
        # u = User.objects.create_user(username=username, password=password)
        u = User(username=username)
        u.set_password(password)
        u.save()
        return redirect('home')


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('login')

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('home')