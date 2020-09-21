from django.db import models


class Feed(models.Model):
	url = models.URLField(max_length=200, blank=False, null=False)
	title = models.CharField(max_length=32, blank=False, null=False)
	icon = models.CharField(max_length=200, default='', blank=True)
	created_date = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return str(self.title)

	class Meta:
		ordering = ('-id',)


