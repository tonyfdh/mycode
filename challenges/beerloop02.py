#!/usr/bin/env python3

import time

print('This is a simple script to demonstrate loops with user input.')

while True:
    # Input validation for starting and ending numbers
    while True:
        b1 = input('Enter a number between 1-99 to start at: ')
        b2 = input('Enter a number between 1-99 to end at: ')
        if b1.isdigit() and b2.isdigit():
            b1 = int(b1)
            b2 = int(b2)
            if 1 <= b1 <= 99 and 1 <= b2 <= 99:
                break
            else:
                print('Please enter valid numbers between 1 and 99.')
        else:
            print('Please enter integer numbers.')

    # Input validation for count by
    while True:
        countby = input('How many do you want to count at a time? ')
        if countby.isdigit():
            countby = int(countby)
            if countby > 0 and countby <= abs(b2 - b1):
                break
            else:
                print('Please enter a valid count that is less than or equal to the range.')
        else:
            print('Please enter an integer count.')

    # Check if the numbers entered match
    if b1 != b2:
        break
    else:
        print("Starting number must be different from ending number. Please try again.")

def loop():
    step = 1 if b1 < b2 else -1
    for beer in range(b1, b2 + step, countby * step):
        print(beer, "bottles of beer on the wall!")
        print(beer, "bottles of beer! Take one down, pass it around")
        time.sleep(.5)
 
loop()
print("All outta beer, see ya later!")

