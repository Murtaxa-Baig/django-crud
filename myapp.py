import requests
import json

URL = "http://127.0.0.1:8000/studentapi"

def get_data(id=None):
    try:
        params = {"id": id} if id is not None else {}
        r = requests.get(url=URL, params=params)
        r.raise_for_status()  # Raise an exception for HTTP errors
        data = r.json()
        print("data is", data)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")

get_data(1)
get_data()
