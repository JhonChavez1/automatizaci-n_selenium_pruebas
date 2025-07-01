from selenium import webdriver
from selenium.webdriver.common.by import By
import time


controlador = webdriver.Chrome()
controlador.get("https://www.udemy.com/join/login-popup/?next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&passwordredirect=True&skip_suggest=1")
time.sleep(1)

usuario = controlador.find_element(By.CLASS_NAME,"-ud-compact-form-control")
time.sleep(2)
clave = controlador.find_element(By.CLASS_NAME,"password-form-group--password-input--yB71S")
time.sleep(2)

usuario.send_keys("jhonf.6520@gmail.com")
time.sleep(2)
clave.send_keys("Jf92092666940")
time.sleep(2)

boton = controlador.find_element(By.CLASS_NAME,"ud-text-input")
boton.click()
time.sleep(3)

controlador.quit()


