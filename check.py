#!/usr/bin/python3
import socket
import urllib.request
import os

'''
Author: Martino Jones
Description: This is a Python3 script that will check Nvidia servers for am update for your Nvidia GPU.
'''

#Check to see if the server is available
def is_connected():
  try:
      #Try to connect to nvidia's site
    host = socket.gethostbyname("nvidia.com")
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

def getGPU():
    output = os.popen('lspci | grep -i vga | grep -i nvidia').read()
    output = output.split('[')[1].split(']')[0]
    return output

def getCurrentVersion():
    output = os.popen('nvidia-smi | grep Version').read()
    output = output.split("Version:")[1].split('|')[0].strip(" ")
    return output

def getLatestVersion():
    #This will get the latest version by checking the site
    versions = []
    u2 = urllib.request.urlopen('http://www.nvidia.com/object/linux-amd64-display-archive.html')

    for lines in u2.readlines():
        if "Version" in lines.decode("utf-8"):
            versions.append(lines.decode("utf-8"))

    return versions[0].split("Version:")[1].split("<br>")[0].strip(" ")


def main():
    #Check if can access Nvidia's site
    if is_connected() == False:
        print("Cannot connect to Nvidia server. Can't continue.")
        exit()

    GPU = getGPU()
    latestVerion = getLatestVersion()
    currentVersion = getCurrentVersion()

    print("GPU: " + getGPU())
    if float(latestVerion) > float(currentVersion):
        print("Update available\n")
        print("You're on: " + currentVersion)
        print("Latest version: " + latestVerion)



if __name__ == '__main__':
    main()
