from django.db import models

# Create your models here.

class user_register(models.Model):
	name=models.CharField(max_length=100, default='')
	email=models.CharField( max_length=100, default='')
	phone=models.CharField(max_length=32, default='')	
	password=models.CharField(max_length=32, default='')



class service_register(models.Model):
	servicename=models.CharField(max_length=100, default='')
	



class barber_register(models.Model):
	name=models.CharField(max_length=100, default='')
	email=models.CharField( max_length=100, default='')
	phone=models.CharField(max_length=32, default='')	
	password=models.CharField(max_length=32, default='')
	Image=models.ImageField(upload_to='image',default='')
	servicename = models.ForeignKey('service_register',on_delete=models.CASCADE)
	


class booking_register(models.Model):
	
	time=models.CharField(max_length=32, default='')
	date=models.CharField(max_length=32, default='')
	username = models.ForeignKey('user_register',on_delete=models.CASCADE)
	barbername = models.ForeignKey('barber_register',on_delete=models.CASCADE)
	status=models.CharField(max_length=32, default='Pending')
	




	



