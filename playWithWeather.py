import urllib.request, json

# input from amadeus api
with urllib.request.urlopen("https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle?latitude=41.878&longitude=-87.645&radius=1&apikey=9bkWAf6vpxlcx0OuR03Bak5TtJ1qvvVq") as url:
    data = json.loads(url.read().decode())
    print(data['points_of_interest'][0]['title'])
    #print(data)

# location = input()