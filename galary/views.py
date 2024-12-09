from django.shortcuts import render, get_object_or_404
# from .models import Project


def galary_list(request):
    # projects = Project.objects.all()
    return render(request, 'list_prj.html')
