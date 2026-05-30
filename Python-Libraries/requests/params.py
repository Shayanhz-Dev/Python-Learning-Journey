# Practice requests Library
# 1. get url
# 2. send params
# 3. Create timeout

import requests

url = "https://jsonplaceholder.typicode.com/users/1"
params = {
    "search": "laptop",
    "page": 2,
    "sort": "price"
}
try:
    response = requests.get(
        url,
        params=params,
        timeout=10
    )
    data = response.json()

    print(response.url)
    print(data)
    print("=========")
    print(data['email'])
except requests.RequestException as error:
    print(error)