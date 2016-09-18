from django.shortcuts import render_to_response
from books.models import Book
from django.http import HttpResponse

# Create your views here.
def book_home(request):
	books = Book.objects.order_by('publication_date')
	meta = request.META
	header_dv = meta.items()
	for (k,v) in header_dv:
		print('header[%s]:%s' %(k,v))

	return render_to_response('book_home.html',{'books':books,'header_dv':header_dv,'meta':meta })
	
def search_form(request):
	return render_to_response('search_form.html')

def search_do(request):
	params = request.GET
	for k,v in params.items():
		print("param:%s=%s" % (k,v))

	q = params.get('q')
	if(q!=None):
		books = Book.objects.filter(title__icontains=q)
		return render_to_response('search_results.html',{'books':books,'query':q})
		message = 'You searched for: %r' % params['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
