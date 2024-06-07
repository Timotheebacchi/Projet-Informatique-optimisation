
from gurobipy import multidict, Model, GRB
import pandas as pd 
donnees = pd.read_csv('choix_eleves_projet.csv',sep = ';')

# Préparation des données pour le multidict
combinaisons = {}  # Clés pour les combinaisons élève-projet
scores = {}        # Valeurs pour les scores correspondants

# Score attribué à chaque choix on pourra changer plus tard en fonction ,j'ai mis des scores linéaires, ce n'est pas nécéssairement le meilleure choix, on pourras faire une échelle de satisfaction intégrée
scores_choix = { 0: 100, 1: 80, 2: 60, 3: 40, 4: 20}

# Remplissage des dictionnaires
for index, ligne in donnees.iterrows():
    eleve = ligne['eleves']
    liste_projets = donnees['liste_projets']

    for projet in liste_projets:
        # On crée une clé unique pour chaque combinaison élève-projet
        cle = (eleve, projet)  # Supprime les espaces inutiles
        # On ajoute la clé dans le dictionnaire des combinaisons
        combinaisons[cle] = None 
        scores[cle] = 0
    projets_choisis = ligne['choix_projets'].split(';')  #split pour séparer les choix et les mettre dans une liste
    for choix, projets in enumerate(projets_choisis, start=1):
        # On associe le score correspondant au choix dans le dictionnaire des scores
        scores[cle] = scores_choix.get(choix, 0)

    
    


# Création du multidict
combinaisons, scores = multidict(scores)


m = Model("RAP")

# Chaque variable représente si un élève est assigné à un projet (1) ou non (0)
vars = m.addVars(combinaisons, vtype=GRB.BINARY, name="assignation")

# Ajout des contraintes
# Chaque élève est assigné à exactement un projet
for eleve in set(eleve for (eleve, projet) in combinaisons):
    m.addConstr(sum(vars[eleve, projet] for projet in projets_choisis if (eleve, projet) in vars) == 1, f"ContrainteUnProjet_{eleve}")

# Chaque projet a un nombre maximum de participants que je fixe pour l'instant à 5
for projet in set(projet for (eleve, projet) in combinaisons):
    m.addConstr(sum(vars[eleve, projet] for eleve in eleve if (eleve, projet) in vars) <= 5, f"ContrainteMaxParticipants_{projet}")

# Je veux maximiser le score total mais peut être pas le mieux (?) pourquoi pas plutôt avec un bien être moye meilleur, à voir avec valroy
m.setObjective(sum(vars[eleve, projet] * scores[eleve, projet] for eleve, projet in combinaisons), GRB.MAXIMIZE)

# Optimiser le modèle
m.optimize()


    

    

    


