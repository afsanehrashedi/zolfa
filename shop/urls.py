
from django.contrib import admin
from django.urls import path
from mahsolat.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('arayeshi/',arayeshi),
    path('behdashti/',behdashti),
    path('users/',users),
    path('contact/',contact),
    path('upanel/',upanel),
    path('logout/',lout),
    path('error/',error),
    path('register/',reg),
    path('success/',sc),





]
