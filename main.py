import requests
from datetime import datetime as dt

MY_LAT = #Enter your Latitude
MY_LONG = #Enter your Longitude

# by default, the formatted is on at binary 1. Changing the formatted to 0 changes it to unix time
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
# print(sunrise.split("T")[1].split(":")[0])
print(sunset)
# print(sunset.split("T")[1].split(":")[0])
time_now = dt.now()
print(time_now.hour)
