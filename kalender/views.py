from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from kalender.models import AppointmentForm, Appointment
from django.template import RequestContext

import calendar
import datetime

def kalender(request):
	month_lst = ['Januar', 'Februar', 'Marts', 'April', 'Maj', 'Juni', 'Juli',
		     'August', 'September', 'Oktober', 'November', 'December']
	
	today = datetime.date.today()
	today_tuple = today.timetuple()
	year = today_tuple[0]
	month_number = today_tuple[1]
	month = month_lst[month_number - 1]
	cal = calendar.Calendar()
	days_of_month = cal.itermonthdays(year, month_number)

	weeks = [[]]
	week_counter = 0

	for day in days_of_month: 
		if len(weeks[week_counter]) % 7 != 0:
			weeks[week_counter].append(day)
		else:
			weeks.append([])
			week_counter += 1
			weeks[week_counter].append(day)
	
	return render(request, 'kalender.html', {'weeks' : weeks, 'year' : year, 'month' : month})


def custom_proc(request):
	return{'user':request.user}


def date(request, year, month, day):
	clock_lst = ['07.00', '08.00', '09.00', '10.00', '11.00', '12.00', '13.00',
		     '14.00', '15.00', '16.00', '17.00', '18.00', '19.00', '20.00']

	month_lst = ['Januar', 'Februar', 'Marts', 'April', 'Maj', 'Juni', 'Juli',
		     'August', 'September', 'Oktober', 'November', 'December']

	appDate=datetime.date(int(year), month_lst.index(month)+1, int(day))
	appLst=Appointment.objects.filter(date=appDate).order_by('start')


	h=""
	if request.method=='POST':
		form=AppointmentForm(request.POST)
#		if form.is_valid():
#			h=""
		form=Appointment(date=appDate, start=request.POST['start'], end=request.POST['end'], 
			                 place=request.POST['place'], adress=request.POST['adress'], 
					 building=request.POST['building'], floor=request.POST['floor'], 
					 zipcode=request.POST['zipcode'], city=request.POST['city'], 
					 telephone=request.POST['telephone'], email=request.POST['email'], 
					 message=request.POST['message'], name=request.POST['name'])
		form.save()
		return HttpResponseRedirect('/tolk/kalender')  #/dag/%s/%s/%s' % (year, month, day))
#		else:
#			h=form.errors

	else:
		form = AppointmentForm()
		h=""
	
	return render(request, 'date.html', {'form' : form, 'year' : year, 'month' : month, 
		'day' : day, 'clock_lst' : clock_lst, 'h':h, 'appLst':appLst, 'user':request.user}, context_instance=RequestContext(request,processors=[custom_proc]))












