import requests

task_id = 1  # replace with the ID of the task you want to delete
url = f"http://localhost:5000/api/tasks/{task_id}"

response = requests.delete(url)

print(response.json())