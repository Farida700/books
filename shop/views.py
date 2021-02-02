from django.shortcuts import render, HttpResponse, redirect
from .models import Books

# Create your views here.


def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def newbooks(request):
    book_detail = Books.objects.all()
    return render(request, {"books_detail.html": book_detail})

def add_book(request):
    if request.method=='POST':
       title = request.POST['book_title']
       subtitle = request.POST['book_subtitle']
       description = request.POST['book_decscription']
       price = request.POST['book_price']
       genre = request.POST['book_genre']
       author = request.POST['book_author']
       year = request.POST['book_year']
       books = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
       books.save()
       return redirect(newbooks)

def delete_todo(request, id):
    todo = Books.objects.get(id=id)
    todo.delete()
    return redirect(newbooks)

def unmark_todo(request, id):
    todo = Books.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(newbooks)

def mark_todo(request, id):
    todo = Books.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(newbooks)

def book_detail(request, id):
    books_list=Books.objects.get(id=id)
    return render(request, "books_detail.html", {"books_list": books_list})

