"""books URL Configuration

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
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", books, name="books"),
    path("add-books/", add_books, name="add_books"),
    path("delete-books/<id>", delete_books, name="delete_books"),
    path("unmark-books/<id>", unmark_books, name="unmark_books"),
    path("mark-books/<id>", mark_books, name="mark_books"),
    path("close-books/<id>/", close_books, name="close-books"),
    path("books-detail/<id>", books_detail, name="books_detail"),
]   +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
