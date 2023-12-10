from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentialsapp.forms import CourseForm
from schoolstoreapp.models import Course


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect("register")
            else:
                user=User.objects.create(username=username)
                user.set_password(password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not match")

    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            form=CourseForm()
            return render(request,"course.html",{"form":form})
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")
def load_course(request):
    depart_id = request.GET.get('depart')
    course = Course.objects.filter(department=depart_id).order_by('name')
    return render(request,"load_course.html",{"course":course})
def apply(request):
    if request.method == 'POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Order Confirmed')
            form = CourseForm()
            print("valid")
        else:
            messages.error(request, 'Failed')




    return render(request, "course.html", {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('/')