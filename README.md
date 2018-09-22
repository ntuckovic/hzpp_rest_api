![HZPP REST API](/media/hzpp_api_logo.png?raw=true)

Rest API for hzpp.hr - passengers transfers

## Why?

As frequent Croatian Railways user for everyday communting from home to work and vice-versa, I wanted some quick, nicely formatted and easily accesible data source, for fun and educational purpose, to available trains, their departure times and seat reservations. Croatian Railways do not have any publicly open APIs for such purposes (such a shame if you consider time when we are living), so this little python app scrapes official webpage and its sources to return two types information for now: List of stations, list of trains available between to stations.

#### One notice to Croatian Railways employees:

This is my humble contribution to make public data more accessible to its public, to one that is making money for your salaries.

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


