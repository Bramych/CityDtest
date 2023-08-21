import requests

response = requests.post("https://playground.learnqa.ru/api/get500")
print(response.status_code)