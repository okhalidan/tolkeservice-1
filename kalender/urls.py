from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from kalender import views

urlpatterns=patterns('',
	url(r'^kt/$', login, {'template_name': 'login.html'}),
	url(r'^kalender/$', views.kalender, name='kalender'),
	url(r'^logout/$', logout, {'next_page' : '../kt/'}),
	url(r'^kalender/dag/(\d{4})/([^/]+)/(\d{1,2})/$', views.date, name='date'),
)

