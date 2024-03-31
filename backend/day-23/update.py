import requests
import json

task_id = 3  # replace with the ID of the task you want to update
url = f"http://localhost:5000/api/tasks/{task_id}"
headers = {'Content-Type': 'application/json'}
data = {'title': 'Inupdate na ako yess!'}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(response.json())