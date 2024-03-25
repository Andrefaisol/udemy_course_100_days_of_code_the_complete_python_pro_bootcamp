from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
# driver.get("https://www.tokopedia.com/tokoexpert/powercolor-rx-7700-xt-hellhound-oc-12gb-gddr6")
#
# price_item = driver.find_element(By.CLASS_NAME, value="price")
#
# print(f"price item is {price_item.text}")
# name_item = driver.find_element(By.XPATH, value='//*[@id="pdp_comp-product_content"]/div/h1')
# print(name_item.text)
driver.get("https://www.python.org")
upcoming_events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div')
ue_dict = {}
index = 0
list_text = upcoming_events[0].text.split("\n")
for e in range(0, 10, 2):
    ue_dict[index] = {"time": list_text[e+2], "name": list_text[e+3]}
    index += 1
print(ue_dict)
driver.quit()
