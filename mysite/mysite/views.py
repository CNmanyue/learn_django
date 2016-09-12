from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

current_section_class = "include->nav.html"
def hello(request):
	return HttpResponse("Hello world!")

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except Exception as e:
		# raise e
		print('Exception!!!')
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	# return render_to_response('hours_ahead.html',{'offset':offset,'dt':dt})
	current_section = "include->nav.html"
	print(">>>>>locals:",locals())
	return render_to_response('hours_ahead.html',locals())

def book_list(request):
	books = Book.objects.order_by('name')
	return render_to_response('book_list.html',{'books':books})
	