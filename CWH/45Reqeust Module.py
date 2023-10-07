import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)