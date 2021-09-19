import requests
import json

host_url = "http://thetestingworldapi.com"

response_code = requests.get(host_url+"/api/studentsDetails", {'id': 452914})
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




