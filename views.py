from django.shortcuts import render
from django.http import HttpResponse

import calendar
import datetime

def kalender(request):
	
	month_lst = ['Januar', 'Februar', 'Marts', 'April', 'Maj', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'December']
	
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


def date(request, year, month, day):
	clock_lst = ['07.00', '08.00', '09.00', '10.00', '11.00', '12.00', '13.00', '14.00', '15.00', '16.00', '17.00', '18.00', '19.00', '20.00']

	return render(request, 'date.html', {'year' : year, 'month' : month, 'day' : day, 'clock_lst' : clock_lst})

