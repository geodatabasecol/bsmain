# -*- coding: utf-8 -*-

from os import access
import random
import time
from PQTs.Selenium.Base import BaseAcciones

from PQTs.Utilizar import urlSpotifysinginUS

from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class Acciones(BaseAcciones):
    def ingresarSpotify(self):
        try:
            self.ir(urlSpotifysinginUS)
            self.sleep(2)
            return True
        except:
            self.salir()
            return False


    def loginSpotify(self,cuenta,password):
        try:
            xpathInputEmail = (By.ID,"login-username")
            xpathInputPassword = (By.ID,"login-password")        
            xpathBotonLogin= (By.ID,"login-button")
            visibleInputEmail = self.explicitWaitElementoVisibility(11,xpathInputEmail)
            if visibleInputEmail:
                self.escribir(xpathInputEmail,cuenta)
                
                visibleInputPassword = self.explicitWaitElementoVisibility(11,xpathInputPassword)
                if visibleInputPassword:
                    self.escribir(xpathInputPassword,password)
                    visibleBotonLogin = self.explicitWaitElementoVisibility(11,xpathBotonLogin)
                    if visibleBotonLogin:
                        self.click(xpathBotonLogin)
                        self.explicitWaitElementoInvisibility(11,xpathBotonLogin)
                        return True
                    else:
                        print(f"visibleBotonLogin {xpathBotonLogin}")
                        return False
                else:
                    print(f"visibleInputPassword {visibleInputPassword}")
                    return False
            else:
                print(f"visibleInputEmail {visibleInputEmail}")
                return False
        except:
            self.refreshweb()
            time.sleep(2)
            return False
    
    def cambiarpais(self):

        try: 

            time.sleep(5)                            
            xpathpaises = (By.XPATH, '//*[@id="country"]')
            select_element=self.findElement(xpathpaises)
            select_object= Select(select_element)
            select_object.select_by_value('US')
            time.sleep(3)
            xpathbotonsave =(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/article/section/form/div/button')
            self.click(xpathbotonsave)
            print("click SAVE")
            time.sleep(8)
            return True
        except:
            return False
