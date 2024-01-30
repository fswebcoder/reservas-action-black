from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def reservar(url):
    driver = webdriver.Firefox()
    driver.get(url)

