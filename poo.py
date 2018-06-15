class Singe:
    def __init__(self,nom):
        self.nom = nom

    def mange(self,banane):
        print(self.nom + ' mange la banane ' + banane.couleur)

    def seReproduitAvec(self,singe2,nom_enfant):
        print('Le singe ' + self.nom + ' se reproduit avec le singe ' + singe2.nom + ' pour créer ' + nom_enfant)
        enfant = Singe(nom_enfant)
        return enfant

class Banane:
    def __init__(self,couleur):
        self.couleur = couleur


pierre = Singe('Pierre')
marie = Singe('Marie')
bananeJaune = Banane('Jaune')
bananeVerte = Banane('Verte')

pierre.mange(bananeJaune)
marie.mange(bananeVerte)

robert = pierre.seReproduitAvec(marie,'Robert')
robert.mange(bananeVerte)

