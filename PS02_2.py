import requests
import pprint

prm = {
    'userId' : '1'
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=prm)

print(response.status_code)

response_json = response.json()
pprint.pprint(response_json)