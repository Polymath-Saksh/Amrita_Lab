import requests

response = requests.get('http://localhost:5000/test')
print(response.text)