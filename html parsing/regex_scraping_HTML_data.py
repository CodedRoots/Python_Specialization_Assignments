import urllib.request, urllib.parse, urllib.error
import re

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2104326.html')
tot = 0

for line in fhand:
    line = line.decode()
    if not re.search('<span class="comments">', line):
        continue
    numbers = re.findall('[0-9]+', line)
    if numbers:
        for nbr in numbers:
            nbr = int(nbr)
            tot = tot + nbr
print(tot)