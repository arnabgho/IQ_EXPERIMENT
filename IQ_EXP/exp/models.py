from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Response(models.Model):
	name=models.CharField(max_length=100)
	date=models.DateField()
	age=models.IntegerField()
	question=models.CharField(max_length=100)
	answer=models.IntegerField()
	set_id=models.IntegerField()
	class_id=models.IntegerField()	
	def __unicode__(self):
		return self.name

class Scores(models.Model):
	name=models.CharField(max_length=100)
	date=models.DateField()
	age=models.IntegerField()
	set_id=models.IntegerField()
	score=models.IntegerField()
	class_id=models.IntegerField()	
	def __unicode__(self):
		return self.name

class Sets(models.Model):
	set_text=models.CharField(max_length=100)

	def __unicode__(self):
		return self.set_text
