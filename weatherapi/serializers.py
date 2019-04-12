from rest_framework import serializers
from weatherapi.models import WeatherAPI

class WeatherSerializer(serializers.ModelSerializer):
	class Meta:
		model = WeatherAPI
		fields = ['DATE', 'TMAX', 'TMIN']

class DateSerializer(serializers.ModelSerializer):
	class Meta:
		model = WeatherAPI
		fields = ['DATE']