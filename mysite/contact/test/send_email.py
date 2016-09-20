# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect

# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')


from django.core.mail import send_mail, BadHeaderError

try:
	send_mail(subject, message, from_email, ['admin@example.com'])
except Exception, e:
	raise e
