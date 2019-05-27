import time
from geopy.geocoders import Nominatim
from number2 import MyDistanceCalculator

print(time.strftime('%Y/%m/%d %I:%M:%S  %A\n'))
geolocator = Nominatim(user_agent='WIA2005_Assignment')

d = MyDistanceCalculator()
locations = ['Moscow', 'Dhaka', 'Manila', 'New York City', 'Shanghai', 'Kuala Lumpur', 'Tokyo']

for current in range(len(locations)):
    for other in range(len(locations)):
        if current is not other:
            print(locations[current], '<->', locations[other])
            print('Distance: ' + str(d.distance(locations[current], locations[other])) + 'km')
    print('\n')
