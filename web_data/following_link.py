#Following Links in Python
#The program will use urllib to read the HTML from the data files below,
#extract the href= vaues from the anchor tags, scan for a tag that is in a 
#particular position relative to thefirst name in the list, follow that 
#link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL ')
count = int(input('Enter count '))
pos = int(input('Enter position '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

while count >= 0:
    #request to open initial url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') #get tags from new url
    x = tags[pos-1].text #print followed link name
    print(x)
    print(url)
    url = tags[pos-1].get('href', None) # get the following link
    count-=1
