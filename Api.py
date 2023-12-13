import requests
url="https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=4"
response=requests.get(url)
data=response.json()
print(data)