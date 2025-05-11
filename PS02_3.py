import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "title": "тестовый post запрос",
    "foo": "FOO FOO FOO",
    "body": "тестовый контент post запроса",
    "bar": "Alla ya v bar",
    "userId": 1
}

response = requests.post(url, data=data)

print(response.status_code)

response_json = response.json()
pprint.pprint(response_json)