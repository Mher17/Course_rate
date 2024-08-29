from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views._login, name="login"),
    path("logout", views.log_out, name="logout"),
    path("", views.enter_main_page, name= "enter_main_page"),
    path("<int:course_id>/", views.detail, name= "detail"),
    path("<int:course_id>/rate/", views.rate, name="rate"),
]

