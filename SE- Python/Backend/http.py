import requests

url = "https://www.example.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

# Print the status code and response content
print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.text[:500]}")  # Printing the first 500 characters


"""

curl -X POST -H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_TOKEN_HERE" \
-d '{"name": "John", "age": 30}' \
https://api.example.com/users



curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
-H "Accept: application/json" \
https://www.example.com

"""

"""
What Is the User-Agent Header?
The User-Agent header is a string that identifies the client software making the HTTP request. This header typically contains information about the browser, operating system, and device being used. Servers can use this information to tailor the content they deliver based on the client’s capabilities or to gather analytics about the types of clients accessing the site.

"""









import requests
import json

url = "https://api.example.com/users"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_TOKEN_HERE'
}

data = {
    "name": "John",
    "age": 30
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the status code and response content
print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.text}")

