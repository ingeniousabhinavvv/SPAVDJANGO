from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('gallery/', views.gallery, name='gallery'),
]
