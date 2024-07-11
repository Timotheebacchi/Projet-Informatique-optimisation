import csv 
import random
donnees = [ ]
fichier_csv = 'choix_eleves_projet_test.csv'

with open(fichier_csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['eleves', 'choix_projets','liste_projets'])

        for i in range(30):
                writer.writerow([])
                writer.writerow(['eleve' + str(i),'projet' + str(random.randint(0, 29)) + ";" + 'projet' + str(random.randint(0, 29)) + ";" +  'projet' + str(random.randint(0, 29)) + ";" + 'projet' + str(random.randint(0, 29)) + ";" + 'projet' + str(random.randint(0, 29)),"projet" + str(i)])

        for j in range(30,100):
                writer.writerow([])
                writer.writerow(['eleve' + str(j),'projet' + str(random.randint(0, 29)) + ";" + 'projet' + str(random.randint(0, 29)) + ";" +  'projet' + str(random.randint(0, 29)) + ";" + 'projet' + str(random.randint(0, 29)) + ";" + 'projet' + str(random.randint(0, 29))])
