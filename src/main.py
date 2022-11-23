import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


# Logs on the website
def login(website: str):
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
    # driver.find_element(By.CSS_SELECTOR, 'button.button button-primary g-recaptcha'.replace(' ', '.')).click()

    # Captcha
    captcha()

# Attempt to deal with captcha
def captcha():
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


# Checks how many possible pages are and gets all links from all courses
def obtain_links() -> list[list[list]]:
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
    video_links = []
    for link in course_links:
        video_links.append(obtain_links_current_course(link))
    
    return video_links

# Returns a list with links to all courses from the current page
def obtain_courses_current_page() -> list:

    # Get all course links from current page
    driver.implicitly_wait(5)
    courses = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul').find_elements(By.TAG_NAME, 'li')

    page_course_links = []
    for link in courses:
        page_course_links.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))

    return page_course_links


# Returns a list with links to all videos from a course
def obtain_links_current_course(course: str) -> list[list]:
    driver.get(course)  

    # Obtain all chapters
    driver.implicitly_wait(5)
    chapters = driver.find_element(By.CSS_SELECTOR, 'div.course-player__chapters-menu').find_elements(By.TAG_NAME, 'div')

    # Getting all links from a chapter, of all chapters
    course_links = []
    for chapter in chapters:
        chapter_elements = chapter.find_element(By.XPATH, '//*[@id="ui-id-2"]/ul').find_elements(By.TAG_NAME, 'li')

        chapter_links = []
        for element in chapter_elements:
            vid_url = element.find_element(By.XPATH, './/a').get_attribute('href')
            chapter_links.append(vid_url)
            # chapter_vids = obtain_vids_current_chapter(element)
            # chapter_links.append(chapter_vids)
            
        course_links.append(chapter_links)
    
    return course_links

# Check if the element is a vid, and return his url
def obtain_vids_current_chapter(element: WebElement) -> str:
    url = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
    element.find_element(By.TAG_NAME, 'a').find_element()



if __name__ == '__main__':
    # Obtain credentials from file
    file = open('C:\\Users\\Argnos\\Desktop\\SemanticBots\\src\\credentials.txt', 'rt')
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
    courses = obtain_links()

    for course in courses:
        for chapter in course:
            print(chapter)

    time.sleep(3)
    driver.quit()

    # https://app.web3mba.io/users/sign_in

    '''
    Revisar los links obtenidos de los cursos, puede que guarde los mismos. 
    Ademas comprobar que solo son links a videos
    '''