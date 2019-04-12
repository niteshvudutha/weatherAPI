from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title = "WeatherAPI")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weatherapi.urls')),
    path('swagger/', schema_view),
    path('', include('APIInterface.urls')),
]
