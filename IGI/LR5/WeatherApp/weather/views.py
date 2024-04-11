import requests
from django.shortcuts import render

def index(request):
    appid = '53463e2c2ed3172e0488ab9e52e72b44'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Gomel'
    res = requests.get(url.format(city)).json() 
# получили конвертирование json формата в словарь
    
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}
    return render(request, 'weather/index.html', context)
