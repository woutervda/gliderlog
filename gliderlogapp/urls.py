from django.conf.urls import patterns, include, url
from django.views.generic import FormView
from gliderlogapp.models import Registration

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('gliderlogapp.views',
    url(r'^$','index'),
	# url(r'^entry/$','entry'),
)