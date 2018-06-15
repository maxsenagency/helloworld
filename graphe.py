class Graphe:

    def __init__(self,nom):
        self.nom = nom
        self.noeuds = []
        self.arrete = []

    def ajouterNoeud(self,noeud):
        self.noeuds.append(noeud)

    def ajouterArrete(self,noeud1,noeud2):
        self.arrete.append(noeud1 + ':' + noeud2)

    def isNoeudConnecte(self,noeud1,noeud2):
        if (((noeud1 + ':' + noeud2) in self.arrete) or ((noeud2 + ':' + noeud1) in self.arrete)) :
            return 'Les noeuds ' + noeud1 + ' et ' + noeud2 + ' sont connectés'
        else :
            return 'Les noeuds ' + noeud1 + ' et ' + noeud2 + ' ne sont pas connectés'


graphe1 = Graphe('graphe1')
graphe1.ajouterNoeud('A')
graphe1.ajouterNoeud('B')
graphe1.ajouterNoeud('C')
graphe1.ajouterNoeud('D')

graphe1.ajouterArrete('A','B')
graphe1.ajouterArrete('C','D')
graphe1.ajouterArrete('A','D')

print(graphe1.isNoeudConnecte('B','D'))
print(graphe1.isNoeudConnecte('A','B'))
