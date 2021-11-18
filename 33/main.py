import requests
from datetime import datetime

MY_LAT = 48.743474
MY_LONG = 9.152581
MY_FORMATTED = 0

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": MY_FORMATTED,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]#.split("T")#[1]#.split[":"][0])
sunset = int(data["results"]["sunset"].split("T")[1].split[":"])#[0])
print(f"sunrise: {sunrise}")
print(f"sunet: {sunset}")

time_now = datetime.now()
print(time_now.hour)
