from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("create/", views.create_form, name='create'),
    path("load/", views.load_form, name='load'),
    path("vote/<int:pk>/", views.vote, name='vote'),
    path("results/", views.results, name='results'),



]
