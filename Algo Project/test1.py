import time
from geopy import distance
from geopy.geocoders import Nominatim
from distancebetween import MyDistanceCalculator
# 3.832795, 103.308332 -- my house

print(time.strftime('%Y/%m/%d %I:%M:%S  %A'))
geolocator = Nominatim(user_agent='WIA2005_Assignment')

d = MyDistanceCalculator()
location1 = 'Moscow'
location2 = 'New York City'

print('Distance: ' + str(d.distance(location1, location2)) + 'km\n')

print(d.get_addr(location1))
print(d.get_addr(location2))

# shanghai = geolocator.geocode('Shanghai', timeout=20, language='en')
# dhaka = geolocator.geocode('Dhaka', timeout=20, language='en')
#
# shanghai_coord = (shanghai.latitude, shanghai.longitude)
# dhaka_coord = (dhaka.latitude, dhaka.longitude)
# print(distance.distance(shanghai_coord, dhaka_coord).km)

# location = geolocator.geocode('Shanghai', addressdetails=True, language='en')
# if location:
#     latitude = location.latitude
#     longitude = location.longitude
# print('\n' + str(location))
# print('\nCoordinate: ' + str(latitude) + ', ' + str(longitude))
