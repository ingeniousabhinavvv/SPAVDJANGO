from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def noticeboard(request):
    return render(request, 'noticeboard.html')


def gallery(request):
    return render(request, 'gallery.html')
