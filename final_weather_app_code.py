import datetime
import json
import urllib.request
import tkinter
from tkinter import *
import sys
import os
from tkinter import PhotoImage


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
    root = tkinter.Tk()
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


if __name__ == '__main__':
    try:
        city_name = input("Enter a city name:")
        data_output(data_organizer(data_fetch(url_builder(city_name))))
    except IOError:
        print('no internet')


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
if weatherid == '200':
    print('Rainy Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id3.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '201':
    print('Rainy Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id3.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '202':
    print('Rainy Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id3.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '230':
    print('Rainy Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id3.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '231':
    print('Rainy Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id3.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '232':
    print('Rainy Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id3.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # thunderstorm

if weatherid == '210':
    print('Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id4.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '211':
    print('Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id4.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '212':
    print('Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id4.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '221':
    print('Thunderstorm')
    weathertype = tkinter.PhotoImage(file="id4.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # light rain

if weatherid == '300':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '301':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '302':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '310':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '311':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '312':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '313':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '314':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '321':
    print('Light Rain')
    weathertype = tkinter.PhotoImage(file="id5.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # rain
if weatherid == '500':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '501':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '502':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '503':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '504':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '511':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '520':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '521':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '522':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '531':
    print('Rain')
    weathertype = tkinter.PhotoImage(file="id6.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # snow
if weatherid == '600':
    print('Snow')
    weathertype = tkinter.PhotoImage(file="id7.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '601':
    print('Snow')
    weathertype = tkinter.PhotoImage(file="id7.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '602':
    print('Snow')
    weathertype = tkinter.PhotoImage(file="id7.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '620':
    print('Snow')
    weathertype = tkinter.PhotoImage(file="id7.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '621':
    print('Snow')
    weathertype = tkinter.PhotoImage(file="id7.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '622':
    print('Snow')
    weathertype = tkinter.PhotoImage(file="id7.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # sleet
if weatherid == '611':
    print('Sleet')
    weathertype = tkinter.PhotoImage(file="id8.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '612':
    print('Sleet')
    weathertype = tkinter.PhotoImage(file="id8.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '615':
    print('Sleet')
    weathertype = tkinter.PhotoImage(file="id8.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '616':
    print('Sleet')
    weathertype = tkinter.PhotoImage(file="id8.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # tornado
if weatherid == '781':
    print('TORNADO')
    weathertype = tkinter.PhotoImage(file="id9.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '900':
    print('TORNADO')
    weathertype = tkinter.PhotoImage(file="id9.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # sunny
if weatherid == '800':
    print('Sunny/Clear')
    weathertype = tkinter.PhotoImage(file="id10.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '951':
    print('Sunny/Clear')
    weathertype = tkinter.PhotoImage(file="id10.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # lightly cloudy
if weatherid == '801':
    print('Sunny with some clouds')
    weathertype = tkinter.PhotoImage(file="id11.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # mid cloudy
if weatherid == '802':
    print('Cloudy')
    weathertype = tkinter.PhotoImage(file="id12.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

    # heavy cloudy
if weatherid == '803':
    print('Lots of clouds')
    weathertype = tkinter.PhotoImage(file="id13.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

if weatherid == '804':
    print('Lots of clouds')
    weathertype = tkinter.PhotoImage(file="id13.gif")
    typew = tkinter.Label(image=weathertype)
    typew.grid(row=0, column=6, columnspan=3, rowspan=2, padx=5, pady=5)

root.mainloop()

