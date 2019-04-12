from django.db import models

class WeatherAPI(models.Model):
	DATE = models.CharField(max_length = 8, primary_key = True)
	TMAX = models.FloatField()
	TMIN = models.FloatField()

	def __str__(self):
		return self.DATE