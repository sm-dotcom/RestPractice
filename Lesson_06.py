import jsonpath
import requests
import json


# API URL
baseurl = "https://reqres.in"

def create_user_func():
    # Lesson#4
    file = open('C:\\Users\\sarah.mahmood\\Desktop\\CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)

    Parameters = {
        "name": "another_user",
        "job": "second_leader"
    }

    url = baseurl + "/api/users"
    response = requests.post(url, headers=Parameters)
    print(response.content)

    # check response
    assert response.status_code == 202

    # Fetch headers
    print(response.headers.get('Content-Length'))

    # parse response to json format
    response_json = json.loads(response.text)

    # pick ids using json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

    # <<<<<<< HEAD

    # =======
    update_li = jsonpath.jsonpath(response_json, 'createdAt')
    print(update_li[0])
    # >>>>>>> [Sarah]Restapi Put and post request. Main token generated.


