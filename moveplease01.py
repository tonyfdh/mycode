#!/usr/bin/env python3

# import libs
import shutil
import os

def main():
    
    # set current directory
    os.chdir('/home/student/mycode')

    # move an object
    shutil.move('raynor.obj', 'ceph_storage/')

    # request input to rename a file
    xname=input('What would you like to rename kerrigan.obj too?')

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


main()
