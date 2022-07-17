# -*- coding: utf-8 -*-

from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesNeverInstall import Acciones


def iniciarNeverInstall():

    cuenta = 'azuresilk05@gmail.com'
    password = 'fps91507856'

    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)

    acciones.ingresarSitio()
    returnLoginGoogle = acciones.loginGoogle(cuenta,password)

    if returnLoginGoogle == True:
        returnResumeApp = acciones.esperarResumeApp()
        if returnResumeApp == True:
            
            returnIniciarVsCode = acciones.iniciarVsCode()
            if returnIniciarVsCode == True:
                acciones.vscodeTab()

            else:
                print(f"returnIniciarVsCode {returnIniciarVsCode}")

    else:
        print(f"returnLoginGoogle {returnLoginGoogle}")

    # 


iniciarNeverInstall()