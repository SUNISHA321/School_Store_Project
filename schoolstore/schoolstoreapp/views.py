from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from schoolstoreapp.models import Department


def index(request):
    return render(request, "index.html")

def departDetail(request,d_slug):
    try:
        department=Department.objects.get(slug=d_slug)
    except Exception as e:
        raise e
    return  render(request,'department.html',{'department':department})
