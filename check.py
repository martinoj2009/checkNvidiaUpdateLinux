#!/usr/bin/python3
import socket
import subprocess
import os

'''
Author: Martino Jones
Description: This is a Python3 script that will check Nvidia servers for
    am update for your Nvidia GPU.
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
    print(output)



def main():
    #Check if can access Nvidia's site
    if is_connected() == False:
        print("Cannot connect to Nvidia server. Can't continue.")
        exit()

    getGPU()




if __name__ == '__main__':
    main()
