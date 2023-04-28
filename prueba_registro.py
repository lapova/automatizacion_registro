import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from time import sleep

class usando_unittest(unittest.TestCase):

    #Abrir un navegador en modo incógnito:
    # from selenium.webdriver.chrome.options import Options
    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.get('url-pag')

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path=r"C:\Driver_Chrome\chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get('https://demoqa.com/login')

    def test_book_store(self):
        driver = self.driver

        #Manejo archivo excel
        filessheet = "./registro.xlsx"
        wb = load_workbook(filessheet)
        hojas = wb.get_sheet_names()
        print(hojas)
        datos = wb.get_sheet_by_name('Hoja1')
        wb.close()

        #Recorrer el archivo de excel
        for i in range(1,4): #Filas excel
            name, last, user, password=datos[F'A{i}:D{i}'][0]

            #Nuevo usuario
            driver.find_element(By.ID, 'newUser').click()
            driver.find_element(By.ID, 'firstname').send_keys(name.value)
            driver.find_element(By.ID, 'lastname').send_keys(last.value)
            driver.find_element(By.ID, 'userName').send_keys(user.value)
            driver.find_element(By.ID, 'password').send_keys(password.value)
            sleep(3)

            #Cambiar al iframe
            iframe = driver.find_element(By.XPATH, '//*[@id="g-recaptcha"]/div/div/iframe')
            driver.switch_to.frame(iframe)

            sleep(3)

            # Validar el recaptcha
            driver.find_element(By.ID, 'recaptcha-anchor').click()

            sleep(3)

            #Cambiar de vuelta al contenido principal
            driver.switch_to.default_content()

            #Clic para registrar usuario
            driver.find_element(By.XPATH, "//*[@id='register']").click()

            #Login 
            driver.find_element(By.ID, 'userName').send_keys(name.value)
            driver.find_element(By.ID, 'password').send_keys(password.value)
            driver.find_element(By.ID, 'login').click()
            
    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
