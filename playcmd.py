import urllib.request, json,argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--lat',default='37.4419', dest='lat', help='lat of position')
parser.add_argument('--lon',default='-122.1419', dest='lon', help='lon of position')
parser.add_argument('--distance',default='1', dest='distance', help='radius to search in km')

args = parser.parse_args()

user_latitude = args.lat
user_longitude = args.lon
radius = args.distance


print (user_latitude)
print (user_longitude)
print (radius)