from flask import Flask, render_template, request, redirect, session
import pandas as pd
import csv
import Programme_optimisation as po

app = Flask(__name__)
app.secret_key = 'key'

liste = [["glaciaire","https://fr.wikipedia.org/wiki/Glacier_(métier)"],
    ["jaugeages","https://fr.wikipedia.org/wiki/Jauge"],
    ["mont chauvel","https://fr.mappy.com/poi/5f72fe085e26a26ef844c1a2"],
    ["puzzle","https://fr.wikipedia.org/wiki/Puzzle"],
    ["sursaut-gamma","https://fr.wikipedia.org/wiki/Sursaut_gamma"],
    ["democratie","https://fr.wikipedia.org/wiki/Démocratie"],
    ["vieillissement-mouche","https://fr.wikipedia.org/wiki/Mouche"],
    ["cristal","https://fr.wikipedia.org/wiki/Cristal"],
    ["mines-paris","https://www.minesparis.psl.eu"]]

@app.route("/")

def user():
    return render_template("Username.html")

@app.route("/check_username", methods=["POST"])
def check_username() :
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    if nom == "Roy" and prenom == "Valerie" :
        return render_template("Pass.html")
    else :
        session["nom"] = nom
        session["prenom"] = prenom
        session["connecte"] = "eleve"
        return render_template("Choice_Page.html",toto=liste)

@app.route("/check_pass", methods=["POST"])
def check_pass() :
    pword = request.form["motdepasse"]
    if pword == "mines" :
        session["connecte"] = "prof"
        return render_template("Teacher.html")

@app.route("/save_choice", methods = ["POST"])
def save_choice() :
    d = request.json #<- dictionnaire qui contient les choix
    fichier_csv = 'choix_eleves_projet.csv'
    with open(fichier_csv, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Création d'une liste pour les valeurs de request.json
        valeurs_json = [d.get(str(i)) for i in range(1, 5)]
        # Concaténation des valeurs avec un séparateur ";"
        valeurs_concatenees = ";".join(valeurs_json)
        # Écriture dans le fichier CSV
        writer.writerow([session.get('prénom', '') + " " + session.get('nom', ''), valeurs_concatenees])
    return redirect("Saved", code=302)

@app.route("/Saved", methods = ['GET'])
def res() :
    return render_template("Saved.html")

@app.route("/runcode", methods = ['POST'])
def run() :
    l = po.main()
    return render_template("Results.html",result=l)

if __name__ == "__main__":
    app.run(debug=True)