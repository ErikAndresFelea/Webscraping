import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as ac


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
    units = driver.find_element(By.XPATH, '//*[@id="ui-id-2"]/ul').find_elements(By.TAG_NAME, 'li')
    for unit in units:
        unit_url = unit.find_element(By.TAG_NAME, 'a').get_attribute('href')

        file_type = unit.find_element(By.XPATH, './/a/div[2]/div').get_attribute('innerHTML').split('\n')
        file_type = file_type[2].strip()

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(unit_url)

        if file_type[:1] == 'V':
            # If none, its not completed
            driver.implicitly_wait(5)
            is_completed = len(driver.find_elements(By.TAG_NAME, 'footer'))

            ''' Code already done here '''
            
            # If not completed, mark as completed
            if is_completed == 0:

                # Switch to iframe and move playbar
                iframe = driver.find_element(By.TAG_NAME, 'iframe')
                driver.switch_to.frame(iframe)

                playbar = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[4]/div')
                ac(driver).move_to_element(playbar).click().perform()

                driver.switch_to.window(driver.window_handles[0])


        else:
            # If one, its not completed
            is_completed = len(driver.find_element(By.TAG_NAME, 'footer').find_elements(By.TAG_NAME, 'button'))

            ''' Code already done here '''

            if is_completed == 1:
                driver.find_element(By.TAG_NAME, 'button').click()


        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        
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