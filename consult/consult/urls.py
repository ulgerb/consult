"""consult URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appMy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('about/',About, name='About'),
    path('service/',Service, name='Service'),
    path('contact/',Contact, name='Contact'),
    path('detail/', Detail, name='Detail'),
    # PAGES
    path('pages/blog/', Blog, name='Blog'),
    path('pages/feature/', Feature, name='Feature'),
    path('pages/team/', Team, name='Team'),
    path('pages/testimonial/', Testimonial, name='Testimonial'),
]
