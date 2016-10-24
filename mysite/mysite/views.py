from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

import urllib3
import json

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

def gjjcx(request):
	errors = []
	params = request.POST
	qryflag = 1
	print('params:',params)
	for k,v in params.items():
		print("param:%s=%s" % (k,v))

	print('connect gjjcx...')
	
	verify = params.get('verify','')
	url_str = 'http://app.szzfgjj.com:7001/accountQuery?accnum=20780739155&certinum=431003199406012214&qryflag=1&verify='+verify;
	# cx_data = {'accnum':'20780739155','certinum':'431003199406012214','qryflag':'1','verify':verify}
	http = urllib3.PoolManager()
	r = http.request('GET',url_str)
	print('result：',r.data.decode('utf-8'))

	return render_to_response('gjjcx.html',locals())

