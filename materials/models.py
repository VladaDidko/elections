from django.db import models
from PIL import Image


# Create your models here.
class Member(models.Model):
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	img = models.ImageField(upload_to='member_pics')
	position = models.CharField(max_length=40)
	info = models.CharField(max_length=120)

	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)
	# 	img = Image.open(self.img.path)
	# 	output_size = (300, 300)
	# 	img.thumbnail(output_size)
	# 	img.save(self.img.path)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		image = Image.open(self.img.path)
		resized_image = image.resize((200, 200), Image.ANTIALIAS)
		resized_image.save(self.img.path)