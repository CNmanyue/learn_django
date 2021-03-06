"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from mysite.views import *
from books.views import *
from contact.views import *
# from books import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(?P<offset>(\d)|(1\d)|(2[0-4]))/$',hours_ahead),
    url(r'^books/$',book_home),
    # url(r'^books/search-form/$',search_form),
    url(r'^books/search/$',search_do),
    url(r'^contact/$',contact),
    url(r'^contact/thanks/$',contact_thanks),
    url(r'^gjjcx/$',gjjcx),
]
