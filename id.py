from selenium import webdriver
from selenium.webdriver.common.by import By
import time
time.sleep

controlador = webdriver.Chrome()
controlador.get("https://www.udemy.com/join/login-popup/?next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&passwordredirect=True&skip_suggest=1")

usuario = controlador.find_element(By.ID,'form-group--1')
time.sleep(3)
clave = controlador.find_element(By.ID,"form-group--3")
time.sleep(3)

usuario.send_keys("jhonf.6520@gmail.com")
clave.send_keys("Jf92092666940")
time.sleep(2)

boton = controlador.find_element(By.XPATH, "//button[contains(@class, 'helpers--auth-submit-button--W3Tqk')]")
boton.click()
time.sleep(3)

controlador.quit()