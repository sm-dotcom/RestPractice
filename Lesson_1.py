import jsonpath
import requests
import json

# API URL
baseurl = "https://reqres.in"

# Lesson#1
response = requests.get(url)
#Print response
print(response)
print(" ")
#print reponse content
print(response.content)
print(" ")
#Print reponse headers
print(response.headers)
print(" ")

#Print reponse headers
resp= response.json()
showcode = str(resp['Response '])
print("This is showcode",showcode)
print(" ")

#Print reponse status_code
print("this is response status code",response.status_code)