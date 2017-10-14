import urllib.request, json 

# input from amadeus api
with urllib.request.urlopen("https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle?latitude=41.878&longitude=-87.645&radius=1&apikey=9bkWAf6vpxlcx0OuR03Bak5TtJ1qvvVq") as url:
    data = json.loads(url.read().decode())
    # print(data['points_of_interest'][0]['title'])

    # def get_lon(data):

    poi_longitude = data['points_of_interest'][2]['location']['longitude']
    poi_latitude = data['points_of_interest'][2]['location']['latitude']

#print(type(latitude))

#with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?" + str(latitude) + '&' + str(longitude) + '&appid=3a1deb09f4243599aab7a97c86dd6749') as url:
#    data = json.loads(url.read().decode())

with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?lat=" + str(poi_latitude) + '&lon=' + str(poi_longitude) + '&appid=3a1deb09f4243599aab7a97c86dd6749') as url:
    data = json.loads(url.read().decode())
    
    for i in range(0,len(data)):
        print (data['list'][i]['dt_txt'])
    #print(data)