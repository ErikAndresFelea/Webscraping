import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def login(website: str):
    ''' Logs on the website '''
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
    captcha()


def captcha():
    '''Attempt to deal with captcha'''
    '''
    try:
        driver.implicitly_wait(3)
        iframe = driver.find_element(By.NAME, 'c-eta4z8mk6gko')
        driver.switch_to.frame(iframe)
    finally:
        time.sleep(10)
    if found:
        print(found)
    '''
    time.sleep(10)

    '''
    driver.implicitly_wait(2)
    found = driver.find_elements(By.TAG_NAME, 'iframe')
    print('Found ----> ', len(found))
    if len(found) > 0:
        WebDriverWait(driver, timeout=20).until(driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul/li[1]/div/a'))
    '''


def obtain_links():
    '''Checks how many possible pages are and gets the links from all courses'''    
    course_links = []

    # Visits every page with courses
    page_exists = True
    while page_exists:
        # For every page obtains links to all courses
        page_links = obtain_courses_current_page()
        course_links.extend(page_links)
        
        # Seachs for additional page
        page_elem = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/nav/ul/li[7]')
        link_elem = page_elem.find_elements(By.TAG_NAME, 'a')
        
        # If there is no other page, end loop, if yes, jump
        if len(link_elem) < 1: 
            page_exists = False
        else:
            next_path = link_elem[0].get_attribute('href')  
            driver.get(next_path)
             
    # And for every course gets all links

    for link in course_links:
        obtain_chapters_current_course(link)
    

def obtain_courses_current_page() -> list:
    '''Returns a list with the links of all courses from the current page'''
    # Get all course links from current page
    driver.implicitly_wait(5)
    courses = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul').find_elements(By.TAG_NAME, 'li')

    page_course_links = []
    for link in courses:
        page_course_links.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))

    return page_course_links


def obtain_chapters_current_course(course: str):
    '''Searches for units of all chapters'''
    driver.get(course)  
    file.write('Course --- > ' + driver.title + ' | ' + course + '\n')
    
    # Obtain all chapters of the current course
    driver.implicitly_wait(5)
    chapters = driver.find_element(By.CSS_SELECTOR, 'div.course-player__chapters-menu').find_elements(By.XPATH, './*')
    
    # For every chapter of a course
    for chapter in chapters:
        obtain_units_current_chapter(chapter)

    file.write('\n\n\n')


def obtain_units_current_chapter(chapter: WebElement):
    '''Stores links from all units'''
    chapter_title = chapter.find_element(By.TAG_NAME, 'h2').text
    file.write('\tChapter --- > ' + chapter_title + '\n')

    chapter_units = chapter.find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')
    
    # Get links of all content
    for unit in chapter_units:
        unit_url = unit.find_element(By.TAG_NAME, 'a').get_attribute('href')
        unit_title = unit.find_element(By.TAG_NAME, 'a').find_elements(By.TAG_NAME, 'dive')[1]
        unit_title = unit_title.get_attribute('innerHTML')[1].strip()

        # Checking if it is video or text. 2nd element has the text "Video" or "Text"
        file_type = unit.find_element(By.XPATH, './/a/div[2]/div').get_attribute('innerHTML').split('\n')
        file_type = file_type[2].strip()

        # If its video, open new tab and get url
        if file_type[:1] == 'V':
            driver.get(unit_url)
            driver.implicitly_wait(2)
            video_link = driver.find_element(By.TAG_NAME, 'iframe').get_attribute('src')
            file.write('\t\tVIDEO --- > ' + video_link + '\n')

        # If text, get unit url
        else:
            file.write('\t\t(' + file_type.upper() + ') ' + unit_title.upper + ' --- > ' + unit_url + '\n')
        






if __name__ == '__main__':
    # Obtain credentials from file
    file = open('src\\resources\\credentials.txt', 'rt')
    credentials = []
    for line in file:
        credentials.append(line)
    username = credentials[0]
    passwd = credentials[1]
    file.close()

    # Start driver on desired website
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    path = 'https://app.web3mba.io/'

    # Clear old data & store new data
    file = open('src\\store_info.txt', 'w')
    file.close()
    file = open('src\\store_info.txt', 'a')

    login(path)
    obtain_links()

    file.close()

    time.sleep(3)
    driver.quit()
