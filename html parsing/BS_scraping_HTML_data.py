import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2104326.html').read()
soup = BeautifulSoup(html, 'html.parser')
tot = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    tag = tag.decode()
    if not re.search('<span class="comments">', tag):
        continue
    numbers = re.findall('[0-9]+', tag)
    if numbers:
        for nbr in numbers:
            nbr = int(nbr)
            tot = tot + nbr
print(tot)