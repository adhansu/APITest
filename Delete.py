import requests
import json

host_url = "http://thetestingworldapi.com"

response_code = requests.delete(host_url+"/api/studentsDetails/452968")
print("the response for this GET request is")
print(response_code)

if response_code.ok:
    print("This request has no error")
else:
    print("This request has an error")

response_result = (json.dumps(response_code.json(), indent=4))
print(response_result)