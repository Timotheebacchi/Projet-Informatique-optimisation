import csv 
import random

fichier_csv = 'choix_eleves_projet_test.csv'
listproj = ["glaciaire","jaugeages","montchauvel","MDE-réseau-qgis","democratie","resan-tracabilité","scintigraphie1","scintigraphie2","coenergy","friend-concept","e-cube-linky","mines-paris",
        "germain-maureau","kleep","sursaut-gamma","engie-profiling","engie-actif","cbio-visu","keolis-offre","keolis-autonomie","scintigraphie3","datapred",
        "alumni-identifiant","puzzle","methane1","methane2","ocde-empreinte","chu-centrale-appel","pictet-trading-strategie","pictet-forecasting","vieillissement-mouche","scanner-low-cost","cristal"]
n = len(listproj)
listel = ["David Abulius","Valentin Allard","Amine Amzai","Gaspard Aractingi","Nejma Araki","Baptiste Auscher","Madeleine Banessy",
        "Mathis Bardot","Yannis Baron","Louis Barthelemy","Stephanie Bellini", "Gael Bigot", "Louis Bindel", "Denis Bonnand", "Fiona Bonnefoy Cudraz",
        "Mattis Borderies", "Simon Boudara","Louis Boulay","Quentin Bouquet","Antoine BdlR","Charlotte Bourny","Julie Boyer","Esther Braconnier",
        "Salomet Brichet","Dorian Brousse","Ombline Brunet","Louis Brusset","Antoine Campos","Mila Chabassier","Cyrianne Chabert","Aria Chafai",
        "Alice Chakroun","Antoine Chapelant","Benoit Charron","Marion Chatard","Axel Chaumel","Ilias Cherrat","AUrélie Chopard","Maxime Clergé",
        "Matti Comba","Agathe Cotte","Esteban Daude","Maxime De Bussac","Claire De Saint Méloir","Lise Dépinay","Valentin Deumier", "Colin Drouineau",
        "Alban Dujardin","Lilian Dupouy","Guillaume Duveau","Simpson Eng","Pierre Escudie","Augustin Ferrey","Liam Feve","Antoine Fondeur",
        "Olivier Fondeur","Achille Fruchard","Emeric Gandon","Anne Gabrielle Gibeili","Tom Graciet","Mathis Grillot","Eleonore Grison","Clément Herve",
        "Vincent Heynderickx","Nicolas Houbouyan","Donatien Houitte de la Chesnais","Camille Hua","Gwenaelle Hulard","Jules Imbert","Francois Jamet","Eric Kabis de St Chamas",
        "Jules Lagarde","Antoine Laumonier","Lucas le Gall","Pacome Lefebvre","Julie Leon","Titouan Lestanguet","Hannah Levallois","Lea Llinas",
        "Yanis Marmier","Orel Mazor","Timon Mesgouez","Neil Mikou","Luca Morabito","Sioban Nieradzik-Kozic","Alexandre Noel","Raphael Oculi",
        "Taha Oulhazzan","Emeline Padie","Justine Paleotti","Aymeric Papon","Benjamin Parent","Gabriel Patry","Mathis Peinaud","Gaspard Pereira",
        "Romain Perrin","Louis Philibert Nicol","Baptiste Piar","Paul Picard","Antonin Piechczyk","Raphael Pietravalle","Marianne Pinault","Raphael Poux",
        "Camille Prigent","Clara Pruneau","Nathan Rapin","Fatima Rharbal","Benjamin Rivet","Gregor Roncin","Enak Roubertie","Marc Samba",
        "Adelie Saule","Noemie Sauvage","Tom Schippke","Guillaume Setti","Elisa Skowronek","Samy Smail","Martin Sterin","Romain Teissandier",
        "Thomas Ternisien","Mathieu Toscano","Lucie Trolle","Chloe Vagner","Mathis Verdan","Gabriel Vibert","Benoit Vogel","Yanis Yarhzou","Francois Yvetot"]
with open(fichier_csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['eleves', 'choix_projets','liste_projets'])

        for i in range(min(n,len(listel))):
                writer.writerow([])
                writer.writerow([listel[i],listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" +  listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)],listproj[i]])

        for j in range(n,len(listel)):
                writer.writerow([])
                writer.writerow([listel[j],listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" +  listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)] + ";" + listproj[random.randint(0, n-1)]])
