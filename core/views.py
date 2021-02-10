from django.shortcuts import render
from core.models import Book, Author, Genre, Series, Chapter
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models.functions import Length

# Create your views here.

def index(request):
    """View function for home page of site."""
    
    #Generate counts of main objects
    num_books = Book.objects.all().count()
    num_chapters = Chapter.objects.all().count()
    
    #Finished Books (status = 'f')
    num_finished_books = Book.objects.filter(status__exact='f').count()
    
    # The all() is implied by default.
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_chapters': num_chapters,
        'num_finished_books': num_finished_books,
        
    }
    
    return render(request, 'index.html', context=context)

class SeriesListView(generic.ListView):
    model = Series
    context_object_name = 'series_list'
    #queryset = Book.objects.filter(title__icontains='all')[:5]
    template_name = 'series/series_list.html'

class SeriesDetailView(generic.DetailView):
    model = Series
    paginate_by = 10
    context_object_name = 'series_detail'
    template_name = 'series/series_detail.html'

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    #queryset = Book.objects.filter(title__icontains='all')[:5]
    template_name = 'books/book_list.html'
    
class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 10
    template_name = 'books/book_detail.html'
    
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    initial = {'status': 'd'}
    
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    
class ChapterCreate(CreateView):
    model = Chapter
    fields = '__all__'
    initial = {'status': 'd'}
    
class ChapterUpdate(UpdateView):
    model = Chapter
    fields = '__all__'
    
class ChapterDelete(DeleteView):
    model = Chapter
    success_url = reverse_lazy('books')