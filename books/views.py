
from .models import Book
from django.views import generic
'''
def index(request):
    all_books = Book.objects.all()

    context = {
        "all_books": all_books,
    }
    return render(request, "books/index.html", context) '''

class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()
'''
def details(request, book_id):
    try:
        x = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("This book does not exists.")
    return render(request, "books/details.html", {"book": x}) '''

class DetailView(generic.DetailView):
    template_name = 'books/details.html'
    model = Book

