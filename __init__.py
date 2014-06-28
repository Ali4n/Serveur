__author__ = 'Thomas BOTTON, IGOR ZECEVIC, Daoud MOUSTIR'

# Ce serveur attend la connexion d'un client

from featuresSrv.functions import *

HOST = '127.0.0.1'
PORT = 46000

import socket, sys, threading

class ThreadClient(threading.Thread):
    #dérivation d'un objet thread pour gérer la connexion avec un client
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        # Dialogue avec le client
        nom = self.getName()    # Chaque thread possède un nom

        while 1:
            idForServerProcessing = self.connexion.recv(1024).decode("Utf8")

            message = "%s> %s" % (nom, idForServerProcessing)
            print(message)

            # Processing Serveur Menu
                #menu 1=>1 traitement random login & mdp
            if "WAu295kn" == idForServerProcessing:
                print ("traitement du menu 1 1")
                loginRandom = self.connexion.recv(1024).decode("Utf8")
                passwordRandom = self.connexion.recv(1024).decode("Utf8")
                passwordRandomHash = sha512(passwordRandom)

                #display
                message = "%s> %s= %s" % (nom, "loginRandom", loginRandom)
                print(message)
                message = "%s> %s= %s" % (nom, "passwordRandom",passwordRandom)
                print(message)
                message = "%s> %s= %s" % (nom, "passwordRandomHash",passwordRandomHash)
                print(message)


            elif "8fx24ANy" == idForServerProcessing:
                print("traitement du menu 1 2")
                login = self.connexion.recv(1024).decode("Utf8")
                password = self.connexion.recv(1024).decode("Utf8")
                passwordHash = sha512(password)

                #display
                message = "%s> %s= %s" % (nom,"login", login)
                print(message)
                message = "%s> %s= %s" % (nom, "password", password)
                print(message)
                message = "%s> %s= %s" % (nom, "passwordHash", passwordHash)
                print(message)

        """
        while 1:
            msgClient = self.connexion.recv(1024).decode("Utf8")
            if not msgClient or msgClient.upper() =="FIN":
                break
            message = "%s> %s" % (nom, msgClient)
            print(message)
            #Faire suivre le message à tous les autres clients :
            #for cle in conn_client:
            #    if cle != nom:
            #        conn_client[cle].send(message.encode("Utf8"))
        """



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