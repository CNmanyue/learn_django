from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def contact_old(request):
	errors = []
	if request.method == 'POST':
		# get方法指定了''为默认值，解决键丢失与空数据问题
		if not request.POST.get('subject',''):
			errors.append('Enter a subject.')
		if not request.POST.get('message',''):
			errors.append('Enter a message.')
		if not request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			# 这个函数包含四个必选参数：主题、正文、寄信人、收件人列表
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email','manyueonline@163.com'),
				['zhouxw@fadada.com']
			)
			# 若用户刷新一个包含post表单的页面，那么请求将重复发送，所以此处需要重定向！
			return HttpResponseRedirect('/contact/thanks/')

	return render_to_response('contact_form.html',{
		'errors':errors,
		'subject':request.POST.get('subject',''),
		'message':request.POST.get('message',''),
		'email':request.POST.get('email','')
		})
	
from contact.forms import ContactForm

def contact(request):
	if request.method=='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('emial','manyueonline@163.com'),
				['zhouxw@fadada.com']
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject':'I love your site!'}
		)

	return render_to_response('contact_form.html',{'form':form})

def contact_thanks(request):
	return render_to_response('contact_thanks.html')