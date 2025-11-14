
class phrase:
    def __init__(self, nom):
        self.doig_h = nom
    def phrase_pour_doigt(self):
           if self.doig_h== 'A1':print( "Phrase pour le premier doigt",)
           elif self.doig_h== 'A2':print( "Phrase pour le 2 doigt",)
           elif self.doig_h== 'A3':print( "Phrase pour le 3 doigt",)
           elif self.doig_h== 'A4':print( "Phrase pour le 4 doigt",)
           elif self.doig_h== 'A5':print( "Phrase pour le 5 doigt",)
           elif self.doig_h== 'A6':print( "Phrase pour le 6 doigt",)
           elif self.doig_h== 'A7':print( "Phrase pour le 7 doigt",)
           elif self.doig_h== 'A8':print( "Phrase pour le 8 doigt",)
           else:print( "le doigt n'exist pas")
class Class_1:
    def __init__(self, nom):
        self.doig = nom
    def phrase(self):
      if self.doig =='A5':
            print("erreur") # classe 1 n'etulise pas le pouce
      else:       
        a=phrase(self.doig)
        a.phrase_pour_doigt()

class Class_2:
    def __init__(self, nom):
        self.doig = nom
    def phrase(self):       
        a=phrase(self.doig)
        a.phrase_pour_doigt()   

class Class_3:
    def __init__(self, nom,nom2):
        self.doig = nom
        self.doig2 = nom
    def phrase(self): 
        if   self.doig=='A1'& self.doig2=='A2': # on peut donne just 1 seul parametre pour la classe  phrase 
          self.doig='A6'
        elif   self.doig=='A2'& self.doig2=='A3':
          self.doig='A7' 
        if   self.doig=='A3'& self.doig2=='A4':
          self.doig='A8'           
        a=phrase(self.doig)
        a.phrase_pour_doigt()  
class general(): #
  def __init__(self,type_nom, valeur_arduino, doigt_utilise,doigt_nmbr):
      self.type=type_nom
      self.val=valeur_arduino
      self.doigt=doigt_utilise
      self.nbr=doigt_nmbr
  def verifier_valeur(self):
     type_classes = ['Class 1','Class 2']  # Liste de toutes les classes de maladies
     type_trouvee = None
     for type in type_classes:
        print(type_classes)
        #print(type.nom)
        if type == self.type:
            type_trouvee = type
            break
     if type_trouvee:
        a = 1# a et b max et min d'interval
        b = 5
        x=self.nbr
        if a <= self.val <= b:
          print("ff")
          if x==1:
            print("ff")
            if self.type=='Class 1':
              print("ff")
              a=Class_1(self.doigt)
              a.phrase()
            elif self.type=='Class 2':  
               a=Class_2(self.doigt)
               a.phrase() 
          elif  x==2:
              doigt_utilise2 = input("Entrez le 2eme doigt utilisé (A1, A2, A3, A4, A5) : ")
              a=Class_3(self.doigt,doigt_utilise2 )
              a.phrase()
        else:
            return print("La valeur ne correspond pas aux critères spécifiés.")
     else:
        return print("type  non trouvée.")


#type_utilisee=Serial.read
type_utilisee = input("Entrez le type : ") #soit Class 1 ou Class 2 ou Class 3
#maladie_utilisee = (f1.maladie)

valeur_arduino = float(input("Entrez la valeur du capteur Arduino : ")) #val de flex senseur antre[1,5] exemple
doigt_nmbr = input("Entrez le nmbre doigt : ") # soit 1 ou 2
doigt_utilise = input("Entrez le doigt utilisé (A1, A2, A3, A4, A5) : ") # ontre le premier doigh
#if doigt_nmbr==1:
resultat_verification = general(type_utilisee, valeur_arduino,doigt_utilise,doigt_nmbr) #
resultat_verification.verifier_valeur()
#elif doigt_nmbr==2:
   #resultat_verification2 = verifier_valeur(type_utilisee, valeur_arduino, doigt_utilisem,doigt_utilisem2,doigt_nmbr)    print(resultat_verification)

