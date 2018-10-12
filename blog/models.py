from django.db import models

# Create your models here.
class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=255)
	body = models.TextField(max_length=5000)
	pub_date = models.DateTimeField()

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
