"""podgotovka URL Configuration

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
from django.urls import path, include
from apps.views import Temp,ProductView, Login,SignUp
from  users import  urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Temp.as_view()),
    path('pr/', ProductView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include(urls)),
    path('login/', Login.as_view(), name='login'),
    path('reg/', SignUp.as_view()),
]
