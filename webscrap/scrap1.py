import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://www.udemy.com/courses/search/?src=ukw&q=c+programming"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the website
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a file to save the HTML content
    with open('website_content.txt', 'w') as file:
        # Write the HTML content into the file
        file.write(soup.prettify())
else:
    print(f"Failed to fetch the website. Status code: {response.status_code}")