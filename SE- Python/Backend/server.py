from urllib.parse import urlparse

#from urllib.parse import urlparse, parse_qs
address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)
print(parts)
print(parts.query)
# query = parse_qs(parts.query)
# print(query)


# import requests
# a = requests.get('http://www.udacity.com')
# print(a)


# requests.get('http://swapi.co/api/people/1/')
# a.json()['name']