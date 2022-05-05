from my_number.my_number import return_number
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

Key = "77ba67a9864141d0b3f46b27a21f3212"

phone_number_get = return_number()

get_number = phonenumbers.parse(phone_number_get)
your_location = geocoder.description_for_number(get_number, "ru")

service_provider_name = phonenumbers.parse(phone_number_get)

geocoder = OpenCageGeocode(Key)
query = str(your_location)
result = geocoder.geocode(query)

lat = result[0]["geometry"]["lat"]
lng = result[0]["geometry"]["lng"]
operator = carrier.name_for_number(service_provider_name, "ru")

map = folium.Map(location = [lat, lng], zoon_start = 9)
folium.Marker([lat, lng], popup = your_location).add_to(map)

number_info = f"\tКординаты: {lat, lng}\n\tОператор: {operator}\n\tМестоположение: {your_location}"
print(f"---Номер: {phone_number_get}---\n{number_info}")

map.save("my_location.html")
open("../my_location.html")