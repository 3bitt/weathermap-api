import datetime
from rest_framework import status
import pytest
from tests.conftest import TestUser
from weather_app_client.models import CityWeather


@pytest.mark.django_db
class TestCityWeatherView:
    
    def test_post_city_weather_data(self, test_user: TestUser):
        response = test_user.trigger_city_weather_data_collection()
        assert response.status_code == status.HTTP_200_OK
        assert response.data["result"] == "Weather data collected"
        saved_data = CityWeather.objects.all()
        assert len(saved_data) == 1
        record_timestamp = saved_data[0].timestamp.strftime("%d/%m/%Y %H:%M:%S")
        assert  record_timestamp == datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  

        
    def test_get_city_weather_data(self, test_user: TestUser):
        response = test_user.trigger_city_weather_data_collection()
        assert response.status_code == status.HTTP_200_OK
        assert response.data["result"] == "Weather data collected"
        response = test_user.get_city_weather_data()
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
