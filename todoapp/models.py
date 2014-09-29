from django.db import models

class Todo(models.Model):
	author = models.CharField(max_length=100, default='Incognito')
	title = models.CharField(max_length=255)
	text = models.TextField()
	time = models.DateTimeField()
	deadline = models.DateTimeField()
	isdone = models.BooleanField(default=False) 