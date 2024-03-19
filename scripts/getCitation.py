import requests, json, os
api_key = os.environ.get('API_KEY')
headers = {'x-api-key': api_key}

r = requests.post(
    'https://api.semanticscholar.org/graph/v1/paper/batch',
    params={'fields': 'citationCount,title'},
    json={"ids": ["3c550bda6ac5a98f630203b1750721acc61605b2", "9ba36db0d9f2d586abaa85ea6a0b48c609c5c9ec"]}, 
    headers=headers
)

json_data = json.dumps(r.json(), indent=2)
# print(json_data)
with open('./citationCount.json', 'w') as file:
    file.write(json_data)
