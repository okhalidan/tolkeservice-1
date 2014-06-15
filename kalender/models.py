from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.core.validators import validate_email
import datetime


TIMES=((datetime.time(00,30),'00:30'),(datetime.time(01,00),'01:00'),(datetime.time(01,30),'01:30'),
       (datetime.time(02,00),'02:00'),(datetime.time(02,30),'02:30'),(datetime.time(03,00),'03:00'),
       (datetime.time(03,30),'03:30'),(datetime.time(04,00),'04:00'),(datetime.time(04,30),'04:30'),
       (datetime.time(05,00),'05:00'),(datetime.time(05,30),'05:30'),(datetime.time(06,00),'06:00'),
       (datetime.time(06,30),'06:30'),(datetime.time(07,00),'07:00'),(datetime.time(07,30),'07:30'),
       (datetime.time(8,00),'08:00'),(datetime.time(8,30),'08:30'),(datetime.time(9,00),'09:00'),
       (datetime.time(9,30),'09:30'),(datetime.time(10,00),'10:00'),(datetime.time(10,30),'10:30'),
       (datetime.time(11,00),'11:00'),(datetime.time(11,30),'11:30'),(datetime.time(12,00),'12:00'),
       (datetime.time(12,30),'12:30'),(datetime.time(13,00),'13:00'),(datetime.time(13,30),'13:30'),
       (datetime.time(14,00),'14:00'),(datetime.time(14,30),'14:30'),(datetime.time(15,00),'15:00'),
       (datetime.time(15,30),'15:30'),(datetime.time(16,00),'16:00'),(datetime.time(16,30),'16:30'),
       (datetime.time(17,00),'17:00'),(datetime.time(17,30),'17:30'),(datetime.time(18,00),'18:00'),
       (datetime.time(18,30),'18:30'),(datetime.time(19,00),'19:00'),(datetime.time(19,30),'19:30'),
       (datetime.time(20,00),'20:00'),(datetime.time(20,30),'20:30'),(datetime.time(21,00),'21:00'),
       (datetime.time(21,30),'21:30'),(datetime.time(22,00),'22:00'),(datetime.time(22,30),'22:30'),
       (datetime.time(23,00),'23:00'),(datetime.time(23,30),'23:30'),(datetime.time(00,00),'00:00'))


class Appointment(models.Model):
	date = models.DateField()
	start = models.TimeField(choices=TIMES)
	end = models.TimeField(choices=TIMES)
	name = models.CharField(max_length=50)
	place = models.CharField(max_length=50)
	adress = models.CharField(max_length=75)
	building = models.CharField(blank=True, max_length=25)
	floor = models.CharField(blank=True, max_length=10)
	zipcode = models.IntegerField(blank=True, null=True)
	city = models.CharField(max_length=35)
	telephone = models.CharField(blank=True, max_length=8)
	email = models.EmailField(validators=[validate_email])
	message = models.TextField(blank=True)
	attach = models.FileField(upload_to='dokumenter', blank=True, null=True)

	def __unicode__(self):
		return u'Dato: %s \n Start: %s Slut: %s \n Sted: %s \n Address: %s \n Building: %s Floor: %s \n Postnr.: %d By: %s \n Telefon: %s \n Email: %s \n Andet: %s \n Name: %s ' % (self.date,self.start, self.end, self.place, self.adress, self.building, self.floor, self.zipcode, self.city, self.telephone, self.email, self.message, self.name)




class AppointmentForm(ModelForm):
	class Meta:
		model=Appointment
		fields=('start', 'end', 'name', 'place', 'adress', 'building', 'floor',
			'zipcode', 'city', 'telephone', 'email','message','attach')
		
		widgets={'building':TextInput(attrs={'size':'2'}),
			 'zipcode':TextInput(attrs={'size':'2', 'maxlength':'4'}), 
			 'telephone':TextInput(attrs={'size':'4'}),
			 'floor':TextInput(attrs={'size':'2'}),
			 'message':Textarea(attrs={'cols':30, 'rows':4}),
			 }


