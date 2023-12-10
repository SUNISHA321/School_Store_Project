from . models import Department
def menu_link(request):
    links=Department.objects.all()
    return dict(links=links)