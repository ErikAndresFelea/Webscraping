import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.wait import WebDriverWait


# Logs on the website
def login(website: str):
    ''' DONT EDIT '''
    # Open web page
    driver.get(website)

    # Accept coockies & open login tab
    driver.implicitly_wait(1)
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonAccept').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Iniciar sesi').click()

    # Login with credentials
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="user[email]"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="user[password]"]').send_keys(passwd)
    driver.find_element(By.CSS_SELECTOR, 'button.button button-primary g-recaptcha'.replace(' ', '.')).click()

    # Captcha
    time.sleep(10)

    # Get first course link
    driver.implicitly_wait(2)
    courses = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul').find_elements(By.TAG_NAME, 'li')
    first_course = courses[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.get(first_course)
    driver.implicitly_wait(5)

    ''' EDIT FROM HERE ''' 
    div = driver.find_element(By.XPATH, '//*[@id="ember823"]/div[2]/div')
    spans = div.find_elements(By.TAG_NAME, 'span')
    print('Spans: ', len(spans))

    span = spans[len(spans) - 1].get_attribute('innerHTML').strip()
    print(span)

        
''' DONT EDIT '''
if __name__ == '__main__':
    # Obtain credentials from file
    file = open('src\\resources\\credentials.txt', 'rt')
    credentials = []
    for line in file:
        credentials.append(line)
    username = credentials[0]
    passwd = credentials[1]

    # Start driver on desired website
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    path = 'https://app.web3mba.io/'

    login(path)

    time.sleep(3)
    driver.quit()