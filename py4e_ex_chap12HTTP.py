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
'''
import socket

while True:
    url = input('Enter the url: ')

    if url == 'done':
        print('Project ended')
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
        print(data.decode(), end='') # not change the line in the end
    mysock.close()
'''
#Exercise 2: Change your socket program so that it counts
# the number of characters it has received
# and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document
# and count the total number of characters
# and display the count of the number of characters
# at the end of the document.
'''
import socket

while True:
    url = input('Enter the url: ')

    if url == 'done':
        print('Project ended')
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
        data = mysock.recv(3000)
        if len(data) < 1: # judge the stream is closed or not
            break
        print(data.decode(), end='')  # not change the line in the end
        print('The characters of data = ', len(data))
        quit()
    mysock.close()
'''
# Exercise 3: Use urllib to replicate the previous exercise of (1)
# retrieving the document from a URL, (2) displaying up to 3000 characters,
# and (3) counting the overall number of characters in the document.
# Don't worry about the headers for this exercise,
# simply show the first 3000 characters of the document contents.
'''
import urllib.request, urllib.parse, urllib.error

count = 0
#wordslst = list()

while True:
    url = input('Enter the url: ')

    if url == 'done':
        print('Project ended')
        quit()

    try:
        fhand = urllib.request.urlopen(url)

    except:
        print('The invalid url')
        continue

    while True:
        for line in fhand:
            line = line.decode().rstrip()
            #print(type(line))
            for words in line:
                count = count + 1
                #wordslst.append(words)
                if count <= 3000:
                    print(words)
                    continue
                else:
                    print(words[:3000])
                    break
            print('The number of characters is: ', count) # can not print the real character number if the count > 3000
'''
#Exercise 4: Change the urllinks.py program to extract and count
# paragraph (p) tags from the retrieved HTML document and
# display the count of the paragraphs as the output of your program.
# Do not display the paragraph text, only count them.
# Test your program on several small web pages as well as
# some larger web pages.
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

prompt = 'Enter the url: '
uname = input(prompt)
html = urllib.request.urlopen(uname, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
count = 0
for tag in tags:
    count = count + 1
print(count)
'''
#Exercise 5: (Advanced) Change the socket program so that
# it only shows data after the headers and a blank line
# have been received. Remember that recv is receiving
# characters (newlines and all), not lines.
'''
import socket

while True:
    url = input('Enter the url: ')

    if url == 'done':
        print('Project ended')
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
        data = mysock.recv(3000)
        if not data:
            break
        else:
            data = data.decode()
            header_end_pos = data.find('\r\n\r\n') + 4 # +4 means also ignore the space, can know it by checking the webpage sourcecode
            refined_data = data[header_end_pos:]
            if len(refined_data) < 1:
                break
            print(refined_data, end='')
    mysock.close()
'''
#the example of github URL=https://stackoverflow.com/users/4952130/dimitris-fasarakis-hilliard
import socket

url = input('Enter the url: ')
hostname = url.split('/')[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
cmd = ('GET '+url+' HTTP/1.0\r\n\r\n').encode() # no space
mysock.send(cmd)

resp = []
while True:
    data = mysock.recv(3000)

    if not data:
        break
    else:
        resp.append(data.decode())
mysock.close()

resp = ''.join(resp)
#print(resp)
body = resp.partition('\r\n\r\n')[2] # using the assigned character to split
print(body, end='')
