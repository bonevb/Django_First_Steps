from django.db import models

# Create your models here.
class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=255)
	body = models.TextField(max_length=5000)
	pub_date = models.DateTimeField()

	def summary(self):
		return self.body[:100]
