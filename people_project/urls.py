"""
URL configuration for people_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from people import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.person_list, name='person_list'),
    path('create/', views.person_create, name='person_create'),
    path('update/<int:pk>/', views.person_update, name='person_update'),
    path('delete/<int:pk>/', views.person_delete, name='person_delete'),
]
