import jsonpath
import requests
import json


# API URL
baseurl = "https://reqres.in"



# # Lesson#4
file = open('C:\\Users\\sarah.mahmood\\Desktop\\CreateUser.json','r')
json_input = file.read()
request_json =json.loads(json_input)
print(request_json)

Parameters = {
    "name": "another_user",
    "job": "second_leader"
}


url = baseurl + "/api/users"
response = requests.post(url, headers=Parameters)
print(response.content)

#check response
assert response.status_code == 201

#Fetch headers
print(response.headers.get('Content-Length'))

#parse response to json format
response_json = json.loads(response.text)

#pick ids using json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])








# def testcase_to_getAuthtoken(self, TestCasesStatus=True):
#
#     TestCaseID= "101"

