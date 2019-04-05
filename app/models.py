# MIT License

# Copyright (c) Justin James Gonzales, Martin Thomas Saliba, Brent Zaguirre

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# “This is a course requirement for CS 192 Software Engineering II under the supervision of 
# Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, 
# University of the Philippines, Diliman for the AY 2015-2016”.

# ---------------------------------------------------------------------------------------------

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=30, blank=True)
    mobile_number = models.CharField(max_length=13, blank=True)
    user_type = models.CharField(max_length=50, blank=False, default="Buyer")
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class ORG(models.Model):
	name = models.CharField(max_length=20, unique=True)
	user= models.ForeignKey(User, on_delete="models.CASCADE")
	desc = models.TextField(max_length=100)
	location = models.CharField(max_length=30, blank=True)
	mobile_number = models.CharField(max_length=13, blank=True)
	rating = models.ForeignKey('star_ratings.Rating', on_delete=models.CASCADE,default=6)
	'''
	def save(self, *args, **kwargs):
		print(self.user.profile.user_type)
		if not self.rating and self.user.profile.user_type=="Buyer":
			self.rating = star_ratings.Rating.objects.create()
		super(ORG, self).save(*args, **kwargs)'''
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('app-orgs')

class IGP(models.Model):
	item = models.CharField(max_length=100)
	org = models.ForeignKey(ORG, on_delete=models.CASCADE)
	itype = models.CharField(max_length=100)
	price = models.FloatField(null=True, blank=True, default=None)
	date_posted = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='images', blank=True)
	view = models.IntegerField(default=0)
	rating = models.ForeignKey('star_ratings.Rating',on_delete=models.CASCADE,default=6)
	def __str__(self):
		return self.item
	def get_absolute_url(self):
		return reverse('app-igps')