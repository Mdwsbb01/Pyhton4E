#socket
'''
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):  # judge the stream is closed or not
        break
    print(data.decode())
mysock.close()
'''
'''
#url
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().rstrip())
'''
#html
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

prompt = 'Enter: '
uname = input(prompt)
html = urllib.request.urlopen(uname, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
'''
#Exercise 1: Change the socket program socket1.py
# to prompt the user for the URL
# so it can read any web page.
# You can use split('/') to break the URL
# into its component parts so you can
# extract the host name for the socket connect call.
# Add error checking using try and except to
# handle the condition where the user
# enters an improperly formatted or non-existent URL.

import socket

while True:
    url = input('Enter the url: ')

    if url == 'done':
        print('project end')
        quit()

    try:
        hostname = url.split('/')[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostname, 80))
        cmd = ('GET '+url+' HTTP/1.0\r\n\r\n').encode() # no space
        mysock.send(cmd)
    except:
        print('The invalid url')
        continue

    while True:
        data = mysock.recv(512)
        if len(data) < 1: # judge the stream is closed or not
            break
        print(data.decode(), end='')
    mysock.close()

