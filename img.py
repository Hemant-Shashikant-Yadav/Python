import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from PIL import Image

def save_images(url, output_folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Extract image URLs
    img_tags = soup.find_all('img')
    # print(img_tags)
    # print(type(img_tags))
    img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]
    # print(img_urls)
    # print(type(img_urls))
    # Download and save images
    for img_url in img_urls:
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(output_folder, os.path.basename(urlparse(img_url).path))
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)
            print(f"Image saved: {img_name}")
        except Exception as e:
            print(f"Error downloading image from {img_url}: {e}")

if __name__ == "__main__":
    website_url = " https://www.whatsapp.com"
    output_folder = "Y:\Coding\Python-1"
    save_images(website_url, output_folder)
