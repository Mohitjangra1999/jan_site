from django.shortcuts import render
from .models import Book
from django.http import  HttpResponse
from django.template import loader

def index(request):
    all_books = Book.objects.all()
    temp = loader.get_template("books/index.html")
    cont = {
        "all_books": all_books
    }
    return HttpResponse(temp.render(cont, request))

def details(request,book_id):
    return HttpResponse("<h1>You requested info for book " + str(book_id) +"</h1>")

