from django.db import models
from django.forms import ModelForm, TextInput, Textarea

#########################################

TIMES=(('6.00','6.00'),('6.30','6.30'),('7.00','7.00'),('7.30','7.30'))


class Appointment(models.Model):
	date = models.DateField()
	start = models.CharField(choices=TIMES,max_length=5)
	end = models.CharField(choices=TIMES, max_length=5)
	place = models.CharField(max_length=50)
	adress = models.CharField(max_length=75)
	building = models.CharField(blank=True, max_length=25)
	floor = models.CharField(blank=True, max_length=10)
	zipcode = models.IntegerField()
	city = models.CharField(max_length=35)
	telephone = models.CharField(blank=True, max_length=8)
	email = models.EmailField()
	message = models.TextField(blank=True)
	attach = models.FileField(upload_to='dokumenter', blank=True)

#	def __unicode__(self):
#		d=date.strftime("%d/%m/%y")
#		return u'Dato: %s \n Start: %s Slut: %s \n Sted: %s \n Address: %s \n Building: %s Floor: %d \n Postnr.: %d By: %s \n Telefon: %s \n Email: %s \n Andet: %s ' % (self.d,self.start, self.end, self.place, self.address, self.building, self.floor, self.zipcode, self.city, self.telephone, self.email, self.message)




class AppointmentForm(ModelForm):
	class Meta:
		model=Appointment
		fields=('start', 'end', 'place', 'adress', 'building', 'floor', 'zipcode', 'city', 'telephone', 'email','message','attach')
		widgets={'building':TextInput(attrs={'size':'2'}),
			 'zipcode':TextInput(attrs={'size':'2', 'maxlength':'4'}), 
			 'telephone':TextInput(attrs={'size':'4'}),
			 'floor':TextInput(attrs={'size':'2'}),
			 'message':Textarea(attrs={'cols':30, 'rows':4}),
			 }


