import csv 
import random

fichier_csv = 'choix_eleves_projet_test.csv'
listproj = ["glaciaire","jaugeages","montchauvel","MDE-réseau-qgis","democratie","resan-tracabilité","scintigraphie1","scintigraphie2","coenergy","friend-concept","e-cube-linky","mines-paris",
        "germain-maureau","kleep","sursaut-gamma","engie-profiling","engie-actif","cbio-visu","keolis-offre","keolis-autonomie","scintigraphie3","datapred",
        "alumni-identifiant","puzzle","methane1","methane2","ocde-empreinte","chu-centrale-appel","pictet-trading-strategie","pictet-forecasting","vieillissement-mouche","scanner-low-cost","cristal"]
n = len(listproj)
listel = ["David Abulius","Valentin Allard","Amine Amzai","Gaspard Aractingi","Nejma Araki","Baptiste Auscher","Madeleine Banessy",
        "Mathis Bardot","Yannis Baron","Louis Barthelemy","Stephanie Bellini", "Gael Bigot", "Louis Bindel", "Denis Bonnand", "Fiona Bonnefoy Cudraz",
        "Mattis Borderies", "Simon Boudara","Louis Boulay","Quentin Bouquet","Antoine BdlR","Charlotte Bourny","Julie Boyer","Esther Braconnier"
        ]


with open(fichier_csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['eleves', 'choix_projets','liste_projets'])

        for i in range(min(n,len(listel))):
                writer.writerow([])
                writer.writerow([listel[i],listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" +  listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)],listproj[i]])

        for j in range(n,len(listel)):
                writer.writerow([])
                writer.writerow([listel(i),listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" +  listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)]])
