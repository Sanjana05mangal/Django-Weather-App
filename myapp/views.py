from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    city= request.GET.get('city', 'Indore')
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=03a8e0f8f61d21d6a4737a902972be29'
    data= requests.get(url).json()
    payload= {
             'city': data['name'], 
             'weather': data['weather'][0]['main'], 
             'icon': data['weather'][0]['icon'], 
             'temperature': int(data['main']['temp'] -273) , 
             'pressure': data['main']['pressure'], 
             'humidity': data['main']['humidity']
             }
    context= {'data': payload}
    print(context)
    return render(request, 'home.html', context)