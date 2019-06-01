import requests
import json
import tkinter as tk

weather_root=tk.Tk()
weather_root.title('WeatherApp')
weather_root.iconbitmap('Weather.ico')


'''
def WeatherAppFunc():
     api_request=requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=3c7f9cd251791d68e63bd8608d798fdb')

     api=json.loads(api_request.content)
     print('City           ',api['city']['name'])
     for i in range(40):
         print('Temprature::',api['list'][i]['main']['temp'])
         print('Minimum Temprature::',api['list'][i]['main']['temp_min'])
         print('Maximum Temprature::',api['list'][i]['main']['temp_max'])
         print('Pressure::',api['list'][i]['main']['pressure'])
         print('Sea_level::',api['list'][i]['main']['sea_level'])
         print('Date        ',api['list'][i]['dt_txt'])
         print(api['list'][i]['weather'][0]['main']+'      '+api['list'][i]['weather'][0]['description'])
         print('Icon        ',api['list'][i]['weather'][0]['icon'])

'''
def WeatherAppFunc():
    api_request=requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=3c7f9cd251791d68e63bd8608d798fdb')
    api=json.loads(api_request.content)


    city_name=tk.Label(weather_root,text=api['city']['name'],bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    city_name.grid(row=0,column=0,columnspan=30,sticky='nesw')

    city_temp=tk.Label(weather_root,text='Temprature',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    city_temp.grid(row=1,column=0,sticky='nesw')
    city_min_temp=tk.Label(weather_root,text='Min-Temp',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    city_min_temp.grid(row=1,column=1,sticky='nesw')
    city_max_temp=tk.Label(weather_root,text='Max-Temp',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2,)
    city_max_temp.grid(row=1,column=2,sticky='nesw')
    city_pressure=tk.Label(weather_root,text='Pressure',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    city_pressure.grid(row=1,column=3,sticky='nesw')
    city_sea_level=tk.Label(weather_root,text='Sea-Level',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    city_sea_level.grid(row=1,column=4,sticky='nesw')
    city_cloud_status=tk.Label(weather_root,text='Cloud-Status',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    city_cloud_status.grid(row=1,column=5,sticky='nesw')
    city_rain_status=tk.Label(weather_root,text='Rain-Staus',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    city_rain_status.grid(row=1,column=6,sticky='nesw')
    date=tk.Label(weather_root,text='Date',bg='#003b9b',fg='white',height=1,font=('Verdana',15,'bold'),bd=2)
    date.grid(row=1,column=7,sticky='nesw')
    for i in range(2,20):
        city_temp=tk.Label(weather_root,text=api['list'][i]['main']['temp'],height=1,font=('Verdana',15,'bold'),bd=2)
        city_temp.grid(row=i,column=0,sticky='nesw')
        city_min_temp=tk.Label(weather_root,text=api['list'][i]['main']['temp_min'],height=1,font=('Verdana',15,'bold'),bd=2)
        city_min_temp.grid(row=i,column=1,sticky='nesw')
        city_max_temp=tk.Label(weather_root,text=api['list'][i]['main']['temp_max'],height=1,font=('Verdana',15,'bold'),bd=2)
        city_max_temp.grid(row=i,column=2,sticky='nesw')
        city_pressure=tk.Label(weather_root,text=api['list'][i]['main']['pressure'],height=1,font=('Verdana',15,'bold'),padx=2,bd=2)
        city_pressure.grid(row=i,column=3,sticky='nesw')
        city_sea_level=tk.Label(weather_root,text=api['list'][i]['main']['sea_level'],height=1,font=('Verdana',15,'bold'),bd=2)
        city_sea_level.grid(row=i,column=4,sticky='nesw')
        city_cloud_status=tk.Label(weather_root,text=api['list'][i]['weather'][0]['main'],height=1,font=('Verdana',15,'bold'),bd=2)
        city_cloud_status.grid(row=i,column=5,sticky='nesw')
        city_rain_status=tk.Label(weather_root,text=api['list'][i]['weather'][0]['description'],height=1,font=('Verdana',15,'bold'),bd=2)
        city_rain_status.grid(row=i,column=6,sticky='nesw')
        date=tk.Label(weather_root,text=api['list'][i]['dt_txt'],height=1,font=('Verdana',15,'bold'),bd=2)
        date.grid(row=i,column=7,sticky='nesw')

WeatherAppFunc()
update_buttun=tk.Button(weather_root,text='Update',font=('Verdana',15,'bold'),command=WeatherAppFunc,bg='#003b9b',bd=2)
update_buttun.grid(row=21,column=7,sticky='sw')


weather_root.mainloop()
