class info:
    def __init__(self, id, identite, location, sociopro):
        self.id = id
        self.identite = identite
        self.location = location
        self.sociopro = sociopro
        
        
        
    def show_fiche(self):
        print('INFORMATION CLIENT : \n identite :'+str(self.identite )+', location :'+ str(self.location) + ', sociopro :' + str(self.sociopro))
        
        
    def Getidentite():
        return self.identite
    
    def Getlocation():
        return self.location
    
    def Getsociopro():
        return self.sociopro
"""
    def get_user_id(self):
        while 1:
            try:
                return self.identite[name,login]
                #identite = [name, login]
            except:
                print('Mauvaise entré identité!')
                continue
    def get_user_sociopro(self):
        while 1:
            try:
                activite = input('Entrez votre activité: ')
                hobby = input('Entrez un hobby: ')
                return self.sociopro[activite, hobby]
                #sociopro = self[activite, hobby]
            except:
                print('Mauvaise entré pour sociopro!')
                continue
    def get_user_location(self):
        while 1:
            try:
                pays = input('Entrez votre pays : ')
                ville = input('Entrez un ville : ')
                return self.location[pays, ville]
                #location = self[pays, ville]
            except:
                print('Mauvaise entré pour la localisation!')
                continue
"""