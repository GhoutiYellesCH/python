from ortools.sat.python import cp_model
model = cp_model.CpModel()

blanche = model.NewIntVar(1, 5, 'blache')
rouge = model.NewIntVar(1, 5, 'rouge')
verte = model.NewIntVar(1, 5, 'verte')
jaune = model.NewIntVar(1, 5, 'jaune')
blue = model.NewIntVar(1, 5, 'blue')
norvegien = model.NewIntVar(1, 5, 'norvegien')
anglais = model.NewIntVar(1, 5, 'anglais')
ukrainien = model.NewIntVar(1, 5, 'ukrainien')
japonais = model.NewIntVar(1, 5, 'japonais')
espagnol = model.NewIntVar(1, 5, 'espagnol')
cheval = model.NewIntVar(1, 5, 'cheval')
renard = model.NewIntVar(1, 5, 'renard')
zebre = model.NewIntVar(1, 5, 'zebre')
escargot = model.NewIntVar(1, 5, 'escargot')
chien = model.NewIntVar(1, 5, 'chien')
thé = model.NewIntVar(1, 5, 'thé')
eau = model.NewIntVar(1, 5, 'eau')
lait = model.NewIntVar(1, 5, 'lait')
cafe = model.NewIntVar(1, 5, 'cafe')
jus = model.NewIntVar(1, 5, 'jus')
sculpteur = model.NewIntVar(1, 5, 'sculpteur')
diplomate = model.NewIntVar(1, 5, 'diplomate')
medecin = model.NewIntVar(1, 5, 'medecin')
violoniste = model.NewIntVar(1, 5, 'violoniste')
acrobate = model.NewIntVar(1, 5, 'acrobate')

X = {blanche, rouge, verte, jaune, blue, norvegien, anglais, ukrainien, japonais, espagnol, cheval,
renard, zebre, escargot, chien, thé, eau, lait, cafe, jus, sculpteur , diplomate , medecin , violoniste ,
acrobate }


model.AddAllDifferent([blanche, rouge, verte, jaune, blue])
model.AddAllDifferent([norvegien, anglais, ukrainien, japonais, espagnol])
model.AddAllDifferent([cheval, renard, zebre,escargot, chien])
model.AddAllDifferent([thé, eau, lait, cafe, jus])
model.AddAllDifferent([sculpteur, diplomate, medecin, violoniste, acrobate])

model.Add(anglais == rouge)
model.Add(chien == espagnol)
model.Add(cafe == verte)
model.Add(ukrainien == thé)
model.Add(verte == blanche + 1)
model.Add(sculpteur == escargot)
model.Add(diplomate == jaune)
model.Add(lait == 3)
model.Add(norvegien == 1)
b = model.NewBoolVar("b")
model.Add(medecin < renard ).OnlyEnforceIf(b)
model.Add(medecin > renard).OnlyEnforceIf(b.Not())
model.Add(diplomate < cheval ).OnlyEnforceIf(b)
model.Add(diplomate > cheval ).OnlyEnforceIf(b.Not())
model.Add(violoniste == jus)
model.Add(japonais == acrobate)
model.Add(norvegien < blue ).OnlyEnforceIf(b)
model.Add(norvegien > blue).OnlyEnforceIf(b.Not())

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Solution trouvée :")
        for i in range(1, 6):
            print(f"\nMaison {i}:")
            # Couleur
            for var in X:
                if solver.Value(var) == i:
                    print(f"{var.Name()}")

else:
    print("Pas de solution trouvée.")

