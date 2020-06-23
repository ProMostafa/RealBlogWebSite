from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Article(models.Model):
	author=models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE,
		)
	title=models.CharField(max_length=200)
	text=models.TextField()
	comment=models.TextField(default='No Comment')
	date=models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title

		# when Submite any form reverse to home page  
	def get_absolute_url(self):
		return reverse('home')



'''
class Comment(models.Model):

	post=models.ForeignKey(
		'Article.id',
		on_delete=models.CASCADE,
		)
	comment=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	def __str__(self):
		return "Name {} ,comment {}".format(self.author,self.comment)

'''


