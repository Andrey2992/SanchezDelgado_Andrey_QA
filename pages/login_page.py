"""Page Object de login: completar con locators y acciones de Appium."""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #Aqui estan los 5 locators
    def __init__(self, driver):
        self.driver = driver
        self.input_email = (AppiumBy.ACCESSIBILITY_ID, "input_email")
        self.input_password = (AppiumBy.ACCESSIBILITY_ID, "input_password")
        self.txt_error = (AppiumBy.ACCESSIBILITY_ID, "txt_error")
        self.home_title = (AppiumBy.ACCESSIBILITY_ID, "home_title")
        self.btn_login = (AppiumBy.ACCESSIBILITY_ID, "btn_login")        

    #Tenemos tres acciones
    def ingresar_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.input_email)).send_keys(email)

    def ingresar_contraseña(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.input_password)).send_keys(password)

    def pulsar_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_login)).click()

    #Tenemos dos metodos que leen texto
    def obtener_titulo_principal(self):
        titulo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home_title))
        return titulo.text

    def obtener_error(self):
        mensaje = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.txt_error))
        return mensaje.text