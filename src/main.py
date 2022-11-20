import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

path1 = 'https://web3mba.io/'
path2 = 'https://app.web3mba.io/users/sign_in'


def login():
    # Open web page
    driver.get(path2)

    # Accept coockies & open login tab
    driver.implicitly_wait(1)
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonAccept').click()

    # Cambiamos de tab & Login
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="user[email]"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="user[password]"]').send_keys(passwd)
    driver.find_element(By.CSS_SELECTOR, 'button.button button-primary g-recaptcha'.replace(' ', '.')).click()

    # Captcha
    captcha()

    # Abrimos primer curso
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a').click()

    # Esperamos y pausamos
    time.sleep(5)
    driver.find_element(By.TAG_NAME, 'video').click()
    time.sleep(0.1)


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