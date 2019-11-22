# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc
 
import socket, sys
 
HOST = '10.22.0.41'
PORT = 15555
#PORT = 30000
 
# 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 2) envoi d'une requête de connexion au serveur :
try:
  mySocket.connect((HOST, PORT))
except socket.error:
  print("La connexion a échoué.")
  sys.exit()

print("Connexion établie avec le serveur.")

msgUsername = input("Entrez un username : ")
mySocket.send(msgUsername.encode('utf-8'))

msgVille = input("Entrez le nom de votre ville : ")
mySocket.send(msgVille.encode('utf-8'))

msgHobby = input("Entrez un ou des hobbies : ")
mySocket.send(msgHobby.encode('utf-8'))




# 3) Dialogue avec le serveur :
msgServeur = mySocket.recv(1024).decode('utf-8')
 
while 1:
  if msgServeur.upper() == "FIN" or msgServeur =="":
      break
  print("Server>", msgServeur)
  msgClient = input(msgUsername+">")
  mySocket.send(msgClient.encode('utf-8'))
  msgServeur = mySocket.recv(1024).decode('utf-8')
 
# 4) Fermeture de la connexion :
print("Connexion interrompue.")
mySocket.close()