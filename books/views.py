
from .models import Book
from django.http import Http404
from django.shortcuts import render

def index(request):
    all_books = Book.objects.all()

    context = {
        "all_books": all_books,
    }
    return render(request, "books/index.html", context)


def details(request, book_id):
    try:
        x = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("This book does not exists.")
    return render(request, "books/details.html", {"book": x})

