from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

urlpatterns = [

    path('', views.home, name=""),
    path('login/', authentication_views.LoginView.as_view(template_name='templates/portfolio1/index.html'), name='login'),

]