import csv


def fn_ancetre(annee_de_prod):
    if (2021-annee_de_prod) >= 25:
        return True
    else:
        return False


def fn_encode(marque,modele,couleur,cylindre,motorisation,annee_de_prod):
    file_csv = "formulaire_garage.csv"
    header = ["marque", "modele", "couleur", "cylindre", "motorisation", "annee_de_production"]
    data = [marque, modele, couleur, cylindre, motorisation, annee_de_prod]
    with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)


# return fn_encode(marque, modele, couleur, cylindre, motorisation, annee_de_production)

def fn_question(question):
    return input(question)


q_marque = "Marque de la voiture : "
marque = fn_question(q_marque)
q_modele = "Modèle de la voiture : "
modele = fn_question(q_modele)
q_couleur = "couleur de la voiture :"
couleur = fn_question(q_couleur)
q_cylindre = "cylindre de la voiture :"
cylindre = fn_question(q_cylindre)
q_motorisation = "motorisation de la voiture :"
motorisation = fn_question(q_motorisation)
q_annee_de_prod= "année_de_production de la voiture :"
annee_de_prod = int(fn_question(q_annee_de_prod))

fn_encode(marque,modele,couleur,cylindre,motorisation,annee_de_prod)

if fn_ancetre(annee_de_prod):
    print(marque ,modele ,"est un ancetre")
else :
    print(marque ,modele ,"n'est pas un ancetre")