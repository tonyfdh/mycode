#!/bin/bash

import datetime

current_date = datetime.datetime.now()
day_of_week = current_date.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_name = days[day_of_week]



name = input ("What is your name? ")
day = input ("What day of the week is it? ")

if day == day_name :

    print("Hello " + name + ", the day is " + day)

else:

    print("Hello " + name + ", you should check your computer's time settings. You said the date is " + day + " and your computer says it is " + day_name + ".")

