# -*- coding: utf-8 -*-
from PQTs.Selenium.Base import BaseAcciones

from PQTs.Utilizar import urlNeverInstall

from selenium.common import exceptions
from selenium.webdriver.common.by import By

class Acciones(BaseAcciones):

    def ingresarSitio(self):
        self.ir(urlNeverInstall)

    def loginGoogle(self,cuenta,password):
        xpathBotonGoogle = (By.XPATH,'//button[@id="googleLogin"]')
        xpathElementoCarga = (By.XPATH,'//div[@class="load-inner"]')

        xpathInputCuenta = (By.XPATH,'//input[@id="identifierId"]')
        xpathBotonCuenta = (By.XPATH,'//div[@id="identifierNext"]//button')

        xpathInputPassword = (By.XPATH,'//div[@id="password"]//input')
        xpathBotonPassword = (By.XPATH,'//div[@id="passwordNext"]//button')

        visibleBotonGoogle = self.explicitWaitElementoVisibility(11,xpathBotonGoogle)
        if visibleBotonGoogle:
            
            self.click(xpathBotonGoogle)
            self.explicitWaitElementoInvisibility(11,xpathElementoCarga)

            visibleInputCuenta = self.explicitWaitElementoVisibility(11,xpathInputCuenta)
            if visibleInputCuenta:
                self.escribir(xpathInputCuenta,cuenta)
                self.click(xpathBotonCuenta)

                visibleInputPassword = self.explicitWaitElementoVisibility(11,xpathInputPassword)
                if visibleInputPassword:
                    self.escribir(xpathInputPassword,password)
                    self.click(xpathBotonPassword)

                    return True
                
                else:
                    print(f"visibleInputPassword {visibleInputPassword}")
            else:
                print(f"visibleInputCuenta {visibleInputCuenta}")
        else:
            print(f"visibleBotonGoogle {visibleBotonGoogle}")

    def esperarResumeApp(self):

        xpathBotonResumeApp = (By.XPATH, "//span[contains(text(),'Resume app')]")

        visibleBotonResumeApp = self.explicitWaitElementoVisibility(1200,xpathBotonResumeApp)
        if visibleBotonResumeApp:
            print('boton encontrado')
            
            return True

        else:
            print(f"visibleBotonResumeApp {visibleBotonResumeApp}")

    def iniciarVsCode(self):

        xpathBotonResumeApp = (By.XPATH, "//span[contains(text(),'Resume app')]")
        xpathBotonOpenInBrowser = (By.XPATH, "//span[contains(text(),'Open in browser')]")

        xpathDivStatusBuilding = (By.XPATH, "//div[@status='Building']")

        # div status="Building"  //div[@status="Building"]

        self.click(xpathBotonResumeApp)

        invisibleDivStatusBuilding = self.explicitWaitElementoInvisibility(1200,xpathDivStatusBuilding)
        if invisibleDivStatusBuilding:

            visibleBotonResumeApp = self.explicitWaitElementoVisibility(60,xpathBotonResumeApp)
            if visibleBotonResumeApp:
                print('boton xpathBotonResumeApp')
                
                self.click(xpathBotonResumeApp)

            else:

                visibleBotonOpenInBrowser = self.explicitWaitElementoVisibility(60,xpathBotonOpenInBrowser)
                if visibleBotonOpenInBrowser:

                    self.click(xpathBotonOpenInBrowser)

                    return True

                else:
                    print(f"visibleBotonOpenInBrowser {visibleBotonOpenInBrowser}")

            #cantidadTabs = self.cantidadWindowHandle()

    def vscodeTab(self):

        cantidadTabs = self.cantidadWindowHandle()

        if cantidadTabs == 2:
            self.cambiarTabEspecifico(cantidadTabs[1])

            self.sleep(120)
        else:
            print(f"cantidadTabs {cantidadTabs}")
