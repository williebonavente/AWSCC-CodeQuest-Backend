"""
    Query String parameters
"""

import requests

# Base API URL
base_url = " https://jsonplaceholder.typicode.com/posts"

# Query parameters
params = {
    "category": "electronics",
    "sort": "desc",
    "page": 1,
    "per_page": 10
}


# Adding query parameters to the URL
response = requests.get(base_url, params=params)

# The full URL with query parameters is constructed automatically
if response.status_code == 200:
    products_data = response.json() # Assuming the response contains JSON data
    print("Products Data:", products_data)
else:
    print("API request failed with status code:",response.status_code)
    