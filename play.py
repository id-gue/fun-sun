import urllib.request, json, argparse
from key import amadeus_api_key, openweathermap_api_key

# get user position from command line
# play.py --lon 10.3 --lat 56.3 --distance 10
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--lat',default='37.4419', dest='lat', help='lat of position')
parser.add_argument('--lon',default='-122.1419', dest='lon', help='lon of position')
parser.add_argument('--distance',default='50', dest='distance', help='radius to search in km')

args = parser.parse_args()

user_latitude = args.lat
user_longitude = args.lon
radius = args.distance


def getGeodata(user_longitude,user_latitude,radius):

    with urllib.request.urlopen(
    	'https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle?latitude=' 
    	+ str(user_latitude) + '&longitude=' + str(user_longitude) + '&radius=' + str(radius) 
    	+ '&apikey=' + str(amadeus_api_key)
    	) as url:
        data = json.loads(url.read().decode())

    return data['points_of_interest']


def getWeatherDataForOneLocation(poi_latitude,poi_longitude):     

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
            
            # weather points for one location, every point is 3h
            weather_value_list.append(weather_value)

    # print(weather_value_list)
    weather_value_average = round(sum(weather_value_list) / float(len(weather_value_list)))
    return weather_value_average


# add weather_average to geodata
def getWeatherData(geodata):
  
    #data_with_weather_list = []
    for oneGeodate in geodata:
        oneGeodate['weather_average']=getWeatherDataForOneLocation(
            oneGeodate['location']['latitude'],oneGeodate['location']['longitude']
            )

    return geodata


# all data together
unfiltered_geodata = getGeodata(user_longitude,user_latitude,radius)
unfiltered_geodata = getWeatherData(unfiltered_geodata)

all_weather_values = 0


# give back the pois with good weather
def filterGeodata(unfiltered_geodata): 

    list = unfiltered_geodata

    total = 0
    count = 0

    # calculate average weather of all POIs
    for i in list:
        total = total + (int(i['weather_average']))
        count += 1
    all_weather_values = (total / count)
    filtered_geodata = []

    # add POIs with weather better than average to filtered_geodata
    for poi in list:
        if poi['weather_average'] <= all_weather_values:
            filtered_geodata.append(poi)

    print(json.dumps(filtered_geodata))

filterGeodata(unfiltered_geodata)
