from rest_framework.test import APIRequestFactory
import pytest
from unittest.mock import patch
from weather_app_client.models import CityWeather, WeatherDetail
from weather_app_client.views import CityWeatherView


class TestUser:
    def __init__(self):
        self.request = APIRequestFactory()
        
    def trigger_city_weather_data_collection(self):
        request = self.request.post("/trigger")
        view = CityWeatherView.as_view({"post": "create"})
        response = view(request)
        return response

    def get_city_weather_data(self):
        request = self.request.get("/data")
        view = CityWeatherView.as_view({"get": "list"})
        response = view(request)
        return response


@pytest.fixture
def test_user(city_weather_service_mock):
    return TestUser()

    
@pytest.fixture
def city_weather_service_mock():
    with patch("weather_app_client.weathermap_client.WeatherMapClient.get_weather_by_city") as mock:
        mock.return_value = {
            "coord": {"lon":21.0118,"lat":52.2298},
            "weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],
            "base":"stations",
            "main":{"temp":-2.31,"feels_like":-4.46,"temp_min":-5.1,"temp_max":0.44,"pressure":1031,"humidity":54},
            "visibility":10000,
            "wind":{"speed":1.54,"deg":130},
            "clouds":{"all":0},"dt":1647041921,
            "sys":{"type":2,"id":2032856,"country":"PL","sunrise":1647061068,"sunset":1647102834},
            "timezone":3600,
            "id":756135,
            "name":"Warsaw",
            "cod":200
        }
        yield mock


@pytest.fixture
def city_weather_db_mock():
    city_weather_data = {
        "coord": {
            "lon": 21.0118,
            "lat": 52.2298
        },
        "weather": [
            {
                "external_id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": -2.31,
            "feels_like": -4.46,
            "temp_min": -5.1,
            "temp_max": 0.44,
            "pressure": 1031,
            "humidity": 54
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.54,
            "deg": 130
        },
        "clouds": {
            "all": 0
        },
        "dt": 1647041921,
        "sys": {
            "type": 2,
            "id": 2032856,
            "country": "PL",
            "sunrise": 1647061068,
            "sunset": 1647102834
        },
        "timezone": 3600,
        "external_id": 756135,
        "name": "Warsaw",
        "cod": 200
    }
    city_weather_child = city_weather_data.pop("weather")
    city_weather = CityWeather.objects.create(**city_weather_data)
    WeatherDetail.objects.create(**city_weather_child[0], city_weather=city_weather)
    return city_weather
