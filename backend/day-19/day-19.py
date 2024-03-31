import requests

# API endpoint for SpaceX latest launch
api_url = "https://api.spacexdata.com/v4/launches/latest"

# Sending a GET request
response = requests.get(api_url)

# Handling the response
if response.status_code == 200:
    # Response content as JSON
    data = response.json()
    mission_name = data["name"]
    date_precision = data["date_precision"]
    launch_date_utc = data["date_utc"]
    details = data["details"]
    cores = data["cores"]
    print(f"Mission Name: {mission_name}")
    print(f"Launch Date (UTC): {launch_date_utc}")
    print(f"Date Precision: {date_precision}")
    print(f"Details: {details}")
    print(f"Cores: {cores}")
else:
    print(f"Request failed with status code: {response.status_code}")