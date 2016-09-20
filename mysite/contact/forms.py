from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100,min_length=8)
	email = forms.EmailField(required=False)
	message = forms.CharField(widget=forms.Textarea)
	# 下面是错误的
	# message = froms.Textarea()









