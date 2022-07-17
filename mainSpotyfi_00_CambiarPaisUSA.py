# -*- coding: utf-8 -*-
#TESTTTTT

import time
from turtle import update
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesPais_to_USA import Acciones
from threading import Thread, Barrier

password='!asdf2021'
hilos=1
def accountsSpotify():

    id=[]
    email =[]
    

    db=MongoDB(hilos)
    db.iniciarDB()
    
    for elem in (db.findby2("accountmanager","acc_estado",1,"pais","COL")):
        print(elem)
        email.append(elem["email"])
        id.append(elem["_id"])
    #for elemid in id:
    #    db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
    db.cerrarConexion()
    return email, id, db

users, id,db= accountsSpotify()
print (len(users))
    
def iniciarSpotify(barrier,email,password,i,id,db):

    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)
    try:
        ingresando=acciones.ingresarSpotify()
    except:
        ingresando=acciones.ingresarSpotify()

    while ingresando==False:
        try:
            ingresando=acciones.ingresarSpotify()
        except:
            ingresando=acciones.ingresarSpotify()

    
    returnLoginSpotify= acciones.loginSpotify(email,password)
    while returnLoginSpotify== False:
        returnLoginSpotify= acciones.loginSpotify(email,password)
    
    
    
    if returnLoginSpotify == True:
        print(f"Hilo {i} - SinginSpotify {returnLoginSpotify}")

    acciones.sleep(5)
    def updatepais(acciones):
        acciones.ir('https://www.spotify.com/us/account/profile')
        acciones.sleep(5)
        acciones.cambiarpais()
        #acciones.executeScript("document.body.style.zoom='50%'")
        #acciones.nuevalista()
        acciones.sleep(10)
    ejecutar=updatepais(acciones)
    while ejecutar== False:
            ejecutar=updatepais(acciones)
    
    db.iniciarDB()
    db.updateOne("accountmanager",id,"pais","US")
    db.cerrarConexion()
    print (f"Account {i}, {id} pais actualizado")
    # 


barrier = Barrier(len(users))
hiloscerrados = 0
threads = []
for i in range(len(users)):
    i = Thread(target=iniciarSpotify, args=(barrier,users[i],password,i,id[i],db))
    i.start()
    threads.append(i)

for i in threads:
	i.join()
 
#iniciarSpotify()


