import requests
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup, element, ResultSet
from time import sleep

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Define Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
# Add more options here if needed

# Define paths
user_home_dir = os.path.expanduser("~")
chrome_binary_path = os.path.join(user_home_dir, "chrome-linux64", "chrome")
chromedriver_path = os.path.join(user_home_dir, "chromedriver-linux64", "chromedriver")

# Set binary location and service
chrome_options.binary_location = chrome_binary_path
service = Service(chromedriver_path)


def get_car_data(base_url:str) :

    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    results:ResultSet[element.Tag] = soup.findAll("div", {"data-cmp" : "itemCard"})

    links = []
    output_list = []

    print(len(results))

    for result in results :
        link_element = result.find("a", {"data-cmp" : "link"}, href=True)
        if isinstance(link_element, element.Tag) and link_element['href'][0] == "/":
            links.append(link_element['href'])

    print(len(links))
    # Initialize Chrome WebDriver
    for link in links:
        try : 
            with webdriver.Chrome(service=service, options=chrome_options) as browser:

                browser.get(f"https://www.autotrader.com{link}")
                html = browser.page_source
                soup = BeautifulSoup(html, "html.parser")
                sleep(30)
                title = soup.find("h1", {"data-cmp" : "heading"}).text
                pricing = soup.find("span", {"data-cmp" : "firstPrice"}).text
                feature_list = []
                features = soup.find("ul", {"data-cmp" : "listColumns"})
                if isinstance(features, element.Tag) : 
                    for feature in features.find_all(recursive=False):
                        feature_list.append(feature.text)

                description = str(soup.find("div", {"data-cmp" : "seeMore"}))
                output_list.append(f"Title: {title} \nPrice: {pricing} \nFeatures: {feature_list} \nDescription: {description} \n")
                print(output_list)
        except Exception as e :
            print(f"Error {e}")
            break

    return output_list
