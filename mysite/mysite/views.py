from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

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
	print(">>>>>locals:",locals())
	return render_to_response('hours_ahead.html',locals())

