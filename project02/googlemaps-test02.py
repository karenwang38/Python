import googlemaps
#import pandas as pd
import time
gmaps = googlemaps.Client(key='AIzaSyByr74aDIXVbHih11Yuqg4XdeYKQMo0ysQ')

query_result = gmaps.places_nearby(keyword="cafe",location= (25.034195, 121.564467), radius=100, language='zh-TW')
#radar_results = gmaps.places_radar(location = (25.0339687, 121.5622835), radius = 100, type = "cafe")
print("query_result =", query_result)

Name = []
Location = []
Address = []

i = 1
for w in query_result['results']:
    print(i, "=========\n", w, "\n==========")
    i = i + 1
    for x in w:
        print("--------" ,x, "-------")
        print(w[x])
        if x == 'geometry':
            Location.append(w[x]['location'])
        elif x == 'name':
            Name.append(w[x])
        elif x == 'vicinity':
            Address.append(w[x])

print(Name)
print(Address)
print(Location)
