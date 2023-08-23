import os
import click
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

@click.command()
@click.argument("url")
@click.argument("save_directory")
def insta_scrape(url, save_directory):
    # _afxw _al46 _al47 <--- button css
    
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    # Introduce an explicit wait to ensure the element has loaded
    wait = WebDriverWait(driver, 10)
    img_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_aagv']/img")))

    image_url = img_element.get_attribute("src")
    print(image_url)

if __name__ == "__main__":
    insta_scrape()
