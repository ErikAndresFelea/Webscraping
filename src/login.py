import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

username = 'hugoa.ferrer@semanticbots.com'
passwd = 'SemanticBots'
path1 = 'https://web3mba.io/'
path2 = 'https://app.web3mba.io/users/sign_in'


def login_path_1():
    # Open web page
    driver.get(path1)

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
    captcha()

    # Close unused tabs
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Open first course
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a').click()

    # Wait and pause video
    ### time.sleep(5)
    ### driver.find_element(By.TAG_NAME, 'video').click()
    time.sleep(0.1)


def login_path_2():
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

    '''
    # For some reason first login does not work
    time.sleep(10)
    
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="user[email]"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="user[password]"]').send_keys(passwd)
    driver.find_element(By.CSS_SELECTOR, 'button.button button-primary g-recaptcha'.replace(' ', '.')).click()
    '''

    # Captcha
    captcha()

    # Abrimos primer curso
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a').click()

    # Esperamos y pausamos
    ### time.sleep(5)
    ### driver.find_element(By.TAG_NAME, 'video').click()
    time.sleep(0.1)


def captcha():
    driver.implicitly_wait(1)
    if driver.find_element(By.TAG_NAME, 'iframe').is_displayed():
        time.sleep(10)
        # driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
        # driver.find_element(By.ID, 'recaptcha-verify-button').click()
        # 
        # driver.implicitly_wait(1)
        # driver.switch_to.window(driver.window_handles[0])

    '''
    try:
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)
        time.sleep(10)
        driver.find_element(By.ID, 'recaptcha-verify-button').click()
        driver.switch_to.window(driver.window_handle[0])
    except:
        NoSuchElementException
    '''    


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)

    login_path_1()
    # login_path_2()

    time.sleep(5)
    driver.quit()