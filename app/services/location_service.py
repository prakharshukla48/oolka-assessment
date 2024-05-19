import googlemaps
import os

class LocationService():

    def get_location(self, address):
        api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

        gmaps = googlemaps.Client(key=api_key)

        # Geocoding an address
        geocode_result = gmaps.geocode(api_key)

        # Print the latitude and longitude
        return (geocode_result[0]['geometry']['location'])

