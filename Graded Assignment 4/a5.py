# /// script
# requires-python = ">=3.11"
# dependencies = ['geopy',
# 'geopandas']
# ///

from geopy.geocoders import Nominatim

locator = Nominatim(user_agent = "myGeocoder")

location = locator.geocode({"city":"Kinshasa", "state":"Kinshasa", "country":"Democratic Republic of the Congo"})

location.raw

#Output: -4.4817100
