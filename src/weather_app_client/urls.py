from django.urls import path
from weather_app_client.views import CityWeatherView


urlpatterns = [
    path("data", CityWeatherView.as_view({"get": "list"})),
    path("trigger", CityWeatherView.as_view({"post": "create"})),
]