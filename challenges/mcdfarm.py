#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_Farm=farms[0]["agriculture"]
W_Farm=farms[1]["agriculture"]
SE_Farm=farms[2]["agriculture"]

def main():
    upick=input("Would to like to see the animals from the NE Farm, W Farm or SE Farm?")
    if upick.lower==("ne farm"):
        print(NE_Farm)
    elif upick.lower==("w farm"):
        print(W_Farm)
    elif upick.lower==("se farm"):
        print(SE_Farm)

main()
