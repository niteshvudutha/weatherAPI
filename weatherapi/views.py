from weatherapi.models import WeatherAPI
from weatherapi.serializers import WeatherSerializer, DateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets, permissions
from datetime import timedelta, datetime
import random


class DateListViewSet(viewsets.ViewSet):
	
	def list(self, request):
		queryset = WeatherAPI.objects.all()
		serializer = WeatherSerializer(queryset, many=True)
		newdata = {}
		response = []
		for i in range(len(serializer.data)):
			prDate = serializer.data[i]['DATE']
			data_get = {"DATE" : prDate}
			response.append(data_get)
		return Response(response)

	def create(self, request):
		serializer = WeatherSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DateViewSet(viewsets.ModelViewSet):
	queryset = WeatherAPI.objects.all()
	serializer_class = WeatherSerializer
	permission_classes = [
	permissions.AllowAny
	]

class ForecastViewSet(viewsets.GenericViewSet):
	queryset = WeatherAPI.objects.all()
	serializer_class = WeatherSerializer
	def retrieve(self, request, pk=None):
		DATE = pk
		DATE = str(DATE)
		startDate = datetime(int(DATE[:4]), int(DATE[4:6]), int(DATE[6:]))
		response = []
		newdata = {}
		for i in range(7):
			currDate = (startDate + timedelta(days = i)).strftime("%Y%m%d")
			serializer = self.get_serializer(WeatherAPI.objects.all().filter(DATE = currDate), many = True)
			if len(serializer.data)==0:
				j = 1
				TMAX = 0
				TMIN = 0
				while j < 4:
					prDate = datetime(int(currDate[:4])-1, int(currDate[4:6]), int(currDate[6:])).strftime("%Y%m%d")
					serializer = self.get_serializer(WeatherAPI.objects.all().filter(DATE = prDate), many = True)
					if len(serializer.data) == 0:
						TMAX = TMAX + round(random.uniform(50, 100), 2)
						TMIN = TMIN + round(random.uniform(2, 50), 2)
					else:
						TMAX = TMAX + serializer.data[0]["TMAX"]
						TMIN = TMIN + serializer.data[0]["TMIN"]
					j = j + 1
				newdata ={"DATE" : currDate, "TMAX" : round(TMAX/3,2), "TMIN" : round(TMIN/3,2)} 
				response.append(newdata)
			else:
				newdata = serializer.data
				response.append(newdata[0])	
		return Response(response)