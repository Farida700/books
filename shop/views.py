from django.shortcuts import render, HttpResponse

# Create your views here.


def books(request):
    return render(request, "books.html")