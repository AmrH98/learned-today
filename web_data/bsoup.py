#Scraping Numbers from HTML using BeautifulSoup 
#The program will use urllib to read the HTML from the data files below, and parse the data,
#extracting numbers and compute the sum of the numbers in the file.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total = 0
temp = 0
# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
    x = str(tag)
    x = re.findall('([0-9]+)',x)
    for i in x: temp = int(i)
    total+=temp
print(total)
