from django.db import models

class Stuff_card(models.Model):
	image = models.ImageField() 
	text = models.CharField(max_length=50)
	price = models.TextField()
	size = models.TextField()

	def __str__(self):
		return self.text 