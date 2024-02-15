import requests

response = requests.get("https://api.thecatapi.com/v1/images/search")

print(response.json()[0].get('url'))
