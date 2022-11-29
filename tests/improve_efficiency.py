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
    # Obtain data from every unit and improve time efficiency
    chapter = driver.find_element(By.CSS_SELECTOR, 'div.course-player__chapters-menu').find_elements(By.XPATH, './*')[0]
    chapter_units = chapter.find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')

    a = time.time()
    print('Capitulo ', time.time() - a)

    # Get links of all content
    for unit in chapter_units:
        print('\tUnidad ', time.time() - a)
        unit_url = unit.find_element(By.TAG_NAME, 'a').get_attribute('href')
        unit_title = unit.find_element(By.TAG_NAME, 'a').find_elements(By.TAG_NAME, 'div')[1]
        unit_title = unit_title.get_attribute('innerHTML').split('\n')
        unit_title = unit_title[1].strip()

        print('\t\tobtener datos ', time.time() - a)
        file_type, prerequisite = filter_data(unit, a)
        print('\t\tdatos obtenidos ', time.time() - a)

        # If its video, open new tab and get url
        if file_type == 'V':
            new_tab(unit_url)
            video_url = driver.find_element(By.XPATH, '//*[@id="content-inner"]')
            video_url = video_url.find_element(By.XPATH, './div[2]/iframe').get_attribute('src')         ### Problema, tarda mucho en ejecutarse
            print('\t\t\tSegmento 1', time.time() - a)
            file.write('\t\t(' + file_type.upper() + ') ' + unit_title.upper() + ' --- > ' + video_url + '\n')
            if prerequisite:
                mark_as_completed(file_type, unit_url)
            print('\t\t\tSegmento 2', time.time() - a)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        # If text, get unit url
        else:
            if prerequisite:
                mark_as_completed(file_type, unit_url)
            print('\t\t\tSegmento 1', time.time() - a)
            file.write('\t\t(' + file_type.upper() + ') ' + unit_title.upper() + ' --- > ' + unit_url + '\n')
        print('\t\tdatos filtrados ', time.time() - a)
        print('\t\t' + file_type + '\n')
        
        
def new_tab(tab_url: str):
    ''' Open new tab with a url '''
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(tab_url)
    driver.implicitly_wait(5)


def mark_as_completed(file_type: str, unit_url: str):
    ''' Marks as completed the intended unit '''

    if file_type == 'V':
        # If none, its not completed
        is_completed = len(driver.find_elements(By.TAG_NAME, 'footer'))

        # If not completed, mark as completed
        if is_completed == 0:

            # Switch to iframe and move playbar
            iframe = driver.find_element(By.TAG_NAME, 'iframe')
            driver.switch_to.frame(iframe)

            playbar = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/div[4]/div')
            ac(driver).move_to_element(playbar).click().perform()

    elif file_type != 'E':
        new_tab(unit_url)
        
        # If one, its not completed
        if file_type == 'M':
                time.sleep(5)
        is_completed = len(driver.find_element(By.TAG_NAME, 'footer').find_elements(By.TAG_NAME, 'button'))

        if is_completed == 1:
            time.sleep(1)
            button = driver.find_element(By.XPATH, '//*[@id="course-player-footer"]/button/div')
            ac(driver).move_to_element(button).click().perform()

        driver.close()
        driver.switch_to.window(driver.window_handles[0])


def filter_data(unit: WebElement, a: any) -> tuple[str, bool]:
        ''' Gets the type of the file and if it is a prerequisite '''
        # Checking type of content. Video, text, multimedia...
        info = unit.find_element(By.XPATH, './/a/div[2]/div')
        file_type = info.get_attribute('innerHTML').split('\n')
        file_type = file_type[2].strip()

        # Checking if it is prerequisite
        print('\t\t\tSegmento 1', time.time() - a)
        driver.implicitly_wait(0.1)
        spans = info.find_elements(By.XPATH, './/span')         ### Problema, tarda mucho si el elemento no tiene span
        print('\t\t\tSegmento 2', time.time() - a)
        if len(spans) < 2:
            prerequisite = False
        else:
            span = spans[len(spans) - 1].get_attribute('innerHTML').strip()
            prerequisite = True if span == 'PRERREQUISITO' else False

        print('\t\t\tSegmento 3', time.time() - a)
        return file_type[:1], prerequisite

        
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
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=chrome_options)
    path = 'https://app.web3mba.io/'

    # Clear old data & store new data
    file = open('tests\\test_output.txt', 'w')
    file.close()
    file = open('tests\\test_output.txt', 'a')

    login(path)

    file.close()

    time.sleep(3)
    driver.quit()