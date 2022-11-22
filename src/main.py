import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    ### driver.find_element(By.CSS_SELECTOR, 'button.button button-primary g-recaptcha'.replace(' ', '.')).click()

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
def obtain_links() -> list:
    all_links = []

    # Searches on all posible course pages and stores links on all_links
    page_exists = True
    while page_exists:
        ### print('Total amount of links ---> ', len(all_links))
        ### driver.implicitly_wait(5)

        # Seachs for additional page, if exists, jump
        next_url = False
        next_path = ''   
        page_elem = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/nav/ul/li[7]')
        link_elem = page_elem.find_elements(By.TAG_NAME, 'a')
        
        # If there is no other page, end loop, if yes, save url
        if len(link_elem) < 1: 
            page_exists = False
        else:
            next_url = True
            next_path = link_elem[0].get_attribute('href')  
             
        # For every page obtains links to all courses
        courses = obtain_courses_current_page()

        # And for every course gets all links
        for link in courses:
            all_links.append(obtain_vids_current_course(link))

        # If there is another page with courses, jump there
        if next_url:
            driver.get(next_path)
            

# Returns a list with links to all courses from the current page
def obtain_courses_current_page() -> list:

    # Get all course links from current page
    driver.implicitly_wait(5)
    courses = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/ul').find_elements(By.TAG_NAME, 'li')

    all_course_links = []
    for link in courses:
        all_course_links.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))

    return all_course_links


# Returns a list with links to all videos from a course
def obtain_vids_current_course(course: str) -> list:

    # For every course get all vids links
    driver.get(course)

    # Getting all links from a course
    driver.implicitly_wait(5)
    course_links = driver.find_element(By.XPATH, '//*[@id="ui-id-2"]/ul').find_elements(By.TAG_NAME, 'li')

    all_links = []
    for link in course_links:
        all_links.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))


# Process the links obtained to retain only the vids
def proces_links(links: list[list]):
    
    for list in links:
        for link in list:
            pass


if __name__ == '__main__':
    # Obtain credentials from file
    file = open('C:\\Users\\remoA\\Desktop\\SemanticBots\\src\\credentials.txt', 'rt')
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

    time.sleep(3)
    driver.quit()

    # https://app.web3mba.io/users/sign_in

    '''
    Revisar los links obtenidos de los cursos, puede que no coja todos. 
    Ademas comprobar que solo son links a videos
    '''