"""mycontacts URL Configuration

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
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('indexx',views.indexx),
    path('',views.index),
    path('register',views.register),
    path('addregister',views.addregister),
    path('addcontact',views.addcontact),
    path('viewcontact',views.viewcontact),
    path('contactview',views.contactview),
    path('viewdetails',views.viewdetails),
    path('detailview',views.detailview),
    path('login',views.login),
    path('addlogin',views.addlogin),
    path('admin',views.admin),
    path('user',views.user),
    path('logout',views.logout),
    path('userprofile',views.userprofile),
    path('adminss',views.adminss),
    path('userinfo',views.userinfo),
    path('delete/<int:id>',views.delete,name='delete'),
    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser'),
    path('updatecontact',views.updatecontact),
    path('updateuser',views.updateuser),
    path('update/<int:id>',views.update,name='update'),
    path('update/updates/<int:id>',views.updates,name='updates'),
    path('update1/<int:id>',views.update1,name='update1'),
    path('update1/updateuser/<int:id>',views.updateuser,name='updateuser'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
