from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 
import time

elchofer = webdriver.Chrome(r"D:\marioAdair\Universidad\SeptimoSemestre\testing\chromedriver_win32/chromedriver.exe")
elchofer.get("https://www.demoblaze.com/index.html")
alert = Alert(elchofer)


#### Registro
def registro():
	elchofer.find_element(By.ID, "signin2").click()
	time.sleep(3)
	elchofer.find_element(By.ID, "sign-username").send_keys("mariotest123456")
	elchofer.find_element(By.ID, "sign-password").send_keys("mario12345")
	time.sleep(2)
	elchofer.find_element(By.XPATH, "//button[contains(text(),\'Sign up\')]").click()
	time.sleep(3)
	alert.accept()  

########Login#####
def login():
	elchofer.find_element(By.ID, "login2").click()
	time.sleep(3)
	elchofer.find_element(By.ID, "loginusername").send_keys("mariotest123")
	elchofer.find_element(By.ID, "loginpassword").send_keys("mario12345")
	time.sleep(2)
	elchofer.find_element(By.XPATH, "//button[contains(text(),\'Log in\')]").click()
	time.sleep(2)

########Carrito de compras#####
def comprar(tipo, producto):
	elchofer.find_element(By.XPATH, "//a[contains(text(),\'" + tipo + "\')]").click()
	time.sleep(2)

	elchofer.find_element(By.XPATH, "//a[contains(text(),\'" + producto + "\')]").click()
	time.sleep(3)

	elchofer.find_element(By.XPATH, "//a[contains(text(),\'Add to cart\')]").click()
	time.sleep(2)
	alert.accept() 
	time.sleep(2)

	elchofer.find_element(By.XPATH, "//a[contains(text(),\'Home \')]").click()

def vercarrito():
	elchofer.find_element(By.XPATH, "//a[contains(text(),\'Cart\')]").click()


registro()
login()
comprar("Phones", "Samsung galaxy s6")
comprar("Laptops", "Sony vaio i5")
time.sleep(2)
vercarrito()