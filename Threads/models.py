from __future__ import unicode_literals

from django.db import models

from Login.models import User

# Create your models here.
class Thread(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.CharField(max_length=2000)
	author = models.ForeignKey(User)

	def __str__(self):
		return self.text

class Comment(models.Model):
	text = models.CharField(max_length=2000)
	author = models.ForeignKey(User)
	thread = models.ForeignKey(Thread)