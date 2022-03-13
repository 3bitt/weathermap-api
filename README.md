# OpenWeatherMap API
API uses openweathermap.org open API to fetch weather data for city Warsaw and display it in json format.<br>
Fetched data is stored in local SQLite database.<br>
**After server is started API fetches data automatically every 5 minutes.**

---

## Requirements
1. OpenWeatherMap API key - can be obtained after registering in https://openweathermap.org (free)

---

## Setup instructions
1. Clone repository
2. Create virtual environment with Python 3.9.7 using your favourite tool (venv, conda, etc...)
3. Activate virtual environment
4. Install dependencies <br>
`pip install -r requirements.txt`
5. Create `.env` file in project root folder and fill in required variables <br>
SECRET_KEY - can be copy-pasted from example below <br>
WEATHERMAP_API_KEY - your openweathermap API key <br>
DEBUG - True or False

    **Example**
    ```
    SECRET_KEY=django-insecure-v_w%*rhD+=o43@ji2$%j)05-$@=to(i+g^ooiwf3@ow3m38f
    WEATHERMAP_API_KEY=<your_key>
    DEBUG=True
    ```
6. Initialize database <br>
`python src/manage.py migrate`
7. Run server <br>
`python src/manage.py runserver`<br>
**Notice:** After server is started API fetches data automatically every 5 minutes.
8. Have fun

### To run tests use `pytest` command

---
## Endpoints

Return list of data stored in local DB in json format 
> [GET] /data

Trigger data collection from openwathermap.org for city Warsaw and save it in local DB

> [POST] /trigger


### API documentation

Interactive web interface (no resource URL, just host root)
> [GET] /

documentation in json format

> [GET] /swagger.json

documentation in yaml format

> [GET] /swagger.yaml