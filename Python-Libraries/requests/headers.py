# Practice requests 
# Get URL
# Create headers
# Create timeout

import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    data = response.json()
    print(data)

except requests.RequestException as error:
    print(error)
