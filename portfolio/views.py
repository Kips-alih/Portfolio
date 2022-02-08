from django.shortcuts import render
from .models import Project


# Create your views here.
def index(request):
    project=Project.objects.all()

    return render(request, 'main/index.html',{'projects':project})
