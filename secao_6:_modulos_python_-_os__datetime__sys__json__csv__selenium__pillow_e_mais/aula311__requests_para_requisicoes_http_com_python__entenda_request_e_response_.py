# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests


# http:// -> 80
# https:// -> 443
# url = 'http://localhost:3333/'
url = "http://127.0.0.1:3333/"

response = requests.get(url)
print(response)
print(response.status_code)
# print(response.headers)
# print(content)  # vai aparecer um b na frente do codigo significa bytes
print(response.text)
