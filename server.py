#SUJET LIBRE 
#faire une doc
import socket
import sys
import threading
from multiprocessing import Process
import time
from info import info




class Server:


    def SubClient(self):

        id=input("Entrer votre identite : ")
    
        age=18
        #while (isinstance(age=input("Entrer votre age : "), int)):

        
        location = input("Entrer votre location : ")
        sociopro = input("Entrer votre sociopro : ")
        info_client = info(id,age,location,sociopro)




    def GererClient(self,indice):
        
        print("Client %s connecté." % (self.connexions[indice-1]))
        self.connexions[indice].send("Vous êtes connecté au serveur. Envoyez vos messages.".encode('utf-8'))
        
        msgClient = self.connexions[indice].recv(1024)
        print(msgClient)
        while 1:
            self.GereMessages(indice,msgClient)




    def GererSession(self):
        #self.threads = []
        while 1:
            #Attente de la requête de connexion d'un client :
            print("Serveur de chat prêt, attente de connexion")
            self.mySocket.listen(5)


            #Connexion et ajout de l'host et de l'ip au dictionaire (VERIFIER) :
            connexion, adresse = self.mySocket.accept()
            self.sessions[self.counter] = {adresse}  
            self.sessions["echange"] = 0
            self.connexions.append(connexion)
            
            
            print("Client connecté, adresse IP et port : %s" % (self.sessions))
            self.GererClient(self.counter)
            self.counter +=1
            #thread = threading.Thread(target=self.GererClient, arg=(self.sessions[self.counter-1],))
            #threads.append(thread)
            #thread.start()


    # constructeur
    def __init__(self,host,port):

        self.HOST = host
        self.PORT = port


        # compteur de connexions actives
        self.counter = 0	
        self.sessions = {}
        self.connexions = []

        #Création du socket
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #liaison du socket à une adresse précise :
        try:
            self.mySocket.bind((self.HOST, self.PORT))
        except socket.error:
            print("La liaison du socket à l'adresse choisie a échoué.")
            sys.exit





    def GereMessages(self,indice,message):
        if(self.sessions["echange"]==1):
            exit(0)
        elif message[0] == '/':
            if message == '/EXIT':
                #Fermeture de la connexion :
                self.connexions[indice].send("fin".encode("Utf8"))
                print("Connexion interrompue.")
                self.connexions[indice].close()       
                return 1

            elif message == '/LIST':
            #lister les utilisateur connecté
                print("Lister les utilisateurs ")

            elif message == '/CHANGE':
                print("Changer d'utilisateur : ")

    # def Listen():
        
        # # 5) Dialogue avec le client :
        # msgServeur ="Vous êtes connecté au serveur de chat. entrer votre commande"
        # connexion.send(msgServeur.encode("Utf8"))
        # msgClient = connexion.recv(1024).decode("Utf8")
        # while 1:
        #     print("C>", msgClient)
        #     if msgClient[0] == "/" :
        #         value = self.GererCommand(  
        #         msgServeur = input("S> ")
        #         connexion.send(msgServeur.encode("Utf8"))
        #         msgClient = connexion.recv(1024).decode("Utf8")





    














