from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv

def register1():
    # Specifying incognito mode as you launch your browser[OPTIONAL]
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    option.add_argument('headless')
    # Create new Instance of Chrome in incognito mode
    browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

    # Go to desired website
    browser.get("https://www.gartner.com/en/research/magic-quadrant")
    with open('dict.csv') as csv_file:
        reader = csv.reader(csv_file)
        myDict = dict(reader)

    # # Wait 20 seconds for page to load
    # timeout = 20
    # try:
    #     # Wait until the final element [Avatar link] is loaded.
    #     # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
    #     # the last things to be loaded.
    #     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
    # except TimeoutException:
    #     print("Timed out waiting for page to load")
    #     browser.quit()


    # allLinks = browser.find_element_by_tag_name("a");
    # allLinks= browser.find_elements_by_xpath("//*[@href]")
    #
    # for  link in allLinks:
    #     browser.find_elements_by_xpath("//*[@href]")
    #     print(link)

    links = browser.find_elements_by_partial_link_text('')
    for link in links:
        print(link.get_attribute("text"))


    # # Get all of the titles for the pinned repositories
    # # We are not just getting pure titles but we are getting a selenium object
    # # with selenium elements of the titles.
    #
    # # find_elements_by_xpath - Returns an array of selenium objects.
    # titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")
    #
    # # List Comprehension to get the actual repo titles and not the selenium objects.
    # titles = [x.text for x in titles_element]
    #
    # # print response in terminal
    # print('TITLES:')
    # print(titles, '\n')
    #
    #
    # # Get all of the pinned repo languages
    # language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
    # languages = [x.text for x in language_element] # same concept as for-loop/ list-comprehension above.
    #
    # # print response in terminal
    # print("LANGUAGES:")
    # print(languages, '\n')
    #
    # # Pair each title with its corresponding language using zip function and print each pair
    # for title, language in zip(titles, languages):
    #     print("RepoName : Language")
    #     print(title + ": " + language, '\n')

if __name__ == '__main__':
    register1()