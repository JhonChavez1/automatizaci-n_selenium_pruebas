from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.udemy.com/join/login-popup/?next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&passwordredirect=True&skip_suggest=1")
driver.maximize_window()

correo = driver.find_element(By.ID, "email")
correo2 = driver.find_element(By.NAME, "email")
correo3 = driver.find_element(By.CLASS_NAME, "form-control")

# ESTE CÓDIGO NO SE EJECUTA

