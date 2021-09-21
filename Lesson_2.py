import jsonpath
import requests
import json

# API URL
baseurl = "https://reqres.in"

# Lesson#2
url = "https://reqres.in/api/user?page=2"
response = requests.get(url)
json_reponse = json.loads(response.text)
# print(json_reponse)
print("    ")
pages = jsonpath.jsonpath(json_reponse,'total_pages')
assert pages[0] == 4