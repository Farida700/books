from django.shortcuts import render, HttpResponse, redirect
from .models import Books

# Create your views here.


def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_todo(request):
    form = request.POST
    text = form["books_text"]
    books = Books(text=text)
    books.save()
    return redirect(books)