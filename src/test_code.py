'''
    Code to iterate on posible pages until there are no more

     

    









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
    