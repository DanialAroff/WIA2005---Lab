import calendar
import time
from geopy.geocoders import Nominatim

cal = calendar.month(2019, 5)
print(cal)

print(time.strftime('%Y/%m/%d %I:%M:%S  %A'))
geolocator = Nominatim(user_agent='WIA2005_Assignment')

# location = geolocator.geocode('Shanghai', addressdetails=True, language='en')
# if location:
#     latitude = location.latitude
#     longitude = location.longitude
# print('\n' + str(location))
# print('\nCoordinate: ' + str(latitude) + ', ' + str(longitude))
