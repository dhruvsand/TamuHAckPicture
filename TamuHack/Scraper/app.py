from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv


app = Flask(__name__)
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument('headless')
# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

# Go to desired website
browser.get("https://www.gartner.com/en/research/magic-quadrant")

@app.route('/<title>')
def hello_world(title):
    title = "Access Management"
    links = browser.find_elements_by_partial_link_text('')
    for link in links:
        if title in link.get_attribute("text"):
            browser.get(link.get_attribute("href"))
            print('HI World!' + browser.find_element_by_class_name("summary"))
            return browser.find_element_by_tag_name("p")





    return 'Hello World!'+title


if __name__ == '__main__':
    app.run()
