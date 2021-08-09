"""DjangoHindiTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from student_management_system_app import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginUser, name="login"),
    path('signup', views.signupUser, name="signup"),
    path('signup_process', views.signup_process, name="signup_process"),
    path('login_proces', views.login_proces, name="login_proces"),
    path('home',views.home,name="home"),
    path('logout',views.logoutUser,name="logout"),
    url(r'^',include('api.urls'))
]
