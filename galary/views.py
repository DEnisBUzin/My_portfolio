from django.shortcuts import render, get_object_or_404
# from .models import Project

def projects(request):
    # projects = Project.objects.all()
    return render(request, 'index.html')
