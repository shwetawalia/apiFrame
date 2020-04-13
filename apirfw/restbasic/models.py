from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	mobile_name = models.IntegerField()
	profile_pic = models.ImageField(upload_to='Pics')
	date_of_birth = models.DateField(blank=True)

	def __str__(self):
		return self.user.username

# Create your models here.
