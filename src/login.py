import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


def login():
    # Open web page
    driver.get(path)

    # Accept coockies & open login tab
    driver.implicitly_wait(1)
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonAccept').click()

    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/nav/ul/li[11]/a').click()


    # Swap tab and login
    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="user[email]"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="user[password]"]').send_keys(passwd)
    driver.find_element(By.CSS_SELECTOR, 'button.button button-primary g-recaptcha'.replace(' ', '.')).click()

    # Captcha
    time.sleep(10)
    # captcha()

    # Close unused tabs
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Open first course
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a').click()

    # Ensure we are in the correct video
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
        # driver.implicitly_wait(3)
        time.sleep(30)
        iframe = driver.find_element(By.NAME, 'c-eta4z8mk6gko')
        driver.switch_to.frame(iframe)
    finally:
        time.sleep(10)


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    path = 'https://web3mba.io/'

    file = open('credentials.txt', 'rt')
    credentials = []
    for line in file:
        credentials.append(line)
    username = credentials[0]
    passwd = credentials[1]

    login()

    time.sleep(3)
    driver.quit()

    # https://app.web3mba.io/users/sign_in