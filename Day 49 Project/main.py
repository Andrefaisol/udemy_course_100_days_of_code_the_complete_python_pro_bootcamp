from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = ("https://www.linkedin.com")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(15)
email = driver.find_element(By.NAME, value="session_key")
email.send_keys("") # your linkedin email
pw = driver.find_element(By.NAME, value="session_password")
pw.send_keys("") # your linkedin password
press_log = driver.find_element(By.XPATH, value="//*[@id='main-content']/section[1]/div/div/form/div[2]/button")
press_log.click()
print("press login")
time.sleep(10)
search = driver.find_element(By.XPATH, value="//*[@id='global-nav-typeahead']/input")
search.send_keys("Python Developer", Keys.ENTER)
time.sleep(5)
job = driver.find_element(By.XPATH, value="//*[@id='search-reusables__filters-bar']/ul/li[1]/button")
job.click()
time.sleep(5)

easy = driver.find_element(By.XPATH, value="//*[@id='search-reusables__filters-bar']/ul/li[7]/div")
easy.click()
time.sleep(3)
list_job = driver.find_elements(By.CSS_SELECTOR, value="div div a strong")
for e in list_job:
    time.sleep(4)
    e.click()
    time.sleep(4)
    save = driver.find_element(By.XPATH, value="//*[@id='main']/div/div[2]/div[2]/div/div[2]/div/div[1]"
                                               "/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]")
    save.click()



