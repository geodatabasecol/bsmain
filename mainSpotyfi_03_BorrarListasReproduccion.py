# -*- coding: utf-8 -*-
import time
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesSinginSpotify import Acciones
from threading import Thread, Barrier

password='!asdf2021'
hilos=6
def accountsSpotify():

    id=[]
    email =[]
    

    db=MongoDB(hilos)
    db.iniciarDB()
    for elem in (db.findby1("accountmanager","creacionlistasentrenamiento",2)):
       
        email.append(elem["email"])
        id.append(elem["_id"])
    return email, id

users, id= accountsSpotify()
print (len(users))
    
def iniciarSpotify(barrier,email,password,i,id):


    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)

    acciones.ingresarSpotify()
    
    returnLoginSpotify= acciones.loginSpotify(email,password)

    if returnLoginSpotify == True:
        print(f"Hilo {i} - SinginSpotify {returnLoginSpotify}")

    time.sleep(3)
    driver.refresh()
    time.sleep(20)
    '''
    acciones.nuevalista()
    time.sleep(2)
    acciones.buscaryagregarartista()
    '''
    db=MongoDB(hilos)
    db.iniciarDB()
    
    db.updateOne("accountmanager",id,"creacionlistasentrenamiento",0)
    db.cerrarConexion()
    print (f"Account {i} lista de reproduccion eliminada")
    # 


barrier = Barrier(len(users))
hiloscerrados = 0
threads = []
for i in range(len(users)):
    i = Thread(target=iniciarSpotify, args=(barrier,users[i],password,i,id[i]))
    i.start()
    threads.append(i)

for i in threads:
	i.join()
 