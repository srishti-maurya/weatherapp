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
from tkinter import *
import datetime
import json
import urllib.request
def convert_time(time):
    time_convert = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return time_convert
def forming_url(city_name):
    api_of_user = '**************************'
    unit_used = 'metric'
    model_of_api = 'http://api.openweathermap.org/data/2.5/weather?q='
    final_api_url = model_of_api + str(city_name) + '&mode=json&units=' + unit_used + '&APPID=' + api_of_user
    return final_api_url
def data_fetch(final_api_url):
    fetching_url = urllib.request.urlopen(final_api_url)
    getting_output = fetching_url.read().decode('utf-8')
    #print(getting_output)
    api_dict_model = json.loads(getting_output)
    # print(api_dict_model)
    fetching_url.close()
    return api_dict_model
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
    city_lab = Label(window, text="City:")
    city_lab.grid(row=5, column=0)
    city_data.config(text=data['city'])
    city_data.grid(row=5, column=1)
    country_data.config(text=data['country'])
    country_data.grid(row=5, column=2)
    temp_max.config(text=str(data['temp_max']) + temp_symbol)
    temp_max.grid(row=6, column=1)
    temp_min.config(text=str(data['temp_min']) + temp_symbol)
    temp_min.grid(row=6, column=2)
def fetch_data():
    city_name = city_entry.get()
    output_format(organizing_data(data_fetch(forming_url(city_name))))
try:
    window = tkinter.Tk(className='Weather Forecast')
    city_label = Label(window, text="Enter a city: ")
    city_label.grid(row=0, column=0)
    city_entry = Entry(window)
    city_entry.grid(row=0, column=1)
    show = Button(window, text="Show", command=fetch_data)
    show.grid(row=1, column=1)
    city_data = Label(window)
    country_data = Label(window)
    temp_max = Label(window)
    temp_min = Label(window)
    window.mainloop()
except IOError:
    print('no internet')

