from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")
fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sign_up = driver.find_element(By.CSS_SELECTOR, value="button")
fname.send_keys("Andre")
lname.send_keys("Faisol")
email.send_keys("freedom.boy211@gmail.com")
sign_up.click()

