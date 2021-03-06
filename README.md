![HZPP REST API](/media/hzpp_api_logo.png?raw=true)

## Why?

As frequent Croatian Railways user for everyday commuting from home to work and vice-versa, I wanted some quick, nicely formatted and easily accessible data source, for fun and educational purpose, to available trains, their departure times and seat reservations. Croatian Railways do not have any publicly open APIs for such purposes (such a shame if you consider the time we live in), so this little python app scrapes official webpage and its sources to return two types information for now: List of stations, list of trains available between to stations.

#### Notice to Croatian Railways staff:

This is my humble contribution to make public data more accessible to ones that deserve it, tax payers.
Intention of this application is not any type of hacking activity nor data thievery but greater public good!

For the ones who find this code helpful, feel free to use it in any way you wanna to. I'm always open for advice and possible cooperations. Cheers!

## Content

1. [Requirements](#requirements)
    1. [Python packages](#python-packages)
2. [Installation](#installation)
3. [Run locally](#run-locally)
4. [Run in production](#run-in-production)
5. [Endpoints](#endpoints)
    1. [GET: /stations](#get-stations)
    1. [GET: /trains](#get-trainsstart_idstation_iddestination_idstation_iddate2018-12-07)
6. [API specification](#api-specification)
7. [TODOs](#todos) 

## Requirements

* Python 3.7.0

### Python packages

* gunicorn 19.9.0
* eventlet 0.24.1
* hug 2.4.1
* requests 2.19.1
* beautifulsoup4 4.6.3
* demjson 2.2.4

## Installation

1. Navigate to root folder (where `requirements.txt` is located)
2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Run locally

1. Navigate to root folder (where `app.py` is located)
2. Use `gunicorn` for running application:
    
    ```
    gunicorn --reload app:__hug_wsgi__ --bind=0.0.0.0:8000 --workers=2 --timeout=120
    ```

    ##### Notice: `--reload` flag indicates that `gunicorn` restarts workers everytime you make changes in code

## Run in production

When running app in production consider using more than 2 workes, especially more than 1.
Also, `gunicorn` has issues with some deploy vendors (AWS and their ELBs) when using its default sync workers, so consider using `eventlet` or `gevent` workers. I did not notice any problems on any deployment vendors when I ran `5` `eventlet` workers, for example:

```
gunicorn app:__hug_wsgi__ --bind=0.0.0.0:8000 --workers=5 --timeout=120 --worker-class=eventlet
```

## Endpoints

### GET: /stations

#### Example response

```json
{
    "stations": 
        [
        ...
            {
                "id": 76260,
                "name": "Knin"
            },
            {
                "id": 78653,
                "name": "Komin"
            },
            {
                "id": 74407,
                "name": "Konjšćina"
            },
            {
                "id": 78801,
                "name": "Kopanica-Beravci"
            },
            {
                "id": 73160,
                "name": "Koprivnica"
            },
            {
                "id": 76411,
                "name": "Koprno"
            },
            {
                "id": 73704,
                "name": "Koreničani"
            },
        ...
        ]
}
```

### GET: /trains?start_id={station_id}&destination_id={station_id}&date=2018-12-07

#### Parameters

* `start_id` - required - id value of departure train station
* `destination_id` - required - id value of destination train station
* `date` - optional - default is current day - date of journey formated in `YYYY-MM-DD`

#### Example response

```json
{
    "trains": [
        {
            "time_departure": "04:44",
            "id": 970,
            "time_arrival": "06:24",
            "time_duration": "01:40",
            "count_transfer": 0
        },
        {
            "time_departure": "05:37",
            "id": 2202,
            "time_arrival": "07:06",
            "time_duration": "01:29",
            "count_transfer": 0
        },
        {
            "time_departure": "07:48",
            "id": 2204,
            "time_arrival": "09:18",
            "time_duration": "01:30",
            "count_transfer": 0
        },
        ...
    ]
}
```

## API specification

API specification is available on any not matched url of application (`hug` package goodie).
For example if you navigate locally to root (`http://localhost:8000/`) of app you will get json response of current available endpoints:

```json
{
  "404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
  "documentation": {
    "handlers": {
      "/stations": {
        "GET": {
          "examples": [
            "http://localhost:8000/stations"
          ],
          "outputs": {
            "format": "JSON (Javascript Serialized Object Notation)",
            "content_type": "application/json; charset=utf-8"
          }
        }
      },
      "/trains": {
        "GET": {
          "outputs": {
            "format": "JSON (Javascript Serialized Object Notation)",
            "content_type": "application/json; charset=utf-8"
          },
          "inputs": {
            "start_id": {
              "type": "A Whole number"
            },
            "destination_id": {
              "type": "A Whole number"
            },
            "date": {
              "type": "Basic text / string value",
              "default": ""
            }
          }
        }
      }
    }
  }
}
```

## TODOs

1. Reservation endpoint

    * For some trains there is a requirement of seat reservation, and hzpp.hr have this option in their official forms. Problem is that reservation form is available under sessioned requests with some kind of basket id in url, which was not successfully extracted till now

2. Tests

    * Application is dying for some test cases

3. CI runners

    * run tests on CI to show coverage

4. Dockerize

    * Make runnable Docker image of application

5. Trains endpoint upgrade
    
    * Support for more advanced filtering parameters, including: class, via, passengers number etc. filtering

6. Docstrings

    * Write methods docstrings
    
