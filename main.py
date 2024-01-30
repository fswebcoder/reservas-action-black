from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from reservas import reservar

driver = webdriver.Firefox()
driver.get("https://www.actionblack.co/reservas")
elem = driver.find_element(By.CLASS_NAME, 'reservas_select__YsLUn')
print(elem.text)
elem.click()
direccion = driver.find_element(By.XPATH, '/html/body/div/main/section/div[1]/ul/li[7]/a')
reservar(direccion.get_attribute('href'))


# assert "No results found." not in driver.page_source
# driver.close()