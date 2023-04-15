from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Wait for the "New Chat" button to become clickable
wait = WebDriverWait(driver, 600)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[3]/div")))

# User has scanned the QR code and is now logged in
print("User has logged in to WhatsApp Web")
