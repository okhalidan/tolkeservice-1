from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from kalender.models import AppointmentForm, Appointment
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage

import calendar
import datetime


CLOCK = ['00.30', '01.00', '01.30', '02.00', '02.30', '03.00', '03.30', '04.00', '04.30', '05.00', 
	 '05.30', '06.00', '06.30', '07.00', '07.30', '08.00', '08.30', '09.00', '09.30', '10.00',
	 '10.30', '11.00', '11.30', '12.00', '12.30', '13.00', '13.30', '14.00', '14.30', '15.00',
	 '15.30', '16.00', '16.30', '17.00', '17.30', '18.00', '18.30', '19.00', '19.30', '20.00',
	 '20.30', '21.00', '21.30', '22.00', '22.30', '23.00', '23.30', '00.00', ]



def kalender(request, month_number, year):
	month_lst = ['Januar', 'Februar', 'Marts', 'April', 'Maj', 'Juni', 'Juli',
		     'August', 'September', 'Oktober', 'November', 'December']

	month_number = int(month_number)
	year = int(year)
	today = datetime.date.today()
	today_tuple = today.timetuple()
	today_year = today_tuple[0]
	today_month = today_tuple[1]
	month_name = month_lst[month_number - 1]
	cal = calendar.Calendar()
	days_of_month = cal.itermonthdays(year, month_number)
	weeks = [[]]
	week_counter = 0

	if month_number > 0 and month_number < 12:
		next_month = month_number + 1
	else:
		next_month = 1
		
	if month_number == 12:
		next_year = year + 1
	else: 
		next_year = year

	if year == today_year and month_number == today_month:
		prev_month = -1
		prev_year = -1
	else:
		if month_number < 13 and month_number > 1:
			prev_month = month_number - 1
		else:
			prev_month = 12

		if month_number == 1:
			prev_year = year - 1
		else:
			prev_year = year
	


	for day in days_of_month: 
		if len(weeks[week_counter]) % 7 != 0:
			weeks[week_counter].append(day)
		else:
			weeks.append([])
			week_counter += 1
			weeks[week_counter].append(day)
	
	return render(request, 'kalender.html', {'weeks' : weeks, 'year' : year, 'month_name' : month_name, 
						 'month_number' : month_number, 'next_month' : next_month, 
				  	         'next_year' : next_year, 'prev_month' : prev_month, 
						 'prev_year' : prev_year})





def makeDay(appLst, user):
	appDay = []

	for clock in CLOCK:
		cl = datetime.time(int(clock[:2]), int(clock[3:]))
		appDay.append(cl)
		
	lst=[]
	for cl in appDay:
		for app in appLst:
			if cl >= app.start and cl < app.end and str(app.name) != str(user):
				lst.append((cl, "Optaget", str(app.name), app.pk))
				break
			elif cl >= app.start and cl < app.end and str(app.name) == str(user):
				lst.append((cl, str(app.place), str(app.name), app.pk))				
				break
			else:
				continue
		if len(lst)==0 or  lst[-1][0] != cl:
			lst.append((cl, "", "", ""))

	appD=[]
	for i in range(len(lst)):
		clStr = lst[i][0].strftime("%H:%M")
		appD.append({'clock':clStr,'place':lst[i][1],'name':lst[i][2], 'pk': lst[i][3]})
	
	return appD




def date(request, year, month, day):
	clock_lst = ['00.30', '01.00', '01.30', '02.00', '02.30', '03.00', '03.30', '04.00', '04.30', '05.00', '05.30', '06.00','06.30','07.00','07.30', '08.00', '08.30', '09.00', '09.30', '10.00', '10.30', '11.00', '11.30', '12.00', '12.30', '13.00', '13.30', '14.00', '14.30', '15.00', '15.30', '16.00', '16.30', '17.00', '17.30', '18.00', '18.30', '19.00', '19.30', '20.00', '20.30', '21.00', '21.30', '22.00', '22.30', '23.00', '23.30', '24.00', ]

	month_lst = ['Januar', 'Februar', 'Marts', 'April', 'Maj', 'Juni', 'Juli',
		     'August', 'September', 'Oktober', 'November', 'December']

	appDate=datetime.date(int(year), month_lst.index(month)+1, int(day))
	appLst=Appointment.objects.filter(date=appDate).order_by('start')
 	monthnr = month_lst.index(month)+1	
	errors=[]
        startLst = []
	endLst = []
	form=AppointmentForm()
	md = makeDay(appLst, request.user)
	strdate= appDate.strftime("%d/%m/%Y") 

	if request.method=='POST':
		if request.POST.get('pk'):
			Appointment.objects.filter(pk=request.POST['pk']).delete()
			return HttpResponseRedirect('/tolk/kalender/dag/%s/%s/%s' % (year, month, day))
		elif request.POST['start'] >= request.POST['end']:
			errors.append('Start skal komme fr end')
		else:
			startLst = Appointment.objects.filter(start=request.POST['start'])
			endLst = Appointment.objects.filter(end=request.POST['end'])

			form=AppointmentForm(request.POST)
			form=Appointment(date=appDate, start=request.POST['start'], end=request.POST['end'], 
			                 place=request.POST['place'], adress=request.POST['adress'], 
					 building=request.POST['building'], floor=request.POST['floor'], 
					 zipcode=request.POST['zipcode'], city=request.POST['city'], 
					 telephone=request.POST['telephone'], email=request.POST['email'], 
					 message=request.POST['message'], name=request.POST['name'])
			form.save()
			
			email = EmailMessage('Bekraeftigelse fra K. Translation', 
			'Du har lavet en aftale hos K. Translation.\n Date: %s \n Start: %s \nSlut: %s \n Sted: %s' % (strdate, request.POST['start'], request.POST['end'], request.POST['place']), to=['morten.trolle@gmail.com'])
			email.send()
			return HttpResponseRedirect('/tolk/kalender/dag/%s/%s/%s' % (year, month, day))
	else:
		form = AppointmentForm()
	
	return render(request, 'date.html', {'errors':errors, 'st':startLst,'e':endLst, 'd':appDate, 'form' : form, 'year' : year, 'month' : month, 'md':md,'monthnr':monthnr, 'day' : day, 'clock_lst' : clock_lst, 'appLst':appLst, 'user':str(request.user)})













