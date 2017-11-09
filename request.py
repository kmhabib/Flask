import requests
import json

headers = {
        "content-type": "application/json"
    }
result = requests.get(url="http://35.166.220.241:8080/api/v1/emails", headers=headers, verify=False)

response = result.json()
print(json.dumps(response))

data = {
        "Sajjad": "sajjad@spokesly.com",
        "Junaid": "junaid@spokesly.com"
    }
#result = requests.post(url="http://127.0.0.1:8080/api/v1/emails", data=json.dumps(data), headers=headers, verify=False)
#result = requests.get(url="http://127.0.0.1:8080/api/v1/emails", headers=headers, verify=False)
#response = result.json()
#print(json.dumps(response))

#result.raise_for_status()
#print(result)
#print(result.json)
