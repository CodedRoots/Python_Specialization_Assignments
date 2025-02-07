# this is a function inception, to find a link at a X index, follow the link, find a link at X index within that link and follow it. 
# This was repeated 7 times and the last link was not followed as I was looking for the name written in it.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def fct1 (url, count=0, max_count=7):
    if count == max_count:
        print('done')
        return
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    links = [tag.get('href', None) for tag in tags]

    index = 17  
    if index < len(links):
        next_url = links[index]
        print(next_url)

        fct1(next_url, count + 1, max_count)

start_url = 'http://py4e-data.dr-chuck.net/known_by_Kaydane.html'
fct1(start_url)