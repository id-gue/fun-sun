import urllib.request, json

# location data from our user
user_latitude = '37.4419'
user_longitude = '-122.1419'
radius = '1'

area = 

for poi in area:
    # points of interest by amadeus api
    amadeus_api_key = 'mqGD234kuOSO7Wyz7EDADu8v1t3ajYFB'

    with urllib.request.urlopen(
    	'https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle?latitude=' 
    	+ str(user_latitude) + '&longitude=' + str(user_longitude) + '&radius=' + str(radius) 
    	+ '&apikey=' + str(amadeus_api_key)
    	) as url:
        data = json.loads(url.read().decode())

        poi_longitude = data['points_of_interest'][poi]['location']['longitude']
        poi_latitude = data['points_of_interest'][poi]['location']['latitude']

    # weather data for the poi
    openweathermap_api_key = '3a1deb09f4243599aab7a97c86dd6749'

    weather_value_list = []

    with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?lat=" + 
        str(poi_latitude) + '&lon=' + str(poi_longitude) + '&appid=' + str(openweathermap_api_key)
    	) as url:
        data = json.loads(url.read().decode())
        
        for i in range(0,len(data)):
            kelvin = data['list'][i]['main']['temp']
            celsius = round(float(kelvin) - 273.15, 1)

            weather_value = 0
            weather_value = -abs(celsius-25)
            weather_id = data['list'][i]['weather'][0]['id']

            if weather_id == 800 or weather_id == 801:
                pass
            elif weather_id == 802 or weather_id == 803:
                weather_value = weather_value - 10
            else:
                weather_value = weather_value - 50
            
            weather_value_list.append(weather_value)

    # print(weather_value_list)
    weather_value_average = round(sum(weather_value_list) / float(len(weather_value_list)))

        # print(data['list'][i]['weather'][0]['description'])

poi_with_good_weather = {}
poi_with_good_weather['key'] = round(weather_value_average,2)
json_data = json.dumps(poi_with_good_weather)

print(poi_with_good_weather)
