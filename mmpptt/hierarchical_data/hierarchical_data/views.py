from django.shortcuts import render
from hierarchical_data.models import File


def show_files(request):
    return render(request, "files.html", {'files': File.objects.all()})
