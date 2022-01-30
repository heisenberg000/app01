"""app01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_book/', views.add_book),
    # path('find_books', views.find_books),
    # path('update_books', views.update_book),
    # re_path(r'^find_book/(?P<book_id>\d{1,2})/$', views.find_book, name='find_book'),
    # re_path(r'^del_book/(?P<book_id>\d{1,2})/$', views.del_book, name='del_book')

]
