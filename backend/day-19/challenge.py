import requests

api_url =  "https://api.spacexdata.com/v5/launches/latest"

# Sending a GET request
response = requests.get(api_url)


#handling the response
if response.status_code == 200:
    # response content as json
    data = response.json()
    title = data.get("title", "No title available")  # Check if "title" key exists, provide default value if not
    body = data.get("body", "No body available")  # Check if "body" key exists, provide default value if not
    print(f"Title: {title}")
    print(f"Body: {body}")
else:
    print(f"Request failed with status code:  {response.status_code}")