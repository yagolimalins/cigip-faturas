
from extract import *
from PyPDF2 import PdfReader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

reader = PdfReader("faturas.pdf")

for i in range (0, len(reader.pages)):
        page = reader.pages[i]
        content = page.extract_text()

        codigoUnico = extraiCodigoUnico(content)
        mes = extraiMes(content)
        valor = extraiValor(content)
        consumo = extraiConsumo(content)
        leitura = extraiLeitura(content)

        print(f'\nCódigo Único: {codigoUnico}\n'
                f'Mês: {mes}\n'
                f'Valor: {valor}\n'
                f'Consumo: {consumo}\n'
                f'Leitura: {leitura}') 


        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:3000/index.html")

        elem = driver.find_element(By.ID, "uc")
        elem.clear()
        elem.send_keys(str(codigoUnico))

        elem = driver.find_element(By.ID, "mes")
        elem.clear()
        elem.send_keys(str(mes))

        elem = driver.find_element(By.ID, "consumo")
        elem.clear()
        elem.send_keys(str(consumo))

        elem = driver.find_element(By.ID, "valor")
        elem.clear()
        elem.send_keys(str(valor))

        elem = driver.find_element(By.ID, "leitura")
        elem.clear()
        elem.send_keys(str(leitura))