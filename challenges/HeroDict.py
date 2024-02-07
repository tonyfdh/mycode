#!/usr/bin/env python3

char_name=input("Which character do you want to know about? (Starlord, Mystique, Hulk)").lower()

char_stat=input("What statistic do you want to know about? (real name, powers, archenemy)").lower()

marvelchars= {
"starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

# Case-insensitive dictionary lookup
char_info = marvelchars.get(char_name)
if char_info:
    stat_value = char_info.get(char_stat)
    if stat_value:
        print(f"{char_name.title()}'s {char_stat} is: {stat_value.title()}")
    else:
        print(f"Stat '{char_stat}' not found for character '{char_name.title()}'")
else:
    print(f"Character '{char_name.title()}' not found")

