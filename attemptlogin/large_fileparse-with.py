#!/usr/bin/env python3

loginfail=0 #set variable
loginsuccess=0 #second variable for success
# open with
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    #loop
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            print(line.split(" ")[-1] + " IP for failed login")
        elif "POST" in line:
            loginsuccess += 1

print("The nuymber of failed login attempts is", loginfail)
print("The number of successful login attempts is", loginsuccess)
