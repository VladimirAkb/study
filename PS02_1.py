import requests
import pprint

prm = {
    'q' : 'html'
}

response = requests.get('https://api.github.com/search/repositories', params=prm)

print(response.status_code)

response_json = response.json()
pprint.pprint(response_json)