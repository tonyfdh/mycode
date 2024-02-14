#!/usr/bin/env python3

import urllib.request
import json
import datetime
import requests
import reverse_geocoder as rg

issloc= "http://api.open-notify.org/iss-now.json"

def main():
    gpstrac = urllib.request.urlopen(issloc)

    nav = gpstrac.read()
    gmaps = json.loads(nav.decode("utf-8"))
    long = gmaps['iss_position'].get('longitude')
    lat = gmaps['iss_position'].get('latitude')
    locator_resp= rg.search((lat,long))

    city= locator_resp[0]["name"]
    country= locator_resp[0]["cc"]


    ts = resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(st)
    

    print(f"Current location of the ISS:\n" 
    f"Lon: {gmaps['iss_position'].get('longitude')}\n" 
    f"Lat: {gmaps['iss_position'].get('latitude')}\n"
    f"Current flyover location: {city}, {country}")
    # f"Time: {ts}")
   # print("Current location of the ISS:")
   # print(f"Lon: {gmaps['iss_position'].get('longitude')}")
   # print(f"Lat: {gmaps['iss_position'].get('latitude')}")
   # print(gmaps)

main()

