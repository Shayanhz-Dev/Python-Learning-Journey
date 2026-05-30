# Practice requests library
# Error handling practice

import requests

url = "https://wrong-site-123456.com"

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
    print("Request Successful")
    
except requests.exceptions.Timeout:
    print("Timeout Error")

except requests.exceptions.ConnectionError:
    print("Connection Error")

except requests.exceptions.HTTPError:
    print("HTTP Error")

except requests.RequestException as error:
    print(error)
