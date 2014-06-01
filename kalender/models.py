from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.core.validators import validate_email

TIMES=(('06:00','06:00'),('06:30','06:30'),('07:00','07:00'),('07:30','07:30'),('08:00','08:30'),
	('09:00','09:00'),('09:30','09:30'),('10:00','10:00'),('10:30','10:30'),('11:00','11:00'),
	('11:30','11:30'),('12:00','12:00'),('12:30','12:30'),('13:00','13:00'),
	('13:30','13:30'),('14:00','14:00'),('14:30','14:30'))


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
		return u'Dato: %s \n Start: %s Slut: %s \n Sted: %s \n Address: %s \n Building: %s Floor: %s \n Postnr.: %d By: %s \n Telefon: %s \n Email: %s \n Andet: %s ' % (self.date,self.start, self.end, self.place, self.adress, self.building, self.floor, self.zipcode, self.city, self.telephone, self.email, self.message)




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


