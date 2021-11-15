from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	is_organisor = models.BooleanField(default=True)
	is_agent = models.BooleanField(default=False)

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username



class Agent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.email

class Lead(models.Model):
	first_name 		= models.CharField(max_length=20)
	last_name 		= models.CharField(max_length=20)
	age 			= models.IntegerField(default=0)
	organisation 	= models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
	agent 			= models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
	category 		= models.ForeignKey("Category", null=True, related_name="leads", blank=True, on_delete=models.SET_NULL)	 
	

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Category(models.Model):
	name = models.CharField(max_length=30)
	organisation 	= models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

def post_user_created_signal(sender, instance, created, **kwargs):
	print(f'wartosc instance to {instance} created {created}')
	if created:
		UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)