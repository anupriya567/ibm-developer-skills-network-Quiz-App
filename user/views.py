from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin , logout
from django.contrib.auth.models import User

def handlesignup(request):
    if request.method =="POST":
        # Get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        
        pass1 = request.POST['spassword1']
        pass2 = request.POST['spassword2']
        
        username = fname+" "+lname
        error = False
        # check for errorneous input
        if len(username)<10:
            error = True

        if pass1!= pass2:
            error = True

        if error == True:
            messages.error(request, "Invalid credentials")
            return redirect('onlinecourse')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,  "Your account created successfully")
        return redirect('onlinecourse')

    else:
        return HttpResponse("404 - Not found")

# Create your views here.
def handlelogin(request): 
    if request.method =="POST":
        # Get the post parameters
        name = request.POST['llname']
        pass1 = request.POST['lpassword1']
        user = authenticate(username = name, password = pass1)
        
        if user is not None:
            dlogin(request, user)
            messages.success(request, "You are loggedin successfully")
            return redirect('onlinecourse')
        else:         
            messages.error(request, "invalid credentials")
            return redirect('onlinecourse')

    else:
        return HttpResponse("404 - Not found")


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('onlinecourse') 