#method 1
'''
import requests
req=requests.get(url='http://api.openweathermap.org/data/2.5/weather?id=1277333&APPID=44e132805ba20778ad6e1b48abf49b05')
data=req.json()
print(data['coord']['lat'])
print(data['weather'][0]['description'])
'''
#method 2
import tkinter
window=tkinter.Tk(className='my first project window')
window.mainloop()
import datetime
import json
import urllib.request
def convert_time(time):
    time_convert = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return time_convert
def forming_url(city_id):
    api_of_user = '44e132805ba20778ad6e1b48abf49b05'
    unit_used = 'metric'
    model_of_api = 'http://api.openweathermap.org/data/2.5/weather?id='

    final_api_url = model_of_api + str(city_id) + '&mode=json&units=' + unit_used + '&APPID=' + api_of_user
    return final_api_url
def data_fetch(final_api_url):
    fetching_url = urllib.request.urlopen(final_api_url)
    getting_output = fetching_url.read().decode('utf-8')
    print(getting_output)
    api_dict_model = json.loads(getting_output)
    print(api_dict_model)
    fetching_url.close()
def organizing_data(api_dict_model):
    data = dict(
        city=api_dict_model.get('name'),
        country=api_dict_model.get('sys').get('country'),
        temp=api_dict_model.get('main').get('temp'),
        temp_max=api_dict_model.get('main').get('temp_max'),
        temp_min=api_dict_model.get('main').get('temp_min'),
        humidity=api_dict_model.get('main').get('humidity'),
        pressure=api_dict_model.get('main').get('pressure'),
        sky=api_dict_model['weather'][0]['main'],
        sunrise=convert_time(api_dict_model.get('sys').get('sunrise')),
        sunset=convert_time(api_dict_model.get('sys').get('sunset')),
        wind=api_dict_model.get('wind').get('speed'),
        wind_deg=api_dict_model.get('deg'),
        dt=convert_time(api_dict_model.get('dt')),
        cloudiness=api_dict_model.get('clouds').get('all')
    )
    return data
def output_format(data):
    temp_symbol = '\xb0' + 'C'
    print('######################################')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], temp_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('######################################')
try:
    name_of_city= input("Enter a city name:")
    output_format(organizing_data(data_fetch(forming_url(1273294))))
except IOError:
    print('no internet')
