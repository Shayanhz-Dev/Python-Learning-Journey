# Practice downloading a file using the requests library in Python
# 1. Set URL and filename
# 2. Create headers
# 3. Send GET request and save file

import requests

url = "https://httpbin.org/image/jpeg"

filename = 'test.jpg'
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
    response.raise_for_status()
    print(response.status_code)
    with open(filename, "wb") as file:
        file.write(response.content)
    print("Download completed!")
except requests.RequestException as error:
    print(error)