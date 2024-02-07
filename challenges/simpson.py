#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# Challenge 1
# from the challenge list, pull the strings eyes, goggles, and nothing and creat a print function that
# returns this output: My eyes! The goggles do nothing!

# print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

# Challenge 2
# From the trial list, pull the strings eyes, goggles, and nothing and creat a print function that
# returns the same output.

# st1=trial[2].get("goggles")
# st2=trial[2].get("eyes")

# print(f"My {trial[2].get('goggles')}! The {trial[2].get('eyes')} do {trial[3]}!")

# Challenge 3
# From the nightmare list, pull the strings eyes, goggles, and nothing and create a print function that
# returns the same output.

print(f"My {nightmare[0]['user']['name'].get('first')}! The {nightmare[0].get('kumquat')} do {nightmare[0].get('d')}!")


