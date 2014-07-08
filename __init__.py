__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

# Ce serveur attend la connexion d'un client

from featuresSrv.functions import *
from ftplib import FTP

HOST = '127.0.0.1'
PORT = 46000

import socket
import sys
import threading
import sqlite3

class ThreadClient(threading.Thread):
    #dérivation d'un objet thread pour gérer la connexion avec un client
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        # Dialogue avec le client
        nom = self.getName()    # Chaque thread possède un nom
        uniqid = "Wm9A8d84F25Uz39rvEeKKzhS5P4dT2sy"

        while 1:
            idForServerProcessing = self.connexion.recv(1024).decode("Utf8")

            message = "%s> %s" % (nom, idForServerProcessing)
            print(message)
            logserver(message)

            #Mettre en place la base de donnée SQL :)
            file = "C:/Users/N3o/PycharmProjects/Serveur/bddmembers.sq3"
            connectbdd = sqlite3.connect(file)
            cursorbdd = connectbdd.cursor()
            try:
                cursorbdd.execute("CREATE TABLE membres (login TEXT, password TEXT)")
            except:
                connectbdd.commit()
                message = "%s> %s" % (nom, "votre table members existe deja ...")
                print(message)
                logserver(message)

            # Processing Serveur Menu
                #menu 1=>1 traitement random login & mdp
            if "WAu295kn" == idForServerProcessing:
                print("traitement du menu 1 1")
                loginRandom = self.connexion.recv(1024).decode("Utf8")
                passwordRandom = self.connexion.recv(1024).decode("Utf8")
                passwordRandomHash = sha512(sha512(sha512(uniqid + passwordRandom)))

                #display
                message = "%s> %s= %s" % (nom, "loginRandom", loginRandom)
                print(message)
                logserver(message)
                message = "%s> %s= %s" % (nom, "passwordRandom", passwordRandom)
                print(message)
                logserver(message)
                message = "%s> %s= %s" % (nom, "passwordRandomHash", passwordRandomHash)
                print(message)
                logserver(message)

                cursorbdd.execute("INSERT INTO membres (login,password) VALUES ('" + loginRandom + "','" + passwordRandomHash + "')")
                message = "%s" % ("Merci vous etes desormais enregistrer avec votre login et mot de passe, vous pouvez vous connecter :)")
                self.connexion.send(message.encode("Utf8"))

            elif "8fx24ANy" == idForServerProcessing:
                print("traitement du menu 1 2")
                login = self.connexion.recv(1024).decode("Utf8")
                password = self.connexion.recv(1024).decode("Utf8")
                passwordHash = sha512(sha512(sha512(uniqid + password)))

                #display
                message = "%s> %s= %s" % (nom, "login", login)
                print(message)
                logserver(message)
                message = "%s> %s= %s" % (nom, "password", password)
                print(message)
                logserver(message)
                message = "%s> %s= %s" % (nom, "passwordHash", passwordHash)
                print(message)
                logserver(message)

                cursorbdd.execute("INSERT INTO membres (login,password) VALUES ('" + login + "','" + passwordHash + "')")
                message = "%s" % ("Merci vous etes desormais enregistrer avec votre login et mot de passe, vous pouvez vous connecter :)")
                self.connexion.send(message.encode("Utf8"))

            elif "Sa8w94Tb" == idForServerProcessing:
                print("traitement du menu 2 Authentification")
                loginAuth = self.connexion.recv(1024).decode("Utf8")
                passwordAuth = self.connexion.recv(1024).decode("Utf8")
                passwordAuthHash = sha512(sha512(sha512(uniqid + passwordAuth)))
                checkAuth = "0"

                #display
                message = "%s> %s= %s" % (nom, "loginAuth", loginAuth)
                print(message)
                logserver(message)
                message = "%s> %s= %s" % (nom, "passwordAuth", passwordAuth)
                print(message)
                logserver(message)
                message = "%s> %s= %s" % (nom, "passwordAuthHash", passwordAuthHash)
                print(message)
                logserver(message)

                cursorbdd.execute("SELECT * FROM membres")
                result = list(cursorbdd)
                lenghtUsersInBDD = len(result)

                for z in range(lenghtUsersInBDD):
                    if result[z][0] == loginAuth:
                        checkAuth = "1"

                        if result[z][1] == passwordAuthHash:
                            checkAuth = "2"

                #display good or bad 3 state => good login, good login & pass, bad login & pass,
                if checkAuth == "1":
                    message = "%s> %s" % (nom, "status good login ('"+ loginAuth +"') + bad password ('"+ passwordAuth +"')")
                    print(message)
                    logserver(message)

                    message = "%s" % ("Mauvais Login & Mot de passe")
                    self.connexion.send(message.encode("Utf8"))

                elif checkAuth == "2":
                    message = "%s> %s" % (nom, "status good login & good password ('"+ loginAuth +"', '"+ passwordAuth +"')")
                    print(message)
                    logserver(message)

                    message = "%s" % ("Bienvenu sur votre espace de stockage")
                    self.connexion.send(message.encode("Utf8"))


                elif checkAuth == "0":
                    message = "%s> %s" % (nom, "status bad login & bad password")
                    print(message)
                    logserver(message)

                    message = "%s" % ("Mauvais Login & Mot de passe")
                    self.connexion.send(message.encode("Utf8"))

            #displayBDD
            cursorbdd.execute("SELECT * FROM membres")
            for lignes in cursorbdd:
                message = "%s> %s= %s" % (nom, "lignes", lignes)
                print(message)

            connectbdd.commit()
            cursorbdd.close()
            connectbdd.close()

        #Fermeture de la connexion :
        self.connexion.close()  #couper la connexion côté serveur
        del conn_client[nom]    #supprimer son entrée dans le dictionnaire
        print("Client %s déconnecté." % nom)
        # Le thread se termine ici

#Initialisation du serveur - Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print("Serveur prêt, en attente de requêtes ...")
mySocket.listen(5)

# Attente et prise en charge des connexions demandées par les clients :
conn_client = {}
while 1:
    connexion, adresse = mySocket.accept()
    # Crée un nouvel objet thread pour gérer la connexion :
    th = ThreadClient(connexion)
    th.start()
    #Mémoriser la connexion dans le dictionnaire :
    it = th.getName()   #identifiant du thread
    conn_client[it] = connexion
    print("Client %s connecté, adresse IP %s, port %s" %(it, adresse[0], adresse[1]))
    # Dialogue avec le client :
    #msg = "Vous êtes connecté. Envoyez vos messages."
    #connexion.send(msg.encode("Utf8"))