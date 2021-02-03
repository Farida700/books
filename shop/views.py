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
    title = form['book_title']
    subtitle = form['book_subtitle']
    description = form['book_decscription']
    price = form['book_price']
    genre = form['book_genre']
    author = form['book_author']
    year = form['book_year']
    books = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    books.save()
    return redirect(books)

def delete_books(request, id):
    books = Book.objects.get(id=id)
    books.delete()
    return redirect(books)

def unmark_books(request, id):
    books = Book.objects.get(id=id)
    books.is_favorite = False
    books.save()
    return redirect(books)

def mark_books(request, id):
    books = Book.objects.get(id=id)
    books.is_favorite = True
    books.save()
    return redirect(books)

def close_books(request, id):
    books = Book.objects.get(id=id)
    books.is_closed = not books.is_closed
    books.save()
    return redirect(books)

def books_detail(request, id):
    books = Book.objects.filter(id=id)
    return render(request, "books_detail.html", {"books_list": mybook})

