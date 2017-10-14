import urllib.request, json

# location data from our user
user_latitude = '37.4419'
user_longitude = '-122.1419'
radius = '1'

# points of interest by amadeus api
"""
amadeus_api_key = 'mqGD234kuOSO7Wyz7EDADu8v1t3ajYFB'

with urllib.request.urlopen(
	'https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle?latitude=' 
	+ str(user_latitude) + '&longitude=' + str(user_longitude) + '&radius=' + str(radius) 
	+ '&apikey=' + str(amadeus_api_key)
	) as url:
    data = json.loads(url.read().decode())

    poi_longitude = data['points_of_interest'][0]['location']['longitude']
    poi_latitude = data['points_of_interest'][0]['location']['latitude']
"""
poi_longitude = user_longitude
poi_latitude = user_latitude

# weather data for the poi

openweathermap_api_key = '3a1deb09f4243599aab7a97c86dd6749'

with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?lat=" 
	+ str(poi_latitude) + '&lon=' + str(poi_longitude) + '&appid=' + 
	str(openweathermap_api_key)
	) as url:
    data = json.loads(url.read().decode())
    
    for i in range(0,len(data)):
        kelvin = data['list'][i]['main']['temp']
        celsius = round(float(kelvin) - 273.15, 1)

        celsius_value = 0

        celsius_value = -abs(celsius-25)
        print(round(celsius_value,2), celsius)


        weather_value = 0

        weather_description = data['list'][i]['weather'][0]['description']
        if 'clear' in weather_description:
        	pass
        elif weather_description == 'scattered clouds':
        	weather_value = weather_value - 5
        elif weather_description == 'overcast clouds':
        	weather_value = weather_value - 10
        else:
        	print('There is no weather!')

        print(weather_description)
        print(weather_value)



