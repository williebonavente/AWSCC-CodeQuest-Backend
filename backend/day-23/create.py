import requests
import json

url = "http://localhost:5000/api/tasks"
headers = {'Content-Type': 'application/json'}
data = {'title': 'ULOls.'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())