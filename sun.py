import urllib.request, json, argparse

# get user position from command line
# play.py --lon 10.3 --lat 56.3 --distance 10
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--lat',default='37.4419', dest='lat', help='lat of position')
parser.add_argument('--lon',default='-122.1419', dest='lon', help='lon of position')
parser.add_argument('--distance',default='50', dest='distance', help='radius to search in km')

args = parser.parse_args()

print ("{'location':'hamburg'}")
