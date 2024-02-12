#!/usr/bin/env python3

# lcount= 0 # set linecount variable

def read():
    lcount= 0
    with open('dracula.txt','r') as book:
        with open('vampirediary.txt','w') as fang:
            for line in book:
                if "vampire" in line.lower():
                    lcount += 1
                    print(line)
                    fang.write(line)
    print(lcount, " lines were read")               
read()

