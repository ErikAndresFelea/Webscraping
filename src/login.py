import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException

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
    # captcha()

    # Close unused tabs
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Open first course
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a').click()

    # Wait and pause video
    driver.implicitly_wait(5)
    iframe = driver.find_element(By.ID, 'iframe-ember1709')
    driver.switch_to.frame(iframe)
    time.sleep(4)
    button = driver.find_element(By.CSS_SELECTOR, 'button.w-vulcan-v2-button w-css-reset w-css-reset-tree w-css-reset-button-important'.replace(' ', '.'))
    ActionChains(driver).move_to_element(button).click().perform()
    

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
    try:
        iframe = driver.find_element(By.NAME, 'c-eta4z8mk6gko')
        captcha = WebDriverWait(driver, timeout=2).until(ec.visibility_of_element_located((By.TAG_NAME, 'iframe')))
        if captcha:
            time.sleep(10)
    finally:
        pass
    # driver.implicitly_wait(1)
    # if driver.find_element(By.TAG_NAME, 'iframe').is_displayed():
    #     WebDriverWait(driver, timeout=10).until(driver.find_element(By.XPATH, '//*[@id="sign_in_98ad691a24"]/div[5]/button').is_displayed)
        # time.sleep(10)
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

    # https://app.web3mba.io/users/sign_in