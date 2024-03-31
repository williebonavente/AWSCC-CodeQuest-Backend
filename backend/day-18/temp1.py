"""
HEADERS
"""

import requests


# Base API url
base_url =  "https://jsonplaceholder.typicode.com/posts"

# Custom headers
headers = {
    "User-Agent": "MyCustomApp/1.0",
    "Authorization": "Bearer your-access-token"
}

# Sending a GET request with custom headers
response = requests.get(base_url, headers= headers)

# Display response and headers
print("Response Status Code:", response.status_code)
print("Response Headers: ")

for key, value in response.headers.items():
    print("f{key}: {value}")
    
# Response content (in this case, it's just an example)
print("Response Content:", response.text)