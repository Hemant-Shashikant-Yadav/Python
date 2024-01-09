import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def save_images_from_youtube(url, output_folder):
    # Set up a headless browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Give the page some time to load (adjust as needed)

        # Scroll down to load more content (you may need to adjust the number of scrolls)
        for _ in range(3):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        # Find and save images
        img_tags = driver.find_elements_by_tag_name('img')
        for img_tag in img_tags:
            img_url = img_tag.get_attribute('src')
            if img_url:
                img_data = requests.get(img_url).content
                img_name = os.path.join(output_folder, os.path.basename(urlparse(img_url).path))
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Image saved: {img_name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/"
    output_folder = "Y:\Coding\Python-1"
    save_images_from_youtube(youtube_url, output_folder)
