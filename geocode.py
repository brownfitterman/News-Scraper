from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("Gandipet")
print(location.latitude)
print(location.longitude)


