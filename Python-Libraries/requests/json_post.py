# Practice requests library
# Send json payload
# Checking status with raise_for_status

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My First Post",
    "body": "Hello World",
    "userId": 1
}

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=10
    )
    response.raise_for_status()
    data = response.json()
    print(data)

except requests.RequestException as error:
    print(error)