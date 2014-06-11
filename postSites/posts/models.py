import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
from django import forms

class Form(forms.Form):
    content = forms.CharField(max_length=256)


class Post (models.Model):
	content = models.CharField(max_length=256)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <  now
	
	was_published_recently.admin_order_field='pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published Recently?'
	def __str__(self):
		return self.content

class Comment(models.Model):
	parent = models.ForeignKey(Post)
	content = models.CharField(max_length=256)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.content
