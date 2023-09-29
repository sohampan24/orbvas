from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect  # Add this import

# Create your views here.

@csrf_protect  # Add the decorator here
def HomePage(request):
    return render(request, 'home.html')

@csrf_protect  # Add the decorator here
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        phnno = request.POST.get('phnno')

        if pass1 != pass2:
            return HttpResponse("Your password does not match!!")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('login')

        print(uname, email, pass1, pass2, phnno)
    return render(request, 'signup.html')

@csrf_protect  # Add the decorator here
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!!!")

    return render(request, 'UserLogin.html')
