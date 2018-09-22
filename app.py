import hug
import requests
import json
import demjson

from falcon import HTTP_400
from datetime import datetime
from bs4 import BeautifulSoup


api = hug.API(__name__)

hzpp_url = 'http://www.hzpp.hr'
hzpp_sales_url = 'https://prodaja.hzpp.hr/hr'
stations_endpoint_template = '/CorvusTheme/Timetable/Locs'
trains_endpoint_template = '/Ticket/Journey?StartId={0}&DestId={1}&DepartureDate={2}&DirectTrains=True'
train_row_cell_parse_keys = {
    0: 'time_departure',
    1: 'id',
    2: 'time_arrival',
    3: 'time_duration',
    4: 'count_transfer'
}
reservations_endpoint_template = '/Ticket/Journey'

@hug.get('/stations')
def get_stations():
    stations_url = f'{hzpp_url}{stations_endpoint_template}'

    response = requests.get(stations_url)
    stations_str = response.text.replace('var locs = ', '')
    stations_lists = demjson.decode(stations_str)
    stations = [
        { 'id': int(station[0]), 'name': station[1] } for station in stations_lists
    ]

    return {
        'stations': stations
    }

@hug.get('/trains')
def get_trains(
        response,
        start_id: hug.types.number,
        destination_id: hug.types.number,
        date: hug.types.text = '',
    ):
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    
    trains_endpoint = trains_endpoint_template.format(start_id, destination_id, date)
    trains_url = f'{hzpp_sales_url}{trains_endpoint}'

    response = requests.get(trains_url)
    soup = BeautifulSoup(response.text, features='html.parser')
    
    try:
        soup_train_rows = soup.find(
            'div', {'id' : 'tt_Result'}).find_all('div', {'class': 'item row'})
    except AttributeError:
        response.status = HTTP_400

        return {
            'errors': {
                'global': 'There are no scheduled trains between provided station ids!'
            }
        }

    trains = []
    for train_row in soup_train_rows:
        train_cells = train_row.find_all('div', {'class': 'col-1-7 cell'})
        train_data = {}

        for i, cell in enumerate(train_cells):
            cell_data = cell.getText()

            if i == 1 or i == 4:
                cell_data = int(cell_data)

            train_data[train_row_cell_parse_keys[i]] = cell_data

        trains.append(train_data)

    return {
        'trains': trains
    }
