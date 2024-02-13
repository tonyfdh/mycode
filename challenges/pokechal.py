#!/usr/bin/env python3

import requests

def main():
    pokenum=input('Pick a number between 1 and 151!\n>')
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi["name"])
    print(pokeapi["sprites"]["front_default"])
    image_url = pokeapi["sprites"]["front_default"]
    response = requests.get(image_url)

    for x in pokeapi['moves']:
        print(x["move"]["name"])

main()
