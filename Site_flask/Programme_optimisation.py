
from gurobipy import multidict, Model, GRB
import pandas as pd 

def main():
    donnees = pd.read_csv('choix_eleves_projet.csv',sep = ';')

    # Préparation des données pour le multidict
    combinaisons = {}  # Clés pour les combinaisons élève-projet
    scores = {}        # Valeurs pour les scores correspondants

    # Score attribué à chaque choix on pourra changer plus tard en fonction ,j'ai mis des scores linéaires, ce n'est pas nécéssairement le meilleure choix, on pourras faire une échelle de satisfaction intégrée
    scores_choix = { 1: 100, 2: 80, 3: 60, 4: 40, 5: 20}

    # Remplissage des dictionnaires
    for index, ligne in donnees.iterrows():
        eleve = ligne['eleves']
        liste_projets = donnees['liste_projets']

        for projet in liste_projets:
            # On crée une clé unique pour chaque combinaison élève-projet
            cle = (eleve, projet)  
            # On ajoute la clé dans le dictionnaire des combinaisons
            combinaisons[cle] = None 
            scores[cle] = 0
            projets_choisis = ligne['choix_projets'].split(';')  #split pour séparer les choix et les mettre dans une liste
        for choix, projets in enumerate(projets_choisis, start=1):
                # On associe le score correspondant au choix dans le dictionnaire des scores
                cle_choix = (eleve, projets)
                scores[cle_choix] = scores_choix.get(choix, 0)

        
    


    # Création du multidict
    combinaisons, scores = multidict(scores)


    m = Model("RAP")

    # Chaque variable représente si un élève est assigné à un projet (1) ou non (0)
    vars = m.addVars(combinaisons, vtype=GRB.BINARY, name="assignation")

    # Ajout des contraintes
    # Chaque élève est assigné à exactement un projet
    for eleve_boucle in set(eleve for (eleve, projet) in combinaisons):
        L=[]
        for (i,j) in combinaisons:
            if i==eleve_boucle:
                L.append(j)
        m.addConstr(sum(vars[eleve_boucle, projet] for projet in L ) == 1, f"ContrainteUnProjet_{eleve}")

    # Chaque projet a un nombre maximum de participants que je fixe pour l'instant à 5
    for projet_boucle in set(projet for (eleve, projet) in combinaisons):
        L=[]
        for (i,j) in combinaisons:
            if j==projet_boucle:
                L.append(i)

        m.addConstr(sum(vars[eleve, projet_boucle] for eleve in L) <= 5, f"ContrainteMaxParticipants_{projet}")

    # Je veux maximiser le score total mais peut être pas le mieux (?) pourquoi pas plutôt avec un bien être moye meilleur, à voir avec valroy
    m.setObjective(sum(vars[eleve, projet] * scores[eleve, projet] for eleve, projet in combinaisons), GRB.MAXIMIZE)

    # Optimiser le modèle
    m.optimize()
    Liste_renvoyée = []
    # Vérifier si le modèle a été résolu avec succès
    if m.status == GRB.OPTIMAL:
        # Parcourir toutes les variables de décision
        for cle, var in vars.items():
            # Si la variable est fixée à 1, la combinaison élève-projet a été choisie
            if var.x > 0.5:  # Utiliser 0.5 comme seuil pour les variables binaires
                eleve, projet = cle
                score = scores[cle]  # Récupérer le score de la combinaison à partir du dictionnaire des scores
               
                Liste_renvoyée.append(eleve +  " est assigné au " +   projet + " avec un score de " +  str(score))

    return Liste_renvoyée


L = main()

for i in L :
    print(i)
        


