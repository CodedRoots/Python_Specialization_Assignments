import json
import urllib.request


url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
info = json.loads(data)

total = 0
counts = []

for item in info['comments']:
    count = item['count']
    counts.append(count)
    total = total + count

print('Counts:', counts)
print('Total:', total)