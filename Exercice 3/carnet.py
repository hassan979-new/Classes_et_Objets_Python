from contact import Contact

class Carnet :
    def __init__(self):
        self.__contacts = []

    def ajouter(self, contact : Contact) :
        self.__contacts.append(contact)

    def recherche(self, fragment:str) :
        resultat = []
        for c in self.__contacts :
            if fragment.lower() in c.nom.lower() :
                resultat.append(c)
        
        return resultat
    
    def afficher_tous(self) :
        for c in self.__contacts :
            print(f"Contact: {c.nom} - Tel: {c.telephone} - email: {c.email}")