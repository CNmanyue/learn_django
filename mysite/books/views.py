from django.shortcuts import render_to_response
from books.models import Book

# Create your views here.
def book_home(request):
	books = Book.objects.order_by('publication_date')
	return render_to_response('book_home.html',{'books':books})
	