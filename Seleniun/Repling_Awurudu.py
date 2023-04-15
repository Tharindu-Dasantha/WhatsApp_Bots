from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

# Wait for the search bar to appear
search_bar = wait.until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]")))

print("The What'sApp is running")

# the things to check on a message
pattern = re.compile(r"awurudu|new|year|happy")


while True:
    try:
        last_msg = driver.find_elements(By.CLASS_NAME, "_1pJ9J")[-1]
        msg = last_msg.find_element(By.CLASS_NAME, "_2KKXC").text
        if pattern.search(msg):
            reply_box = driver.find_element(By.CLASS_NAME, "_1VZX7")
            reply_box.send_keys("එසේම වේවා")
            reply_box.send_keys(Keys.RETURN)
    except IndexError:
        continue

driver.quit()
