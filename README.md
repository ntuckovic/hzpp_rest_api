![HZPP REST API](/media/hzpp_api_logo.png?raw=true)

Rest API for hzpp.hr - passengers transfers

## Why?

As frequent Croatian Railways user for everyday communting from home to work and vice-versa, I wanted some quick, nicely formatted and easily accesible data source, for fun and educational purpose, to available trains, their departure times and seat reservations. Croatian Railways do not have any publicly open APIs for such purposes (such a shame if you consider time when we are living), so this little python app scrapes official webpage and its sources to return two types information for now: List of stations, list of trains available between to stations.

#### Notice to Croatian Railways employees:

This is my humble contribution to make public data more accessible to its public, to ones that are earning money for your salaries.

If you find this offending because of any reason (considering this somekind of hacking acitivity or data thievery) then we do not have nothing to talk about. Please leave this repository link and never try to contact me. Go make yourself a coffee in your office and continue with your "work". It won't last much longer so enjoy while you can.

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
2. Install dependecies:

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

When running app in production consider using more than 2 workes, specially more than 1.
Also, `gunicorn` has issues with some deploy vendors (AWS and their ELBs) when using its defualt sync workers, so consider using `eventlet` or `gevent` workers. I did not notice anu problems on any deployment vendors when I runned `5` `eventlet` workers, for example:

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

### GET: /trains?start_id={station_id}&destination_id={station_id}

#### Example response



