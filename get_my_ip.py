import requests

url = 'https://httpbin.org/ip'
response = requests.get(url)
print response.json()
