# Practice requests
# 1. Set and Get cookie
# 2. Error handling 

import requests

SET_COOKIE_URL = "https://httpbin.org/cookies/set/user/shayan"
GET_COOKIE_URL = "https://httpbin.org/cookies"

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

try:
    # Request 1: Set Cookie
    response = session.get(
        SET_COOKIE_URL,
        timeout=10
    )

    response.raise_for_status()

    print("Cookies stored in session:")
    print(session.cookies.get_dict())

    # Request 2: Send Cookie back
    response = session.get(
        GET_COOKIE_URL,
        timeout=10
    )

    response.raise_for_status()

    print("\nCookies received by server:")
    print(response.json())

except requests.exceptions.Timeout:
    print("Timeout Error")

except requests.exceptions.ConnectionError:
    print("Connection Error")

except requests.exceptions.HTTPError as error:
    print(f"HTTP Error: {error}")

except requests.exceptions.RequestException as error:
    print(f"Request Error: {error}")