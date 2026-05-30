# Practice requests library
# Send Payload

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My First Post",
    "body": "Hello World",
    "userId": 1
}

try:
    response = requests.post(
        url,
        json=payload,
        timeout=10
    )

    print(response.status_code)

    data = response.json()

    print(data)

except requests.RequestException as error:
    print(error)