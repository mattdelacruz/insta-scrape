import os
import click
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from browsermobproxy import Server
@click.command()
@click.argument("url")
@click.argument("save_directory")
def insta_scrape(url, save_directory):
    # _afxw _al46 _al47 <--- button css
    # <button aria-label="Next" class=" _afxw _al46 _al47" tabindex="-1"><div class=" _9zm2"></div></button>
    #<div class=" _9zm2"></div>
    
    media_links = []
    server = Server("browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
    server.start()
    proxy = server.create_proxy()
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--proxy-server={0}".format(proxy.proxy))
    
    driver = webdriver.Chrome(options=options)
    proxy.new_har("chrome_requests")
    
    driver.get(url)
    
    driver.implicitly_wait(10)
        
    try:
        print("getting requests...")
        get_requests = [entry['request']['url'] for entry in proxy.har['log']['entries'] if entry['request']['method'] == 'GET']
    except requests.exceptions.JSONDecodeError:
        print("Failed to retrieve HAR data as JSON from BrowserMob proxy")
        get_requests = []
    
    for r in get_requests:
        print(r)
    
    driver.quit()
    server.stop()

if __name__ == "__main__":
    insta_scrape()
    # WebDriverWait(driver, 10)
    
    # proxy.new_har("instagram", options={'captureHeaders' : True, 'captureContent': True})
    # driver.get(url)

    # for entry in har_data['log']['entries']:
    #     url = entry['request']['url']
    #     if '.jpg' in url or '.mp4' in url:
    #         print(url)

    # Introduce an explicit wait to ensure the element has loaded
    # wait = WebDriverWait(driver, 10)
    
    # if (is_element)
    # img_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_aagv']/img")))

    # image_url = img_element.get_attribute("src")
    # print(image_url)