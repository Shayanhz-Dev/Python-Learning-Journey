# Practice request libraries
# 1. Get url
# 2. Loading data in json 
# 3. Cheacking status

import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)
data = response.json()

print(data['name'], data['email'], data['address']['city'])
print(response.status_code)