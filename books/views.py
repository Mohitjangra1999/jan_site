from django.shortcuts import render
from .models import Book
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    all_books = Book.objects.all()

    context = {
        "all_books": all_books
    }
    return render(request,"books/index.html",context)

def details(request, book_id):
    return HttpResponse("<h1>You requested info for book " + str(book_id) +"</h1>")

