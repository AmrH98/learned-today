#Extracting Data from XML
#The program will prompt for a URL, read the XML data from that URL 
#using urllib and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_482617.xml'

uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
sum = 0
counts = tree.findall('.//count')

for i in counts:
    print('num: ', i.text)
    temp = i.text
    temp = int(temp)
    sum+= temp
print(sum)
