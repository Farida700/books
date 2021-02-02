from django.shortcuts import render, HttpResponse
from .models import Books

# Create your views here.


def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})