import googlemaps

API_KEY = "AIzaSyDbufDUZ5lW7lWJOrdYlrY9zPCSmHcEAMM"



client = googlemaps.Client(API_KEY)

waw = "52.2505562,20.9781065"
lbn = "51.2426387,22.5554689"

directions_result = client.directions(origin=waw,
                                      destination=lbn,
                                      mode="driving",
                                      avoid="ferries")


print(directions_result[0]['legs'][0]['distance'])
