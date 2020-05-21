 #The program will prompt for a URL, read the JSON data from that URL using urllib
 #and then parse and extract the comment counts from the JSON data
 
import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1:
      address = 'http://py4e-data.dr-chuck.net/comments_42.json'

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
     js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to retrieve')
        # print(data)
count = 0
print('-'*50)
print(json.dumps(js, indent=4))
l = len(js['comments'])
for i in range(l):
    count += js['comments'][i]['count']
print(count)
