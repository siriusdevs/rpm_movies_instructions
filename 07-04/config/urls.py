"""config URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.custom_main, name='main')
    #re_path(r'^$', views.main_page, name='main')
    #re_path(r'^$', views.render_dummy, name='main')
    #re_path(r'^$', views.redirection_page, name='main')
]

