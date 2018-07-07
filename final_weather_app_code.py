import datetime
import json
import urllib.request
import tkinter
from tkinter import *
import sys
import os
from tkinter import PhotoImage

import re
import requests
def next_day():
    r = requests.get(url='http://api.openweathermap.org/data/2.5/forecast?q=bangalore&mode=json&units=metric&APPID=44e132805ba20778ad6e1b48abf49b05')
    json_data= r.json()
    list_items= json_data['list']
    now = datetime.datetime.now()
    today=now.day
    list_indices =[]
    for items in list_items:
        matchObj=re.match(r"(\d+)-(\d+)-(\d+)",items['dt_txt'],re.M|re.I)
        list_indices.append(matchObj[3])

    for items in list_indices:
        if(int(items)==today):
            index=list_indices.index(items)
        break
    print(index)
    print(list_items[index])



def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_name):
    user_api = '44e132805ba20778ad6e1b48abf49b05'
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?q='

    full_api_url = api + str(city_name) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all'),
        typeid=raw_api_dict['weather'][0]['id'],
        wtype=raw_api_dict['weather'][0]['description']
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Weather ID: {}'.format(data['typeid']))
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')
    global weatherid
    weatherid = ('{}'.format(data['typeid']))
    weathertype = ('{}'.format(data['wtype']))
    print(weatherid)
    print(weathertype)

    weatherdata = (data['wtype'])
    weathid = (data['typeid'])
    wtempid = (data['temp'])
    wwindid = (data['wind'])
    citid = (data['city'])
    countryid = (data['country'])
    print("-------------------------------")

    print(str(citid) + ", " + str(countryid))
    global root
    ### Shifted root initialization
    root.geometry('900x515')
    root.title('Weather in:' + " " + str(citid) + ", " + str(countryid))
    root.wm_iconbitmap('wicon.ico')
    # temperature
    temp = tkinter.Label(text=str(wtempid) + "°C    ", font=("Courier", 28, 'bold'))
    temp.grid(row=0, column=5)
    # windspeed
    win = tkinter.Label(text=str(wwindid) + " MPH    ", font=("Courier", 28, 'bold'))
    win.grid(row=1, column=5)
    # weather condition text
    wean = tkinter.Label(text=" " + str(weatherdata), font=("Courier", 28, 'bold'))  # make weather update show here
    wean.grid(row=4, column=6)

###
def fetch_data():
    city_name = city_entry.get()
    data_output(data_organizer(data_fetch(url_builder(city_name))))
    print(weatherid)

    if weatherid == '200':
        print('Rainy Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id3.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '201':
        print('Rainy Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id3.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '202':
        print('Rainy Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id3.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '230':
        print('Rainy Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id3.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '231':
        print('Rainy Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id3.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '232':
        print('Rainy Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id3.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # thunderstorm

    if weatherid == '210':
        print('Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id4.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '211':
        print('Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id4.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '212':
        print('Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id4.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '221':
        print('Thunderstorm')
        weathertype = tkinter.PhotoImage(file="id4.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # light rain

    if weatherid == '300':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '301':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '302':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '310':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '311':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '312':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '313':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '314':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '321':
        print('Light Rain')
        weathertype = tkinter.PhotoImage(file="id5.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # rain
    if weatherid == '500':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '501':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '502':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '503':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '504':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '511':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '520':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype
    if weatherid == '521':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '522':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '531':
        print('Rain')
        weathertype = tkinter.PhotoImage(file="id6.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # snow
    if weatherid == '600':
        print('Snow')
        weathertype = tkinter.PhotoImage(file="id7.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '601':
        print('Snow')
        weathertype = tkinter.PhotoImage(file="id7.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '602':
        print('Snow')
        weathertype = tkinter.PhotoImage(file="id7.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '620':
        print('Snow')
        weathertype = tkinter.PhotoImage(file="id7.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '621':
        print('Snow')
        weathertype = tkinter.PhotoImage(file="id7.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '622':
        print('Snow')
        weathertype = tkinter.PhotoImage(file="id7.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # sleet
    if weatherid == '611':
        print('Sleet')
        weathertype = tkinter.PhotoImage(file="id8.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '612':
        print('Sleet')
        weathertype = tkinter.PhotoImage(file="id8.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '615':
        print('Sleet')
        weathertype = tkinter.PhotoImage(file="id8.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '616':
        print('Sleet')
        weathertype = tkinter.PhotoImage(file="id8.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # tornado
    if weatherid == '781':
        print('TORNADO')
        weathertype = tkinter.PhotoImage(file="id9.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '900':
        print('TORNADO')
        weathertype = tkinter.PhotoImage(file="id9.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # sunny
    if weatherid == '800':
        print('Sunny/Clear')
        weathertype = tkinter.PhotoImage(file="id10.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '951':
        print('Sunny/Clear')
        weathertype = tkinter.PhotoImage(file="id10.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

        # lightly cloudy
    if weatherid == '801':
        print('Sunny with some clouds')
        weathertype = tkinter.PhotoImage(file="id11.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype
        #
        # mid cloudy
    if weatherid == '802':
        print('Cloudy')
        weathertype = tkinter.PhotoImage(file="id12.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype


        # heavy cloudy
    if weatherid == '803':
        print('Lots of clouds')
        weathertype = tkinter.PhotoImage(file="id13.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

    if weatherid == '804':
        print('Lots of clouds')
        weathertype = tkinter.PhotoImage(file="id13.gif")
        typew.configure(image=weathertype)
        typew.image = weathertype

###


try:
    # city_name = input("Enter a city name:")
    ###
    root = tkinter.Tk()
    tempimg = tkinter.PhotoImage(file="id.gif")
    imgtemp = tkinter.Label(image=tempimg)

    # temp image
    tempimg = tkinter.PhotoImage(file="id.gif")

    tempweat = tempimg.zoom(3, 3)
    tempweat = tempimg.subsample(2, 2)

    imgtemp = tkinter.Label(image=tempweat)
    imgtemp.grid(row=0, column=0)

    # wind image
    windimg = tkinter.PhotoImage(file="id2.gif")

    windweat = windimg.zoom(3, 3)
    windweat = windimg.subsample(2, 2)

    imgwind = tkinter.Label(image=windweat)
    imgwind.grid(row=1, column=0)

    # img ids
    weathertype = tkinter.PhotoImage(file="id10.gif")
    global typew
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)



    city_label = tkinter.Label(root, text="Enter a city: ")
    city_label.grid(row=40, column=0)
    city_entry = tkinter.Entry(root)
    city_entry.grid(row=40, column=1)

    show = tkinter.Button(root, text="Show", command=fetch_data)
    show.grid(row=41, column=1)
    next_day = tkinter.Button(root, text=">", command=next_day)
    next_day.grid(row=45, column=1)


    root.mainloop()
    ###
    # data_output(data_organizer(data_fetch(url_builder(city_name))))
except IOError:
    print('no internet')
