#!/usr/bin/env python3

import unittest
from selenium import webdriver
import time, os

class sistemasolar():
    def __init__(self):
        self.profile = webdriver.ChromeOptions()
        self.profile.add_argument('ignore-certificate-errors')
        #self.profile.add_argument('--headless')
        #self.profile.add_argument('--no-sandbox')
        #self.profile.add_argument('--disable-dev-shm-usage')
        chrome_driver_binary = "chromedriver"
        self.browser = webdriver.Chrome(chrome_driver_binary,options=self.profile)
        
    def testsolar(self,LINK,USER,PASSWORD):
        self.browser.get(link)
        #self.assertIn('S-Miles Cloud - Hoymiles Power Electronics Inc.', self.browser.title)

        ################# Site com aviso de manutenção
        time.sleep(10)    
        python_button = self.browser.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/button')[0]
        python_button.click()
        time.sleep(4)    
        #python_button = self.browser.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button')[0]
        #python_button.click()
        #time.sleep(4)
        ################# Site com aviso de manutenção

        python_button = self.browser.find_elements_by_xpath('//*[@id="email"]')[0]
        python_button.click()
        python_button.send_keys(usuario)
        time.sleep(1)    

        python_button = self.browser.find_elements_by_xpath('//*[@id="password"]')[0]
        python_button.click()
        python_button.send_keys(senha)
        time.sleep(1)                   

        python_button = self.browser.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/form/div[4]/button')[0]
        python_button.click()
        time.sleep(5)    

        python_button = self.browser.find_elements_by_xpath(
            '//*[@id="app"]/section/header/div/div[1]/div[2]/div[2]/div')[0]
        python_button.click()      
        time.sleep(1)                   

        python_button = self.browser.find_elements_by_xpath(
            '//*[@id="app"]/section/main/div[1]/div/div[1]/div')[0]
        python_button.click()  
        time.sleep(1)                   

        python_button = self.browser.find_elements_by_xpath(
            '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]')[0]
        python_button.click()  
        time.sleep(1)                   

        python_button = self.browser.find_elements_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[3]/a/button')[0]
        python_button.click()  
        time.sleep(5)    

        ######### Mudando de ABA
        p = self.browser.current_window_handle
        print(p)
        chld = self.browser.window_handles[1]
        time.sleep(1)                   
        self.browser.switch_to_window(chld)
        time.sleep(1)                   

        EnergyToday = self.browser.find_elements_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/span[1]')[0]
        time.sleep(1)                   

        EnergyThisMonth = self.browser.find_elements_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/span[1]')[0]
        time.sleep(1)                   

        EnergyThisYear = self.browser.find_elements_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/span[1]')[0]
        time.sleep(1)                   

        return EnergyToday,EnergyThisMonth,EnergyThisYear

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    link = os.environ['LINK']
    usuario = os.environ['USUARIO']
    senha = os.environ['SENHA']
    main = sistemasolar()
    EnergyToday,EnergyThisMonth,EnergyThisYear = main.testsolar(link,usuario,senha)
    print('Total de energia de hoje:',EnergyToday.text)
    print('Total de energia do mes:',EnergyThisMonth.text)
    print('Total de energia do ano:',EnergyThisYear.text)
    main.tearDown()

