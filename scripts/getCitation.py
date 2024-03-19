import requests
import json
import os

api_key = os.environ.get('API_KEY')
headers = {'x-api-key': api_key}

json_data = {}

try:
    response = requests.post(
        'https://api.semanticscholar.org/graph/v1/paper/batch',
        params={'fields': 'citationCount,title'},
        json={"ids": ["3c550bda6ac5a98f630203b1750721acc61605b2", "9ba36db0d9f2d586abaa85ea6a0b48c609c5c9ec"]},
        headers=headers
    )

    response.raise_for_status()
    json_data = response.json()

except Exception as e:
    print(f'An error occurred: {e}')
finally:
    json_output = json.dumps(json_data, indent=2)
    file_path = 'citationCount.json'
    with open(file_path, 'w') as file:
        file.write(json_output)
