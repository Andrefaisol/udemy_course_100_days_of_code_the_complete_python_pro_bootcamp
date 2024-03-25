from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
end_time = time.time() + 60*5
check_time = time.time()
while time.time() < end_time:
    cookie.click()
    gold = driver.find_element(By.ID, value="money").text.replace(",", "")

    cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text.split()[2].replace(",", "")
    buy_cursor = driver.find_element(By.CSS_SELECTOR, value="#buyCursor")

    grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text.split()[2].replace(",", "")
    buy_grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma")

    factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b").text.split()[2].replace(",", "")
    buy_factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory")

    mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine b").text.split()[2].replace(",", "")
    buy_mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine")

    shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b").text.split()[2].replace(",", "")
    buy_shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment")

    alchemy = (driver.find_element(By.CSS_SELECTOR, value="div [id='buyAlchemy lab'] b").text.split()[3]
               .replace(",", ""))
    buy_alchemy = driver.find_element(By.CSS_SELECTOR, value="div [id='buyAlchemy lab']")

    if check_time < time.time():
        print("checking")
    if int(gold) > int(alchemy):
        buy_alchemy.click()
        print("buying alchemy")
    elif int(gold) > int(shipment):
        buy_shipment.click()
        print("buying shipment")
    elif int(gold) > int(mine):
        buy_mine.click()
        print("buying mine")
    elif int(gold) > int(factory):
        buy_factory.click()
        print("buying factory")
    elif int(gold) > int(grandma):
        buy_grandma.click()
        print("buying grandma")
    elif int(gold) > int(cursor):
        buy_cursor.click()
        print("buying Cursor")
    check_time += 5
