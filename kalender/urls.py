from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from kalender import views
import datetime

TODAY = datetime.date.today()
TODAY_TUPLE = TODAY.timetuple()
YEAR = TODAY_TUPLE[0]
MONTH = TODAY_TUPLE[1]

urlpatterns=patterns('',
	url(r'^kt/$', login, {'template_name':'login.html', 'extra_context':{'year':YEAR, 'month':MONTH}}),
	#url(r'^kalender/$', views.kalender),
	url(r'^kalender/(\d{1,2})/(\d{4})/$', views.kalender),
	url(r'^logout/$', logout, {'next_page':'../kt/'}),
	url(r'^kalender/dag/(\d{4})/([^/]+)/(\d{1,2})/$', views.date),
)

