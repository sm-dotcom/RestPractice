import jsonpath
import requests
import json

# API URL
baseurl = "https://reqres.in"

# Lesson#3
url = "https://reqres.in/api/users/2"
response = requests.delete(url)
print(response)
assert response.status_code == 204