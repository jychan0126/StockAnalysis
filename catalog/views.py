from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()


    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/book_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
	    try:
	        book = Book.objects.get(pk=primary_key)
	    except Book.DoesNotExist:
	        raise Http404('Book does not exist')

	    # from django.shortcuts import get_object_or_404
	    # book = get_object_or_404(Book, pk=primary_key)
	    
	    return render(request, 'catalog/book_detail.html', context={'book': book})



class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/book_list.html'  # Specify your own template name/location


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
	    try:
	        author = Author.objects.get(pk=primary_key)
	    except Author.DoesNotExist:
	        raise Http404('Author does not exist')

	    # from django.shortcuts import get_object_or_404
	    # book = get_object_or_404(Book, pk=primary_key)
	    
	    return render(request, 'catalog/author_detail.html', context={'author': author})







