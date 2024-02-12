import requests

url = 'http://numbersapi.com/'

number = input()

response = requests.get(f"{url}{number}")

print(response.text)
