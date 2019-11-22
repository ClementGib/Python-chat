#SUJET LIBRE 
#faire une doc
import socket
import sys  
import _thread
import time
from info import info




class Server:


    def SubClient(self, indice):
       
        msgUsername = self.connexions[indice].recv(1024).decode()
        print("msgUsername reçu : %s" % (msgUsername))
        
        msgVille = self.connexions[indice].recv(1024).decode()
        print("msgVille reçu : %s" % (msgVille))
        
        msgHobby = self.connexions[indice].recv(1024).decode().split(" ")
        print("msgHobby reçu : %s"% (msgHobby))
        
        info_client = info(indice, msgUsername, msgVille, msgHobby)
        self.user.append(info_client)
        
        print(info_client.show_fiche())



    def GererClient(self,indice):
        
        self.SubClient(indice)
        print("Client %s connecté." % (self.connexions[indice-1]))
        self.connexions[indice].send("Vous êtes connecté au serveur. Envoyez vos messages.".encode('utf-8'))
        
        
        
        while 1:
            msgClient = self.connexions[indice].recv(1024)
            #print(msgClient.decode())
            self.GereMessages(indice,msgClient.decode())
            


    def GererSession(self):
        self.threads = []
        while 1:
            #Attente de la requête de connexion d'un client :
            print("Serveur de chat prêt, attente de connexion")
            self.mySocket.listen(5)


            #Connexion et ajout de l'host et de l'ip au dictionaire (VERIFIER) :
            connexion, adresse = self.mySocket.accept()
            
            #Permet de savoir si un utilisateur à un destinataire False/True
            self.sessions[self.counter] = (adresse,False)
            
            #self.sessions[self.counter] =  [False]
            self.connexions.append(connexion)
            
            print(self.sessions)
            print("Client connecté, adresse IP et port : %s" % (self.sessions))
            
            self.threads.append(_thread.start_new_thread(self.GererClient, (self.counter,) ))
  
            #thread = threading.Thread(target=self.GererClient, arg=(self.sessions[self.counter],))
            #threads.append(thread)
            #thread.start()
            
            self.counter +=1



    # constructeur
    def __init__(self,host,port):

        self.HOST = host
        self.PORT = port


        # compteur de connexions actives
        self.counter = 0
        self.user = []
        self.sessions = {}
        self.connexions = []
       

        #Création du socket
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #liaison du socket à une adresse précise :
        try:
            self.mySocket.bind((self.HOST, self.PORT))
        except socket.error:
            print("La liaison du socket à l'adresse choisie a échoué !!!!!!")
            sys.exit





    def GereMessages(self,indice,message):
        #command tapé
        if message[0] == '/':
            if message == '/EXIT':
                #Fermeture de la connexion :
                self.connexions[indice].send("fin".encode("Utf8"))
                print("Connexion interrompue.")
                del self.user[indice]
                del self.sessions[indice]
                self.connexions[indice].close()       
                return 1
            
            elif message == '/LIST':
            #lister les utilisateur connecté
                #for self.sessions[]
                print("Lister des utilisateurs ")
                
                
                #Probleme list objet:
                for obj in self.user:
                    print(obj.Getidentite())
                #
                #     print(info)
                
            elif message == '/SELECT':
                print("Changer d'utilisateur : ")
                #if nom valide dans le dico
                #Ajout du destinataire à self.user
                
            else:
                print(self.sessions["info"])
                msgServeur = "\nCommand inexistante!!! \nEntrer une commande :\n/EXIT : Déconnexion\n/LIST : Lister les utilisateurs connecté\n/SELECT <NAME> : Sélectionner un destinataire".encode('utf-8')
                self.connexions[indice].send(msgServeur)
               
        #dest de dictionary et valeur 1 du tuple (True/False)     
        elif(self.sessions[0][1]==True):
            #Envoi des messages au destinataire
            msgDestinataire = message
            self.connexions[self.user[indice]["dest"]].send(msgServeur)
            exit(0)
        else:
            msgServeur = "Entrer une commande :\n/EXIT : Déconnexion\n/LIST : Lister les utilisateurs connecté\n/SELECT <NAME> : Sélectionner un destinataire".encode('utf-8')
            self.connexions[indice].send(msgServeur)
            
            

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





    














