from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.asiamarche.fr/")
time.sleep(7)
pop_up_button = driver.find_element(By.XPATH, '//*[@id=\"shopify-pc__banner__btn-accept\"]')
pop_up_button.click()

time.sleep(3)
search_bar = driver.find_element(By.XPATH, "//*[@id=\"toolbar\"]/div[3]/div[1]/div/div/form/input[3]")

time.sleep(3)
search_bar2 = driver.find_element(By.XPATH, '//*[@id=\"dfd-searchbox-id-n2-fp-input\"]')
search_bar.send_keys("brioche")

time.sleep(20)


driver.get_screenshot_as_file("Brioches.png")