from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'	

class Quiz(models.Model):
	username = models.CharField(max_length=100)
	#author = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='quiz_file')

	def __str__(self):
		return self.username
