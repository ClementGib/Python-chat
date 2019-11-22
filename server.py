#SUJET LIBRE 
#faire une doc
import socket
import sys
import threading




class Server:


    def GererClient(dico):
        print("Hello")




    def GererSession(self):
        threads = []
        while 1:
            #Attente de la requête de connexion d'un client :
            print("Serveur de chat prêt, attente de connexion")
            self.mySocket.listen(5)

            #Connexion et ajout de l'host et de l'ip au dictionaire (VERIFIER) :
            connexion, adresse = self.mySocket.accept()
            self.counter +=1
            self.sessions[connexion] = adresse        
            #print("Client connecté, adresse IP et port : %s" % (self.sessions[self.counter-1])

            print(sessions)
            # thread = threading.Thread(target=GererClient, arg=(self.sessions[self.counter-1],))
            # threads.append(thread)
            # thread.start()
    





    # constructeur
    def __init__(self,host,port):

        self.HOST = host
        self.PORT = port


        # compteur de connexions actives
        self.counter = 0	
        self.sessions = {}

        #Création du socket
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #liaison du socket à une adresse précise :
        try:
            self.mySocket.bind((self.HOST, self.PORT))
        except socket.error:
            print("La liaison du socket à l'adresse choisie a échoué.")
            sys.exit





    def GererCommand(message):
        if message == '/END':
            #Fermeture de la connexion :
            connexion.send("fin".encode("Utf8"))
            print("Connexion interrompue.")
            connexion.close()
        
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





    














