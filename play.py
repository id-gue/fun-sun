import urllib.request, json

# location data from our user
user_latitude = '37.4419'
user_longitude = '-122.1419'
radius = '1'

# points of interest by amadeus api

amadeus_api_key = 'mqGD234kuOSO7Wyz7EDADu8v1t3ajYFB'

with urllib.request.urlopen('https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle?latitude=' + str(user_latitude) + '&longitude=' + str(user_longitude) + '&radius=' + str(radius) + '&apikey=' + str(amadeus_api_key)) as url:
    data = json.loads(url.read().decode())

    poi_longitude = data['points_of_interest'][0]['location']['longitude']
    poi_latitude = data['points_of_interest'][0]['location']['latitude']

# weather data for the poi

openweathermap_api_key = '3a1deb09f4243599aab7a97c86dd6749'

with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?lat=" + str(poi_latitude) + '&lon=' + str(poi_longitude) + '&appid=' + str(openweathermap_api_key)) as url:
    data = json.loads(url.read().decode())
    
    for i in range(0,len(data)):
        print (data['list'][i]['dt_txt'])
