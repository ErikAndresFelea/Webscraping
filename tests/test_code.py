'''
    This code opens a video link from a course and stops / plays the vid

    # Open first course
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a').click()

    # Ensure we are in the correct video. Get all links from course and click the first video
    driver.implicitly_wait(2)
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    all_links[5].click()

    # Then pause it
    driver.implicitly_wait(5)
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    time.sleep(5)
    button = driver.find_element(By.CSS_SELECTOR, 'button.w-vulcan-v2-button w-css-reset w-css-reset-tree w-css-reset-button-important'.replace(' ', '.'))
    ActionChains(driver).move_to_element(button).click().perform()
    
    
    
    
    
    
    
    
    
    def captcha():
    try:
        driver.implicitly_wait(3)
        iframe = driver.find_element(By.NAME, 'c-eta4z8mk6gko')
        driver.switch_to.frame(iframe)
    finally:
        time.sleep(10)
    if found:
        print(found)

    driver.implicitly_wait(2)
    found = driver.find_elements(By.TAG_NAME, 'iframe')
    print('Found ----> ', len(found))
    if len(found) > 0:
        WebDriverWait(driver, timeout=20).until(driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a'))
    '''
    

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


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

    ''' EDIT FROM HERE ''' 
    driver.implicitly_wait(2)
    url = driver.find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    time.sleep(5)
    url = driver.find_element(By.TAG_NAME, 'iframe').get_attribute('src')
    driver.get(url)
    time.sleep(5)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)
    

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