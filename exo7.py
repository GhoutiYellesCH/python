class Voiture:
    def __init__(self, marque, modèle, couleur):
        self.marque = marque
        self.modèle = modèle
        self.couleur = couleur

    def accelerer(self):
        print("La voiture accélère")

    def freiner(self):
        print("La voiture freine")

    def rechercher_voitures(self,list_voitures, marque_a_chercher):
        for voiture in list_voitures:
            if voiture.marque == marque_a_chercher:
                return voiture
        return None

listvoitures = [Voiture("Renault", "Clio", "rouge"),
                 Voiture("Peugeot", "301", "bleue"),
                 Voiture("Hyundai", "i10", "noire")]

voiture = Voiture("audi","RS3","gray")
voiture.accelerer()
voiture.freiner()
mark = input("searching mark :")
print(voiture.rechercher_voitures(listvoitures,mark))

