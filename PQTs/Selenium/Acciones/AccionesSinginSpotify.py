# -*- coding: utf-8 -*-

from os import access
import random
import time
from PQTs.Selenium.Base import BaseAcciones

from PQTs.Utilizar import urlSpotifysinginUS

from selenium.common import exceptions
from selenium.webdriver.common.by import By

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
    
    def nuevalista(self):

        try:  
            time.sleep(15)                            
            xpathnuevalista = (By.XPATH, "//*[@id='main']/div/div[2]/nav/div[1]/div[2]/div/div[1]/button")
            
            visiblenuevalista = self.explicitWaitElementoVisibility(1200,xpathnuevalista)
            if visiblenuevalista:
                self.click(xpathnuevalista)
                print('Click nueva lista')
                return True
            else:
                print(f"visibleNuevalista {visiblenuevalista}")
                return False
        except:
            return False
        

    def buscaryagregarartista(self):
        listartistas=["The Beatles","Mariah Carey","Elvis Presley","Rihanna","Michael Jackson",
        "Madonna","Billie Eilish","Bruno Mars","Britney Spears","Bachman-Turner Overdrive",
        "Bad Bunny","Bad English","Bananarama","The Bangles","Barenaked Ladies","Toni Basil",
        "Les Baxter","Bay City Rollers","The Beach Boys","The Beatles","Stephanie Beatriz",
        "Bee Gees","The Bellamy Brothers","Regina Belle","Lauren Bennett","Berlin","Bradley Cooper",
        "Chuck Berry","Beyoncé","Mr. Acker Bilk","Mary J. Blige","Blondie","Blue Swede","James Blunt",
        "Michael Bolton","Bon Jovi","Jon Bon Jovi","Gary U.S. Bonds","Krayzie Bone","Debby Boone",
        "Pat Boone","Boston","David Bowie","Box Tops","Brandy","Toni Braxton","Bread",
        "Bobby Brown","Chris Brown","Sleepy Brown","The Browns","Peabo Bryson",
        "The Buckinghams","The Byrds"]

        miscanciones=[
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[2]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[4]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[5]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[6]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[7]/div/div[3]/button'
        ]
        itemsagregar=[
         '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div',
         '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/div[1]/div[2]/div'
        ]

        miscancionesrandom=random.sample(miscanciones, 7)        
        miscanciones1=miscancionesrandom[0:3]
        miscanciones2=miscancionesrandom[3:7]
        cancion1=random.sample(miscanciones1, 3)
        cancion2=random.sample(miscanciones2, 4)

        mylistartistas=random.sample(listartistas, 4)
        mylistartistas.append("SilkLipsMusicX1")
        mylistartistaok=random.sample(mylistartistas, 5)
        mylistartistaok.append("SilkLipsMusicX2")
        mylistartistaok1=random.sample(mylistartistaok, 6)
        print (mylistartistaok1)
        
        xpathbuscarartista=(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/section/div/div/input')
        
        #<p class="Type__TypeElement-goli3j-0 gAmaez FETh66aSunr0whiLsmk4">SilkLipsMusicX</p>
                                           
        xpathalbumSilkLipsMusic=(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/p[1]')
        
        
        body=(By.XPATH,'/html/body')

        visiblebuscarartista= self.explicitWaitElementoVisibility(1200,xpathbuscarartista)
        if visiblebuscarartista:
            
            for  elem in mylistartistaok1:
                
                if elem =='SilkLipsMusicX1':
                    self.clear(xpathbuscarartista)
                    self.escribir(xpathbuscarartista,"SilkLipsMusicX")
                    time.sleep(10)
                    self.pagedown(body)
                    self.sleep(4)
                    self.click(xpathalbumSilkLipsMusic)
                    time.sleep(4)
                    xpathcancion=(By.XPATH,cancion1[0])
                    self.click(xpathcancion)
                    print("click cancion1_1")
                    time.sleep(4)
                    xpathcancion=(By.XPATH,cancion1[1] )
                    self.click(xpathcancion)
                    print("click cancion1_2")   
                    time.sleep(4)
                    xpathcancion=(By.XPATH,cancion1[2])
                    self.click(xpathcancion)   
                    print("click cancion1_3") 
                    
                elif elem =='SilkLipsMusicX2':
                    self.clear(xpathbuscarartista)
                    self.escribir(xpathbuscarartista,'SilkLipsMusicX')
                    time.sleep(10)
                    self.click(xpathalbumSilkLipsMusic)
                    time.sleep(3)
                    xpathcancion=(By.XPATH,cancion2[0] )
                    self.click(xpathcancion)
                    print("click cancion2_1") 
                    time.sleep(3)
                    xpathcancion=(By.XPATH,cancion2[1] )
                    self.click(xpathcancion)     
                    print("click cancion2_2") 
                    time.sleep(3)
                    xpathcancion=(By.XPATH,cancion2[2] )
                    self.click(xpathcancion)      
                    print("click cancion2_3") 
                    time.sleep(3)
                    xpathcancion=(By.XPATH,cancion2[3] )
                    self.click(xpathcancion) 
                    print("click cancion2_4") 
                                                  
                else:
                    self.clear(xpathbuscarartista)
                    self.escribir(xpathbuscarartista,elem)
                    time.sleep(3)
                    
                    i=0
                    for item in itemsagregar:
                        print ("aertista ", elem)
                        time.sleep(100)
                        xpathcancion=(By.XPATH,itemsagregar[i] )
                        print ("XPATH= ",item)
                        self.click(xpathcancion)
                        print("cancion agregada")
                        time.sleep(2)
                        i+=1
                    print('Agregando 2 canciones del artista',elem)  
        
        else:
            print(f"visibleNuevalista {visiblebuscarartista}")
