import urllib.request
import json

print("Weather Report")

region = input("Masukan daerah/kota: ")

try:
    with urllib.request.urlopen(f"https://goweather.herokuapp.com/weather/{region.capitalize()}") as url:
        data = json.load(url)
except urllib.error.HTTPError as e:
    print("An error occured", e)

with urllib.request.urlopen(f"https://goweather.herokuapp.com/weather/{region.capitalize()}") as url:
        data = json.load(url)

temp = data['temperature']
wind = data['wind']
desc = data['description']

print("\nSuhu:", temp, "\nAngin:", wind, "\nDeskripsi:", desc)