from django.db import models



class Article(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	published=models.DateField(auto_now=True)
	category=models.CharField(max_length=100)
	image=models.ImageField(upload_to='profile_image', blank=True)
	optional_image=models.ImageField(upload_to='profile_image', blank=True)
	body_text=models.TextField(default=True, null=True)

	def __str__(self):
		return self.title