import requests
import json

host_url = "http://thetestingworldapi.com"

body = {
        "id": 555,
        "first_name": "monika",
        "middle_name": "sen",
        "last_name": "gupta",
        "date_of_birth": "11/11/1985"
}
response_code = requests.post(host_url+"/api/studentsDetails", data=body)
print("the response for this GET request is")
print(response_code)
if response_code.ok:
    print("This request has no error")
else:
    print("This request has an error")

response_result = (json.dumps(response_code.json(), indent=4))
print(response_result)

if response_result.lower():
    print("The strings are lowerCase")

else:
    print("The strings are not lower case")

# parse the JSON object into a dict
slideInfo = json.loads(response_result)
print(slideInfo["first_name"])
