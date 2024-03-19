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

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
    raise
except requests.exceptions.ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')
    raise
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')
    raise
except requests.exceptions.RequestException as req_err:
    print(f'Request error occurred: {req_err}')
    raise
except Exception as e:
    print(f'An error occurred: {e}')
    raise
finally:
    json_output = json.dumps(json_data, indent=2)
    with open('./scripts/citationCount.json', 'w') as file:
        file.write(json_output)
