from selenium import webdriver
import time


controlador = webdriver.Chrome()
controlador.get("https://www.udemy.com/join/login-popup/?next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F&passwordredirect=True&skip_suggest=1")

usuario = controlador.find_element(By.CLASS_NAME,"form-control")