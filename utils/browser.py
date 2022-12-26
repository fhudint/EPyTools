from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

def chromeBrowser(profile):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir="+ os.getcwd() + "/profile/Chrome/" + profile)
    driver = webdriver.Chrome(options=options)
    driver.get("https://google.com")
    driver.find_element(By.NAME, "q").send_keys("acount google", Keys.RETURN)
    time.sleep(10)
    driver.close()
