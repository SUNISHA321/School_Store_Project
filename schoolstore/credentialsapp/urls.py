from django.urls import path

from . import views
app_name='credential'

urlpatterns = [
    path('register',views.register,name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path("load_course/",views.load_course,name="load_course"),
    path('apply', views.apply, name="apply"),

]