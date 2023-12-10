from . import views
from django.urls import path
app_name='school'
urlpatterns = [
    path('', views.index,name='school'),
    path('<slug:d_slug>/', views.departDetail, name='departDetail'),

]