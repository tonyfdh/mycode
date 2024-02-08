#!/usr/bin/env python3

# import library files
import shutil
import os

def main():
    # move into directory
    os.chdir("/home/student/mycode")

    # copy the file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy the directory
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
