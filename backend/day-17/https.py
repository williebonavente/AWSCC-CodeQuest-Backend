# Challenge time Day 17
import requests

# base url
base_url = "https://jsonplaceholder.typicode.com/"

# Resource Path
resource_path = "/users"

# Parameters
parameters = {"status": "active", "sort": "desc"}

# Construct the complete endpoint URL
endpoint_url = base_url + resource_path

if parameters:
    endpoint_url += "?" + "&".join([f"{key}={value}" for key, value in parameters.items()])

# Sending a GET request to the constructed endpoint URL
response = requests.get("https://jsonplaceholder.typicode.com/")

if response == 200:
    print("Request Successful")

else:
    print("Request Failed")
# Handle the Response as needed
print("API Response:", response.text)

"""
Needed More Reading.
"""