#!/usr/bin/env python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # set counter

# open the file

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# turn the file into a list

keystone_file_lines=keystone_file.readlines()

# loop it
for line in keystone_file_lines:
    # find the fail pattern
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # simplified loginfail = loginfail +1
print("The number of failed log in attempts is", loginfail)
keystone_file.close()
