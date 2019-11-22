class info:
    def __init__(self, identite, age, location, sociopro):
        
        #self.name = name
        #self.login = login
        self.identite = [identite]
        self.age = age

        #self.pays = pays
        #self.ville = ville
        self.location = [location]

        #self.activite = activite
        #self.hobby = hobby
        self.sociopro = [sociopro]

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
                prServerint('Mauvaise entré identité!')
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

