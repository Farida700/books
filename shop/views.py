from django.shortcuts import render, HttpResponse, redirect
from .models import Books

# Create your views here.
def homepage(request):
    return render(request, "books.html")

def books(request):
    book_list = Books.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def add_books(request):
    form = request.POST
    title = request.POST['book_title']
    subtitle = request.POST['book_subtitle']
    description = request.POST['book_decscription']
    price = request.POST['book_price']
    genre = request.POST['book_genre']
    author = request.POST['book_author']
    year = request.POST['book_year']
    books = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    books.save()
    return redirect(books)

def delete_books(request, id):
    todo = Book.objects.get(id=id)
    todo.delete()
    return redirect(books)

def unmark_books(request, id):
    todo = Book.objects.get(id=id)
    books.is_favorite = True
    todo.save()
    return redirect(books)

def mark_books(request, id):
    todo = Book.objects.get(id=id)
    books.is_favorite = False
    todo.save()
    return redirect(books)

def close_books(request, id):
    todo = Book.objects.get(id=id)
    books.is_closed = not books.is_closed
    todo.save()
    return redirect(books)

def books_detail(request, id):
    books_list=Book.objects.get(id=id)
    return render(request, "books_detail.html", {"books_list": books_list})

