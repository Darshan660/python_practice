import phonenumbers as pn
from phonenumbers import geocoder, carrier, timezone

user_number = input("Enter the number(first enter your country code then enter the phonenumber):-")
ch_number = pn.parse(user_number,"CH")
print("Country Name:-",geocoder.description_for_number(ch_number,"en"))

service_provider = pn.parse("+917710020979","RO")
print("Service Provider:-",carrier.name_for_number(service_provider,"en"))