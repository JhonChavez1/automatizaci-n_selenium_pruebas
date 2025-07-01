from selenium import webdriver
from selenium.webdriver.common.by import By
import time


controlador = webdriver.Chrome()

controlador.get("https://www.udemy.com/join/login-popup/?next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&passwordredirect=True&skip_suggest=1")
time.sleep(2)

usuario = controlador.find_element(By.NAME,"email")
time.sleep(2)
clave = controlador.find_element(By.NAME, "password")
time.sleep(2)

usuario.send_keys("jhonf.6520@gmail.com")
time.sleep(2)
clave.send_keys("Jf92092666940")
time.sleep(2)

boton = controlador.find_element(By.XPATH,"//button[contains(@class, 'helpers--auth-submit-button--W3Tqk')]")
boton.click()

