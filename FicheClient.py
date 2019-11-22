class FicheClient:
    def __init__(self, identite, location, sociopro):
        
        #self.name = name
        #self.login = login
        self.identite = []

        #self.pays = pays
        #self.ville = ville
        self.location = []

        #self.activite = activite
        #self.hobby = hobby
        self.sociopro = []

        """
        identite = [name, login]
        location = [pays, ville]
        sociopro = [activite, hobby]
        """


    def get_user_id(self):
        while 1:
            try:
                name = input('Entrez votre name: ')
                login = input('Entrez un login')
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

    def show_fiche(self):
        return self.identite + ' '+ self.location + ' ' + self.get_user_sociopro

User1 = FicheClient(FicheClient.get_user_id(), FicheClient.get_user_sociopro(), FicheClient.get_user_location())
User1.show_fiche()