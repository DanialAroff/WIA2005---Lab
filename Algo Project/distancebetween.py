from geopy import distance
from geopy.geocoders import Nominatim


class MyDistanceCalculator:
    def __init__(self):
        self.timeout = 20
        self.geolocator = Nominatim(user_agent='WIA2005_Project')

    def distance(self, location1, location2):
        location1_g = self.geolocator.geocode(location1, timeout=self.timeout, language='en')
        location2_g = self.geolocator.geocode(location2, timeout=self.timeout, language='en')

        location1_coord = (location1_g.latitude, location1_g.longitude)
        location2_coord = (location2_g.latitude, location2_g.longitude)

        return round(distance.distance(location1_coord, location2_coord).km, 3)

    def get_coord(self, location):
        location = self.geolocator.geocode(location, language='en')
        return location.latitude, location.longitude

    def get_addr(self, location):
        location = self.geolocator.geocode(location, language='en')
        return location

    def set_timeout(self, time):
        self.timeout = time
