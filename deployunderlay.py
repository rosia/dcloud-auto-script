#! /usr/bin/env python

import socket
import time
import getpass
import telnetlib

# Clearing all VTY lines in the term server

user = 'cxadmin'
password = 'C1sco12345'

tn = telnetlib.Telnet('198.18.128.96')
tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"clear line 21\n")
tn.read_until(b"[confirm]")
tn.write(b"\n")
tn.write(b"clear line 22\n")
tn.read_until(b"[confirm]")
tn.write(b"\n")
tn.write(b"clear line 23\n")
tn.read_until(b"[confirm]")
tn.write(b"\n")
tn.write(b"clear line 24\n")
tn.read_until(b"[confirm]")
tn.write(b"\n")
tn.write(b"clear line 25\n")
tn.read_until(b"[confirm]")
tn.write(b"\n")
tn.write(b"term len 0\n")
tn.write(b"show line\n")
tn.write(b"exit\n")
print('cleared all lines!')
print(tn.read_all().decode('ascii'))


# Shared Services Switch

HOST = "198.18.128.96"
SharedSvsPORT = 2021

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #SOCK_STREAM means TCP AF_INET means IPv4 address family
   s.connect((HOST,SharedSvsPORT))
   s.sendall(b'\xff\xfe\x01\xff\xfd\x03\xff\xfc\x18\xff\xfc\x1f')
   time.sleep(2)
   # send an enter to make the hop from the terminal server to the console connection of the node we want to be on
   s.send(b'\r')
   time.sleep(2)
   s.send(b'\r')
   response = s.recv(1024)
   print(response)

   if b'>' in response:
       print(b'Newish switch and response is ' + response)
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Sharedservices.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')

       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   elif b'dialog' in response:
       print(b'Just cleaned switch and response is ' + response)
       time.sleep(4)
       s.send(b'no') #Say no to initial config dialog
       s.send(b'\r')
       time.sleep(4)
       s.send(b'yes') #Say yes to terminate auto install
       s.send(b'\r')
       time.sleep(4)
       s.send(b'\r')
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Sharedservices.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')
      # Crypto key generate
       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   else:
       print(b'Something else ' + response)
       s.close()

except:
   print('Error! on Sharedservices switch')




# Fusion Switch

HOST = "198.18.128.96"
SharedSvsPORT = 2022

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #SOCK_STREAM means TCP AF_INET means IPv4 address family
   s.connect((HOST,SharedSvsPORT))
   s.sendall(b'\xff\xfe\x01\xff\xfd\x03\xff\xfc\x18\xff\xfc\x1f')
   time.sleep(2)
   # send an enter to make the hop from the terminal server to the console connection of the node we want to be on
   s.send(b'\r')
   time.sleep(2)
   s.send(b'\r')
   response = s.recv(1024)
   print(response)

   if b'>' in response:
       print(b'Newish switch and response is ' + response)
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Fusion.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')

       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   elif b'dialog' in response:
       print(b'Just cleaned switch and response is ' + response)
       time.sleep(4)
       s.send(b'no') #Say no to initial config dialog
       s.send(b'\r')
       time.sleep(4)
       s.send(b'yes') #Say yes to terminate auto install
       s.send(b'\r')
       time.sleep(4)
       s.send(b'\r')
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Fusion.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')
      # Crypto key generate
       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   else:
       print(b'Something else ' + response)
       s.close()

except:
   print('Error on Fusion!')




# Core Switch

HOST = "198.18.128.96"
SharedSvsPORT = 2023

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #SOCK_STREAM means TCP AF_INET means IPv4 address family
   s.connect((HOST,SharedSvsPORT))
   s.sendall(b'\xff\xfe\x01\xff\xfd\x03\xff\xfc\x18\xff\xfc\x1f')
   time.sleep(2)
   # send an enter to make the hop from the terminal server to the console connection of the node we want to be on
   s.send(b'\r')
   time.sleep(2)
   s.send(b'\r')
   response = s.recv(1024)
   print(response)

   if b'>' in response:
       print(b'Newish switch and response is ' + response)
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Core.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')

       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   elif b'dialog' in response:
       print(b'Just cleaned switch and response is ' + response)
       time.sleep(4)
       s.send(b'no') #Say no to initial config dialog
       s.send(b'\r')
       time.sleep(4)
       s.send(b'yes') #Say yes to terminate auto install
       s.send(b'\r')
       time.sleep(4)
       s.send(b'\r')
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Core.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')
      # Crypto key generate
       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   else:
       print(b'Something else ' + response)
       s.close()

except:
   print('Error on Core!')


# Core Switch

HOST = "198.18.128.96"
SharedSvsPORT = 2024

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #SOCK_STREAM means TCP AF_INET means IPv4 address family
   s.connect((HOST,SharedSvsPORT))
   s.sendall(b'\xff\xfe\x01\xff\xfd\x03\xff\xfc\x18\xff\xfc\x1f')
   time.sleep(2)
   # send an enter to make the hop from the terminal server to the console connection of the node we want to be on
   s.send(b'\r')
   time.sleep(2)
   s.send(b'\r')
   response = s.recv(1024)
   print(response)

   if b'>' in response:
       print(b'Newish switch and response is ' + response)
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Edge1.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')

       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   elif b'dialog' in response:
       print(b'Just cleaned switch and response is ' + response)
       time.sleep(4)
       s.send(b'no') #Say no to initial config dialog
       s.send(b'\r')
       time.sleep(4)
       s.send(b'yes') #Say yes to terminate auto install
       s.send(b'\r')
       time.sleep(4)
       s.send(b'\r')
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Edge1.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')
      # Crypto key generate
       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   else:
       print(b'Something else ' + response)
       s.close()

except:
   print('Error on Edge1!')

# Edge2 Switch

HOST = "198.18.128.96"
SharedSvsPORT = 2025

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #SOCK_STREAM means TCP AF_INET means IPv4 address family
   s.connect((HOST,SharedSvsPORT))
   s.sendall(b'\xff\xfe\x01\xff\xfd\x03\xff\xfc\x18\xff\xfc\x1f')
   time.sleep(2)
   # send an enter to make the hop from the terminal server to the console connection of the node we want to be on
   s.send(b'\r')
   time.sleep(2)
   s.send(b'\r')
   response = s.recv(1024)
   print(response)

   if b'>' in response:
       print(b'Newish switch and response is ' + response)
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Edge2.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')

       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   elif b'dialog' in response:
       print(b'Just cleaned switch and response is ' + response)
       time.sleep(4)
       s.send(b'no') #Say no to initial config dialog
       s.send(b'\r')
       time.sleep(4)
       s.send(b'yes') #Say yes to terminate auto install
       s.send(b'\r')
       time.sleep(4)
       s.send(b'\r')
       s.send(b'en')
       s.send(b'\r')
       s.send(b'conf t')
       s.send(b'\r')

       with open('/Users/rosia/Desktop/dcloud/configbackup/Edge2.txt', 'r') as f:
           data = f.readlines()
           for line in data:
               print(line.encode('UTF-8'))
               s.send(line.encode('UTF-8'))
               s.send(b'\r')
      # Crypto key generate
       s.send(b'crypto key generate rsa')
       s.send(b'\r')
       time.sleep(2)
       s.send(b'\r')
       s.close()

   else:
       print(b'Something else ' + response)
       s.close()

except:
   print('Error on Edge2!')
