from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.udemy.com/join/login-popup/?next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&passwordredirect=True&skip_suggest=1")
time.sleep(3)

link_recuperar = driver.find_element(By.LINK_TEXT, "He olvidado la contraseña")
link_recuperar.click()
time.sleep(10)

# el catchap impide la automatización de pruebas
correo = driver.find_element(By.ID, "form-group--1")
correo.send_keys("jhonf.6520@gmail.com")
time.sleep(3)


validar = driver.find_element(By.ID, "cf-chl-widget-8zaxr")



driver.quit()