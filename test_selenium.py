from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Connection au site Internet
driver = webdriver.Chrome()
driver.get("https://www.asiamarche.fr/")

# Acceptation des cookies
pop_up_button = driver.find_element(By.XPATH, '//*[@id=\"shopify-pc__banner__btn-accept\"]')
pop_up_button.click()


# Sélection de la barre de recherche et saisie du mot
search_bar = driver.find_element(By.XPATH, "//*[@id=\"toolbar\"]/div[3]/div[1]/div/div/form/input[3]").click()
time.sleep(3)
search_bar2 = driver.find_element(By.NAME, 'search[query]')
search_bar2.clear()
search_bar2.send_keys("brioche")
search_bar2.send_keys(Keys.ENTER)
time.sleep(3)


driver.get_screenshot_as_file("Brioches.png")

time.sleep(10)