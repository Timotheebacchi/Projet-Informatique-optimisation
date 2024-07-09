from flask import Flask, render_template, request, redirect, session
import pandas as pd

app = Flask(__name__)
app.secret_key = 'key'

liste = [["a"],["b","https://www.minesparis.psl.eu"],["c"]]

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
    if pword == "7LcN8R3k84qceJ" :
        session["connecte"] = "prof"
        return render_template("Teacher.html")

@app.route("/save_choice", methods = ['POST'])
def save() :
    request.json #<- dictionnaire qui contient les choix
    session #<- dictionnaire de l'identité

@app.route("/Teacher")
def teach() :
    return render_template("Teacher.html")

if __name__ == "__main__":
    app.run(debug=True)