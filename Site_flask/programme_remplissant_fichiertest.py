import csv 
import random

fichier_csv = 'choix_eleves_projet_test.csv'
listproj = ["glaciaire","jaugeages","montchauvel","MDE-réseau-qgis","democratie","resan-tracabilité","scintigraphie1","scintigraphie2","coenergy","friend-concept","e-cube-linky","mines-paris",
        "germain-maureau","kleep","sursaut-gamma","engie-profiling","engie-actif","cbio-visu","keolis-offre","keolis-autonomie","scintigraphie3","datapred",
        "alumni-identifiant","puzzle","methane1","methane2","ocde-empreinte","chu-centrale-appel","pictet-trading-strategie","pictet-forecasting","vieillissement-mouche","scanner-low-cost","cristal"]
n = len(listproj)


with open(fichier_csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['eleves', 'choix_projets','liste_projets'])

        for i in range(n):
                writer.writerow([])
                writer.writerow(['eleve' + str(i),listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" +  listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)],listproj[i]])

        for j in range(n,100):
                writer.writerow([])
                writer.writerow(['eleve' + str(j),listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" +  listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)]])
