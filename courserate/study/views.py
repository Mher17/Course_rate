from django.shortcuts import get_object_or_404, render
from django.db.models import F
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import LectureUser, Course
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def enter_main_page(request):
    if request.user.is_authenticated:
        course_list = Course.objects.order_by("title")
        context = {"course_list": course_list}
        return render(request, "study/main_page.html", context)
    else:
        return HttpResponseRedirect("/study/login")

def register(request):
    if request.method == "GET":
        return render(request, "study/register.html", {})
    
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    age = request.POST['age']

    user = User.objects.create_user(first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                password=password)
    
    user.save()
    lu = LectureUser(user=user, age=age)
    lu.save()

    return HttpResponseRedirect("/study/login")

def _login(request):
    if request.method == "GET":
        return render(request, "study/login.html", {})
    
    usr = request.POST['username']
    pswd = request.POST['password']
 
    user = authenticate(username=usr, password=pswd)
    if user:
        login(request, user)
        return HttpResponseRedirect("/study/")
    
    return render(request, "study/login.html", {"error": "username or password is wrong"})

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/study/login")

def rate(request, course_id, rating):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, pk=course_id)
        course.count += 1
        course.rate = (((course.count - 1) * course.rate) + rating) / course.count
        course.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
        return HttpResponseRedirect(reverse("study:detail", args=(course.id,)))
    else:
        return HttpResponseRedirect("/study/login")

def detail(request, course_id):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, pk=course_id)
        return render(request, "study/detail.html", {"course": course})
    else:
        return HttpResponseRedirect("/study/login")