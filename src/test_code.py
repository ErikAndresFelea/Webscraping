'''
    Test to check if we get correct info from the navbar page

    # Page nav link test
    driver.implicitly_wait(2)
    next_page_link = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/nav/ul/li[7]')
    element = next_page_link.find_elements(By.TAG_NAME, 'a')
    print(len(element))
    
    driver.implicitly_wait(2)
    driver.get('https://app.web3mba.io/enrollments?page=5')
    next_page_link = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/nav/ul/li[7]')
    element = next_page_link.find_elements(By.TAG_NAME, 'a')
    print(len(element))
'''

'''
    Code to iterate on posible pages until there are no more

    # Looking for more pages other than the main
    

    # If there is more pages
    safety_loop = 0
    while len(next_page_exist) > 0:
        if safety_loop > 7:
            print('Infinite loop, check out')
            break



        # Move to next page and check again...
        next_page = driver.find_element(By.XPATH, '//*[@id="main-content"]/section/div/nav/ul/li[7]')
        next_page_exist = next_page.find_elements(By.TAG_NAME, 'a')
        driver.get(next_page_exist[0].get_attribute('href'))
        safety_loop += 1

    
    









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
    '''
    