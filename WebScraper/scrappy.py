import requests
from bs4 import BeautifulSoup
# learn to use scrapy the framework
# the url for the website
url = 'https://news.ycombinator.com'

# get the response using the requests module
r = requests.get(url)

# making the soup

soup = BeautifulSoup(r.text,'html.parser')
print(soup.select('.score'))
# for i in soup.select('.titlelink'):
# 	print(i)